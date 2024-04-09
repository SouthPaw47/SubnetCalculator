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

choice = "subnets"
number_of_choice = 4
cidr = 23

print(f"number of {choice} = {number_of_choice}, bits = {get_subnet_bits(number_of_choice)}")
if choice == "subnets":
    cidr += get_subnet_bits(number_of_choice)