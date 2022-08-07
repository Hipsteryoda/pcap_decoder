This project graphs the charging values defined below into a visual representation of a DC charging session.

Paramaters:
- Target/Requested Voltage
- Target/Requested Current
- Present/Delivered Voltage
- Present/Delivered Current
- Power (kW)

## Usage
------------------------------------------------------------

1. Place pcaps into `pcaps` directory (in original zipped format)
2. Pass the file you wish to analyze to the decode.sh script like: `./decode.sh pcaps/<file>`
a. Ex: `./decode.sh tap0-1656615284.pcap.zip`
3. The output will be two graphs, one showing target and present voltages and currents, the other showing calculated power based on present voltage and current.