#!/usr/bin/env python3

from validations import *
from helpers import *
import ipaddress

ip = input("Please enter an IP address: ")
if not validate_ip(ip):
    print("Invalid IP Address!")
    exit(1)

cidr = input("Please enter a Subnet mask in CIDR (Optional): ")
if len(cidr) == 0:
    cidr = get_ip_class(ip)
elif not validate_cidr(cidr):
    print("Invalid Subnet mask CIDR!")
    exit(1)

choice = input("Please enter whether you want hosts or subnets: (hosts/subnets) ")
if not validate_choice(choice):
    print("Invalid Option!")
    exit(1)

number_of_choice = input(f"Please enter number of {choice}: ")
if not validate_number(number_of_choice):
    print(f"Invalid Number of {choice}!")
    exit(1)

print("Success!")

cidr, sub, hos = update_cidr(choice, int(number_of_choice), int(cidr))
broadcastId = calculate_broadcast_address(ip , cidr)
networkId =  calculate_network_address(ip , cidr)
subnetamount = calculate_subnets(cidr)
hostamount = calculate_hosts(cidr)
firstTwo = calculate_first_two_hosts(networkId)
lastTwo = calculate_last_two_hosts(broadcastId)
print("Subnet Mask : " + cidr_to_subnet_mask(cidr))
print("CIDR : " + str(cidr))
print("Subnets : " + str(subnetamount))
print("Hosts : " + str(hostamount))
print("Network ID : " + str(networkId))
print("Broadcast ID : " + str(broadcastId))
print("First two hosts : " + str(firstTwo))
print("Last two hosts : " + str(lastTwo))








