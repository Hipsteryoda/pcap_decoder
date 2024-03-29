This project graphs the charging values defined below into a visual representation of a DC charging session.

Paramaters:
- Target/Requested Voltage
- Target/Requested Current
- Present/Delivered Voltage
- Present/Delivered Current
- Power (kW)

## Usage
------------------------------------------------------------

### Linux

NOTE: If the wireshark-v2g plugin is not properly installed and decoding pcaps correctly, you will get `This session ({file}) did not make it to current demand.` everytime.\
NOTE2: If you already have a decoded pcap file in a .txt format, you can simply use `decode.py <file>` to get graphical representations of the session.
1. Install requirements with `pip install -r requirements.txt`
2. Place pcaps into `pcaps` directory (in original zipped format)
3. Pass the file you wish to analyze to the decode.sh script like: `./decode.sh pcaps/<file>`\
  a. Ex: `./decode.sh pcaps/tap0-1656615284.pcap.zip`
4. The output will be two graphs, one showing target and present voltages and currents, the other showing calculated power based on present voltage and current.


### Just Using `decoder.py`

If you already have a pcap file that has been decoded through the wireshark-v2g in a text format, you can simply pass that file as an argument to `decoder.py` to get the graphical representation of the session.

1. `./decoder.py <file.txt>`
