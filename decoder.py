#!/usr/bin/python3

### MODULE IMPORTS ###
import pandas as pd
import numpy as np 

# Regex for text parsing in PCAP file
import re

# Plotting stuff
import matplotlib.pyplot as plt
import seaborn as sns

# Accepting CLI input
import sys

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

    df = pd.DataFrame(
        data={'present_voltage':present_vol, 'present_current':present_cur, 'target_voltage':target_vol, 'target_current':target_cur}
        )

    return df

def graph(df):
    fig, ax = plt.subplots(figsize=(70,40), frameon=True)
    plt.axis(True)

    ax.plot(df['present_voltage'], label='Present Voltage', color='red')
    ax.plot(df['target_voltage'], label='Target Voltage', color='orange')

    ax2 = ax.twinx()
    ax2.plot(df['present_current'], label='Present Current', color='green')
    ax2.plot(df['target_current'], label='Target Current', color='blue')

    plt.show()

    fig.savefig('plot.jpg', bbox_inches='tight')


### RUN ###

# TODO: Support passing of multiple files to script
file = sys.argv[1]

vol, cur = parse(file)
if len(vol) == 0 or len(cur) == 0:
    print(f'This session ({file}) did not make it to current demand.\n')
else:
    vol, cur = lesser(vol, cur)
    df = df_data(vol, cur)
    graph(df)


