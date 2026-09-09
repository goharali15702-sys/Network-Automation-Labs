# Python Type Conversion
# Network Automation Fundamentals


# 1. int() — String → Integer

timeout = "30"

print(timeout)
print(type(timeout))

timeout_number = int(timeout)

print(timeout_number)
print(type(timeout_number))


# 2. float() — String → Float

version = "15.4"

print(version)
print(type(version))

version_number = float(version)

print(version_number)
print(type(version_number))


# 3. str() — Integer → String

device_id = 1

print(device_id)
print(type(device_id))

device_id_text = str(device_id)

print(device_id_text)
print(type(device_id_text))


# 4. bool() — Value → Boolean

print(bool(0))
print(bool(1))
print(bool(""))
print(bool("R1"))


# 5. list() — Tuple → List

devices = ("R1", "R2", "R3")

print(devices)
print(type(devices))

device_list = list(devices)

print(device_list)
print(type(device_list))


# 6. tuple() — List → Tuple

devices = ["R1", "R2", "R3"]

print(devices)
print(type(devices))

device_tuple = tuple(devices)

print(device_tuple)
print(type(device_tuple))


# 7. set() — List → Set

devices = ["R1", "R2", "R3", "R1"]

print(devices)

device_set = set(devices)

print(device_set)
print(type(device_set))


# 8. dict() — List of Tuples → Dictionary

devices = [
    ("R1", "Router"),
    ("SW1", "Switch"),
    ("FW1", "Firewall")
]

device_dict = dict(devices)

print(device_dict)
print(type(device_dict))