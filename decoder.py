#!/usr/bin/python3

### MODULE IMPORTS ###
from shutil import which
import pandas as pd
import numpy as np 

# Regex for text parsing in PCAP file
import re

# Plotting stuff
import matplotlib.pyplot as plt
import seaborn as sns

# Accepting CLI input
import sys, os

### FUNCTION DEFINITIONS ###

# frame = re.compile(r'Frame (\d*):')
def parse(file):
    voltage = re.compile(r'Voltage: (\d+)')
    current = re.compile(r'Current: (\d*)')

    with open(file) as file:
        text = file.read()
        # fra = re.findall(frame, text)
        vol = re.findall(voltage, text)
        cur = re.findall(current, text)

    return vol, cur

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def lesser(list1, list2):
    # if list 1 is longer, truncate list 1 to the lenght of list 2
    if list1 > list2:
        list1 = list1[:len(list2)]
    
    # if list 2 is loger, truncate list 2 to the length of list 1
    elif list1 < list2:
        list2 = list2[:len[list1]]

    # else, do nothing
    else:
        pass

    return list1, list2

def df_data(vol, cur):
    present_vol = []
    present_cur = []
    target_vol = []
    target_cur = []

    for n in range(len(vol)):

        if is_even(n):
            target_vol.append(vol[n])
            target_cur.append(cur[n])

        else:
            present_vol.append(vol[n])
            present_cur.append(cur[n])

    target_vol, present_vol = lesser(target_vol, present_vol)
    target_cur, present_cur = lesser(target_cur, present_cur)

    df = pd.DataFrame(
        data={'present_voltage':present_vol, 'present_current':present_cur, 'target_voltage':target_vol, 'target_current':target_cur}
        )
    # Cleanup for missing values
    df = df.replace('', np.NaN)
    
    df = df.astype(float)

    # Calculate present power 
    v = df.present_voltage.to_numpy()
    i = df.present_current.to_numpy()

    # Power in kW
    p = (v * i) / 1000

    df['present_power'] = p

    return df

def graph(df, filename):
    
    fig, ax = plt.subplots(figsize=(70,40), frameon=True)
    plt.axis(True)
    plt.grid(visible=True)

    # Setting Axis Labels and Size
    # plt.xlabel('Frames', fontsize=40)
    plt.ylabel('Voltage (V)', fontsize=40)

    # Graphing both Voltage values
    ax.plot(
        df['present_voltage'], 
        label='Present Voltage', 
        color='red', 
        linewidth=4
        )
    # Make target values thinner lines and dashed for easier visual differentiation
    ax.plot(
        df['target_voltage'], 
        label='Target Voltage', 
        color='orange', 
        linewidth=2,
        linestyle='--'
        )

    # Set tick paramaters and set legend
    ax.tick_params(axis='both', which='major', labelsize=30)
    ax.legend(loc=2, fontsize='xx-large')

    # Graphing both Current values
    ax2 = ax.twinx()
    ax2.plot(
        df['present_current'], 
        label='Present Current', 
        color='green', 
        linewidth=4
        )
    # Make target values thinner lines and dashed for easier visual differentiation
    ax2.plot(
        df['target_current'], 
        label='Target Current', 
        color='blue', 
        linewidth=2,
        linestyle='--'
        )

    # Set tick paramaters and set legend for second axis
    ax2.tick_params(axis='both', which='major', labelsize=30)
    ax2.legend(loc=1, fontsize='xx-large')
    
    plt.show()

    fig.savefig(filename+'.jpg', bbox_inches='tight')

def graph_kw(df, filename):
    # Define data to graph
    p = df.present_power

    # Create graph and labels
    plt.plot(
        p,
        color='magenta'
    )
    plt.title('Charging Rate over Time (kW)')
    # plt.xlabel('Frames')
    plt.ylabel('Power (kW)')
    
    plt.savefig(filename+'.jpg', bbox_inches='tight')


### RUN ###

# TODO: Support passing of multiple files to script
file = sys.argv[1]

vol, cur = parse('./pcaps/'+file)
if len(vol) == 0 or len(cur) == 0:
    print(f'This session ({file}) did not make it to current demand.\n')
else:
    vol, cur = lesser(vol, cur)
    df = df_data(vol, cur)
    graph(df, file)
    graph_kw(df, file+'_present_power')


