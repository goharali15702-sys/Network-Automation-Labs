# Python Data Types
# Network Automation Fundamentals


# 1. Integer
ssh_timeout = 30

print(ssh_timeout)
print(type(ssh_timeout))


# 2. Float
ios_version = 15.4

print(ios_version)
print(type(ios_version))


# 3. String
hostname = "R1"

print(hostname)
print(type(hostname))


# 4. Boolean
device_up = True

print(device_up)
print(type(device_up))


# 5. List
devices = ["ASA", "NEXUS", "CATALYST", "ASR"]

print(devices)
print(type(devices))

# List is ordered and indexed
print(devices[0])
print(devices[1])
print(devices[3])

# List is changeable
devices[1] = "ROUTER"
print(devices)


# 6. Tuple
ip_addr = ("10.254.0.1", "10.254.0.2", "10.254.0.3")

print(ip_addr)
print(type(ip_addr))

# Tuple is indexed
print(ip_addr[0])
print(ip_addr[1])

# Tuple is immutable (cannot be changed)
# ip_addr[0] = "10.254.0.10"


# 7. Dictionary
if_state = {
    "Gi0/1": "shutdown",
    "Gi0/2": "no shutdown"
}

print(if_state)
print(type(if_state))

# Access dictionary values using keys
print(if_state["Gi0/1"])
print(if_state["Gi0/2"])

# Dictionary is changeable
if_state["Gi0/1"] = "no shutdown"
print(if_state)


# 8. Set
if_names = {"Gi0/1", "Gi0/2", "Gi0/3", "Gi0/1"}

print(if_names)
print(type(if_names))