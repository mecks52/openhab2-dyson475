'''
Prepares the files for usage in openHAB.
Script asks for the SSID and password from sticker, transfers them to the
needed configuration information and stores it into th the openHAB files.
'''
import base64
import hashlib

# Ask for information from device
print("Which type of Dyson air purifier do you use?\n")
print(" 455 - Pure Hot + Cool Link\n")
print(" 469 - Pure Cool Link\n")
print(" 475 - Pure Cool Link Tower\n")
ap_type = input("type (e.g. 455):")
print("Type in the information from the sticker inside your\n")
print("Dyson air purifier:")
ssid = input("Product SSID (e.g.: DYSON-NN2-EU-ABC1234D-475):")
pwd = input("Product WiFi Password (e.g.: adgjsfhk):")
ip_addr = input("Type in the IP-Adress of the air purifier (e.g. 192.168.178.100):")

# Transfer ssid to device identification
dev_id = ssid[6:21]
# Transfer password to hash version
hash = hashlib.sha512()
hash.update(pwd.encode('utf-8'))
pwd_hash = base64.b64encode(hash.digest()).decode('utf-8')

# Create dysonapbroker.things file
ap_broker = "./dysonapbroker.things"
with open(ap_broker, 'r') as ap_broker_f:
    ap_broker_cfg_str = ap_broker_f.read()
    ap_broker_cfg_str = ap_broker_cfg_str.replace("<ap_type>", ap_type)
    ap_broker_cfg_str = ap_broker_cfg_str.replace("<dev-id>", dev_id)
    ap_broker_cfg_str = ap_broker_cfg_str.replace("<pwd-hash>", pwd_hash)
    ap_broker_cfg_str = ap_broker_cfg_str.replace("<ip-addr>", ip_addr)
ap_broker_f.close()
with open("dysonapbroker.things", 'w') as ap_broker_f:
    ap_broker_f.write(ap_broker_cfg_str)
ap_broker_f.close()

# Create dysonXXX.items file
dyson_items = "./dyson"+ap_type+".items"
with open(dyson_items, 'r') as dyson_items_f:
    dyson_items_str = dyson_items_f.read()
    dyson_items_str = dyson_items_str.replace("<dev-id>", dev_id)
dyson_items_f.close()
with open(dyson_items, 'w') as dyson_items_f:
    dyson_items_f.write(dyson_items_str)
dyson_items_f.close()
