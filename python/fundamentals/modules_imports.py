# Python Module Import Practice

# 1. Import the complete module
import network_devices

print(network_devices.ROUTER)


# 2. Import a specific object from the module
from network_devices import IP_ADDRESS

print(IP_ADDRESS)


# 3. Import a module using an alias
import network_devices as nd

print(nd.USERNAME)


# 4. Import a specific object using an alias
from network_devices import USERNAME as user

print(user)