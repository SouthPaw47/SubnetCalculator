# SubnetCalculator
This repository contains Python code for a subnetting calculator. It allows users to input an IP address and optionally a subnet mask in CIDR notation, and then choose whether they want to calculate based on the number of hosts or the number of subnets. The calculator provides various details such as subnet mask, CIDR notation, number of hosts, number of subnets, network address, broadcast address, and details about the first and last two hosts. <br>
## Modules <br>
### `validation.py` <br>
This module contains functions for validating user inputs such as IP addresses, CIDR notations, choices (hosts or subnets), and numeric values. <br>

### `helpers.py` <br>
The helpers module contains various helper functions used in subnetting calculations, such as determining the IP class, calculating subnet bits, updating CIDR, converting CIDR to subnet mask, and calculating network addresses and broadcast addresses. <br>

### `main.py` <br>
The main module serves as the entry point for the subnetting calculator. It prompts the user for inputs, validates them using the functions from the `validation.py` module, and performs subnetting calculations using the functions from the `helpers.py` module. Finally, it displays the calculated details to the user. <br>

### `Usage` <br>
To use the subnetting calculator, follow these steps: <br>

Run the `main.py` script. <br>
Enter the IP address when prompted. <br>
Optionally, enter the subnet mask in CIDR notation. <br>
Choose whether you want to calculate based on hosts or subnets. <br>
Enter the number of hosts or subnets. <br>
The calculator will display the calculated details, including subnet mask, CIDR notation, number of hosts, number of subnets, network address, broadcast address, and details about the first and last two hosts. <br>
