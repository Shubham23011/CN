import json
import random
used_ports = set()


class EndDevice:
    # def __init__(self, h, device_no):
    #     self.h = h
    #     self.device_no = device_no
    def __init__(self, h, port_number, device_name):
        self.h = h
        self.port_number = port_number
        self.device_name = device_name


    def send_acc(self, name,respond_devices):
        self.h.get_data("ack", name, [self.device_name, self.port_number],respond_devices)

    def get_data(self, msg, reciver_devices, devices,respond_devices):

        if reciver_devices[1] == self.port_number:
            if msg != "ack":
                print(
                    f"Received data is:  { msg}   by device  {devices[0]} ({str(devices[1])})")
                respond_devices.append( f"Received data is:  { msg}   by device  {devices[0]} ({str(devices[1])})")

                self.send_acc(devices,respond_devices)


            else:
                print(
                    f"Ack received by device:{self.device_name} ( { str(self.port_number) } ) and send by device:{devices[0]} ( {str(devices[1])})")
                respond_devices.append( f"Ack received by device:{self.device_name} ( { str(self.port_number) } ) and send by device:{devices[0]} ( {str(devices[1])})")

    def send_data(self, msg, reciver_devices,respond_devices ):
        self.h.get_data(msg, reciver_devices,
                        [self.device_name, self.port_number],respond_devices)



class Hub:
    def __init__(self):
        self.list_of_devices = []


    def get_data(self, msg, reciver_devices, devices,respond_devices):
        for device in self.list_of_devices:
            device.get_data(msg, reciver_devices, devices,respond_devices)


    def make_list(self, ar_hub):
        self.list_of_devices = ar_hub


def classdata(reciver_devices, sender_devices,message):
    end_devices = []

    respond_devices = []

    with open("device.json", "r") as json_file:
        devices_data = json.load(json_file)

    with open("device_ports.json", "r") as json_file:
        devices_data_port = json.load(json_file)
    h = Hub()
    for device_data in devices_data_port:
        devices_name = device_data["device_name"]
        port_number = device_data["port_number"]
        end_device = EndDevice(h, port_number, devices_name)
        end_devices.append(end_device)

    h.make_list(end_devices)

    # for device_data in devices_data_port:
    #     port_number = device_data["port_number"]
    #     end_device = EndDevice(h, port_number)
    #     end_devices.append(end_device)
    # Assuming end_device1 is the first device in the list
    end_device = find_matching_device(sender_devices[1], end_devices)

    end_device.send_data(message, reciver_devices,respond_devices)

    return respond_devices

def find_matching_device(port_number, end_devices):
    for device in end_devices:
        if device.port_number == port_number:
            return device
    return None


def generate_random_port():
    global used_ports
    while True:
        port = random.randint(1024, 65535)
        if port not in used_ports:
            used_ports.add(port)
            return port


used_mac_addresses = set()


def generate_random_mac():
    global used_mac_addresses
    while True:
        # Generate a random MAC address in the format xx:xx:xx:xx:xx:xx
        mac_address = ':'.join(
            f'{random.randint(0, 255):02x}' for _ in range(6))
        if mac_address not in used_mac_addresses:
            used_mac_addresses.add(mac_address)
            return mac_address


def port_and_mac_assigen_to_devices(devices):
    device_ports = []

    data = []

# Write the modified data back to the file
    with open("device_ports.json", "w") as json_file:
        json.dump(data, json_file)


    for device_name in devices:
        port_number = generate_random_port()
        mac_number = generate_random_mac()
        device_info = {"device_name": device_name,

                       "port_number": str(port_number), "mac_number": mac_number}

        device_ports.append(device_info)

    json_data = json.dumps(device_ports, indent=4)
    with open("device_ports.json", "w") as json_file:
        json_file.write(json_data)

    json_devicesdata = json.dumps(devices, indent=4)
    with open("device.json", "w") as json_file:
        json_file.write(json_devicesdata)


    return device_ports

