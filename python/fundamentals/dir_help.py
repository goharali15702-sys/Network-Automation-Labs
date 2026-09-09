# Python dir() and help()
# Network Automation Fundamentals


# 1. dir() — Discover available methods

devices = ["R1", "R2", "R3"]

print(dir(devices))


# 2. help() — Get information about a method

help(devices.append)


# 3. Using a method discovered with dir()

devices.append("R4")

print(devices)