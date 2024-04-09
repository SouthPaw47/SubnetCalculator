from math import log2, ceil
from ipaddress import IPv4Network, IPv4Address

# returns the class of the given IP Address
def get_ip_class(ip):
  ip_1_octat = int(ip.split(".")[0])
  
  if ip_1_octat >= 0 and ip_1_octat <= 127:
    return 8 # class A
   
  if ip_1_octat >=128 and ip_1_octat <= 191:
    return 16 # class B
   
  if ip_1_octat >= 192 and ip_1_octat <= 223:
    return 24 # class C
   
  return 0

# calculates how much bits needed for the given number
def get_subnet_bits(num):
    num = int(num)
    return ceil(log2(num))

# updates the cider, subnet and host based on the users choice
def update_cidr(choice, choice_num, cidr):
    if choice == "subnets":
        subnet_bits = get_subnet_bits(choice_num)
        cidr += subnet_bits
        hosts_bits = 32 - cidr
    else:
        hosts_bits = get_subnet_bits(choice_num)
        subnet_bits = 32 - hosts_bits - cidr
        cidr = 32 - hosts_bits
        
    return cidr, subnet_bits, hosts_bits

def cidr_to_subnet_mask(cidr):
    # Calculate the number of full octets
    full_octets = cidr // 8

    # Calculate the number of bits in the last octet
    remaining_bits = cidr % 8

    # Initialize an empty subnet mask list
    subnet_mask_octets = []

    # Append full octets (each octet has 8 bits)
    subnet_mask_octets.extend([255] * full_octets)

    # Add partial octet if necessary
    if remaining_bits > 0:
        subnet_mask_octets.append(int('1' * remaining_bits, 2) << (8 - remaining_bits))
        # Fill remaining octets with 0
        subnet_mask_octets.extend([0] * (4 - len(subnet_mask_octets)))

    # Convert octets to string and join them with periods
    subnet_mask = '.'.join(map(str, subnet_mask_octets))

    return subnet_mask
    
def calculate_hosts(cidr):
    return 2 ** (32 - cidr) - 2

def calculate_subnets(cidr):
    return 2 ** (32 - cidr)

def calculate_network_address(ip_address, cidr):
    ip_octets = list(map(int, ip_address.split('.')))
    cidr_octets = cidr // 8
    remaining_bits = cidr % 8

    network_octets = ip_octets[:cidr_octets]

    if remaining_bits > 0:
        last_octet = ip_octets[cidr_octets]
        network_octets.append(last_octet & (255 << (8 - remaining_bits)))

    network_octets.extend([0] * (4 - len(network_octets)))

    return '.'.join(map(str, network_octets))

def calculate_broadcast_address(network_address, cidr):
    network_octets = list(map(int, network_address.split('.')))
    cidr_octets = cidr // 8
    remaining_bits = cidr % 8

    broadcast_octets = network_octets[:cidr_octets]

    if remaining_bits > 0:
        last_octet = network_octets[cidr_octets]
        broadcast_octets.append((last_octet | (255 >> remaining_bits)))

    broadcast_octets.extend([255] * (4 - len(broadcast_octets)))

    return '.'.join(map(str, broadcast_octets))

def calculate_first_two_hosts(network_address):
    first_host = network_address[:-1] + str(int(network_address[-1]) + 1)
    second_host = network_address[:-1] + str(int(network_address[-1]) + 2)
    return first_host, second_host

def calculate_last_two_hosts(broadcast_address):
    last_host = broadcast_address[:-1] + str(int(broadcast_address[-1]) - 1)
    second_last_host = broadcast_address[:-1] + str(int(broadcast_address[-1]) - 2)
    return second_last_host, last_host



