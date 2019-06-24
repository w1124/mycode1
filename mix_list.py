#!/usr/bin/python3

my_list= ["192.168.0.5", 5080, "UP"]

print("The first item in the list (IP):" + my_list[0])

print("The second item in the list (port): " + str(my_list[1]))

print("The third item in the list (state): " + my_list[2])


new_list= [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

print("The first item in the list (port):" + str(new_list [0]))

print(str(new_list[3] + " is unable to ssh:" + str(new_list[0])))

print(f"When I ssh into IP address {new_list[3]} or {new_list[4]} i am unable to ping ports {new_list[0]}, {new_list[1]}, or {new_list[2]}.")
