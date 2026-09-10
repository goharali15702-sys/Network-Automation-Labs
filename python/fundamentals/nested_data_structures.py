# Python Nested Data Structures
# Network Automation Fundamentals


# 1. List → Tuple
devices = [
    ("R1", "Router"),
    ("SW1", "Switch")
]

print(devices[0])
print(devices[0][0])
print(devices[0][1])


# 2. Dictionary → Dictionary
devices = {
    "R1": {
        "type": "Router",
        "ip": "10.0.0.1"
    },
    "SW1": {
        "type": "Switch",
        "ip": "10.0.0.2"
    }
}

print(devices["R1"])
print(devices["R1"]["type"])
print(devices["R1"]["ip"])

print(devices["SW1"]["type"])
print(devices["SW1"]["ip"])


# 3. Dictionary → List
devices = {
    "routers": ["R1", "R2", "R3"],
    "switches": ["SW1", "SW2", "SW3"]
}

print(devices["routers"])
print(devices["routers"][0])
print(devices["routers"][1])

print(devices["switches"])
print(devices["switches"][0])


# 4. List → Dictionary
devices = [
    {
        "hostname": "R1",
        "type": "Router",
        "ip": "10.0.0.1"
    },
    {
        "hostname": "SW1",
        "type": "Switch",
        "ip": "10.0.0.2"
    }
]

print(devices[0])
print(devices[0]["hostname"])
print(devices[0]["type"])
print(devices[0]["ip"])

print(devices[1]["hostname"])
print(devices[1]["type"])
print(devices[1]["ip"])