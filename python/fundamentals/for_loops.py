# Python For Loops
# Network Automation Fundamentals


# Example 1: Basic for loop
devices = ["R1", "R2", "R3"]

for device in devices:
    print(device)


# Example 2: for loop with multiple statements
for device in devices:
    print("Starting", device)
    print("Checking", device)

print("All checks complete")


# Example 3: for loop with nested dictionaries
devices = [
    {"hostname": "R1", "ip": "10.0.0.1"},
    {"hostname": "R2", "ip": "10.0.0.2"},
    {"hostname": "R3", "ip": "10.0.0.3"}
]

for device in devices:
    print(device["hostname"], device["ip"])


# Example 4: for loop + if/else
devices = [
    {"hostname": "R1", "status": "up"},
    {"hostname": "R2", "status": "down"},
    {"hostname": "R3", "status": "up"}
]

for device in devices:
    if device["status"] == "up":
        print(device["hostname"], "is ready")
    else:
        print(device["hostname"], "needs attention")


# Example 5: range()
for number in range(5):
    print(number)


# Example 6: range(start, stop)
for vlan in range(10, 16):
    print("Checking VLAN", vlan)


# Example 7: range(start, stop, step)
for number in range(2, 10, 2):
    print(number)


# Example 8: range() + if
for vlan in range(10, 16):
    if vlan % 2 == 0:
        print("VLAN", vlan, "is even")


# Example 9: range() + if/else
for vlan in range(10, 14):
    if vlan % 2 == 0:
        print("VLAN", vlan, "is even")
    else:
        print("VLAN", vlan, "is odd")


# Example 10: Networking-style example
vlans = [10, 11, 12, 13, 14, 15]

for vlan in vlans:
    if vlan == 12 or vlan == 15:
        print("VLAN", vlan, "needs attention")
    else:
        print("VLAN", vlan, "is OK")
        