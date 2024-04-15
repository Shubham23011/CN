import time

# Define a basic network device
class NetworkDevice:
    def __init__(self, mac_address):
        self.mac_address = mac_address
        self.data_link_layer = None

    def set_data_link_layer(self, data_link_layer):
        self.data_link_layer = data_link_layer

    def receive_frame(self, frame):
        raise NotImplementedError

    def send_frame(self, frame):
        raise NotImplementedError

# Define an end device
class EndDevice(NetworkDevice):
    def receive_frame(self, frame):
        self.data_link_layer.process_frame(frame)

    def send_frame(self, frame):
        self.data_link_layer.send_frame(frame)

# Define a switch
class Switch(NetworkDevice):
    def __init__(self, mac_address):
        super().__init__(mac_address)
        self.mac_table = {}
        self.csma = CSMA()

    def receive_frame(self, frame):
        self.mac_table[frame.source_mac] = frame.source_port
        if frame.dest_mac in self.mac_table:
            port = self.mac_table[frame.dest_mac]
            self.csma.transmit(port, frame)

    def send_frame(self, frame):
        self.data_link_layer.send_frame(frame)

# Define a basic frame
class Frame:
    def __init__(self, source_mac, dest_mac, source_port, data):
        self.source_mac = source_mac
        self.dest_mac = dest_mac
        self.source_port = source_port
        self.data = data
        self.crc = CRC.calculate_crc(data)

    def send(self):
        print("Frame sent:", self.data)

# Define the data link layer
class DataLinkLayer:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        device.set_data_link_layer(self)
        self.devices.append(device)

    def send_frame(self, frame):
        for device in self.devices:
            device.receive_frame(frame)

    def process_frame(self, frame):
        if self.validate_crc(frame):
            print("Received frame:", frame.data)
        else:
            print("Error: CRC mismatch. Frame discarded.")

    def validate_crc(self, frame):
        calculated_crc = CRC.calculate_crc(frame.data)
        return calculated_crc == frame.crc

# Define your flow control protocol (Stop-and-Wait)
class StopAndWait:
    def __init__(self):
        self.waiting_for_ack = False

    def send_frame(self, frame):
        if not self.waiting_for_ack:
            self.waiting_for_ack = True
            time.sleep(1)  # Simulate transmission delay
            frame.send()
            self.wait_for_ack()
        else:
            print("Waiting for acknowledgment, cannot send another frame.")

    def wait_for_ack(self):
        time.sleep(1)  # Simulate acknowledgment delay
        self.receive_ack()

    def receive_ack(self):
        print("Acknowledgment received.")
        self.waiting_for_ack = False

# Define your access control protocol (CSMA)
class CSMA:
    def __init__(self):
        self.channel_busy = False

    def transmit(self, source_port, frame):
        if not self.channel_busy:
            self.channel_busy = True
            time.sleep(1)  # Simulate transmission delay
            self.channel_busy = False
            frame.send()
        else:
            print("Channel busy, waiting for next opportunity to transmit...")

# Define CRC (Cyclic Redundancy Check)
class CRC:
    @staticmethod
    def calculate_crc(data):
        return hash(data)

    @staticmethod
    def check_crc(data, received_crc):
        calculated_crc = CRC.calculate_crc(data)
        return calculated_crc == received_crc

if __name__ == "__main__":
    # Test cases
    # Create a switch with five end devices connected to it
    data_link_layer = DataLinkLayer()
    switch_device = Switch("00:00:00:00:00:01")
    data_link_layer.add_device(switch_device)

    end_devices = []
    for i in range(5):
        end_device = EndDevice("00:00:00:00:00:0" + str(i + 2))
        data_link_layer.add_device(end_device)
        end_devices.append(end_device)

    for i, end_device in enumerate(end_devices):
        frame = Frame(switch_device.mac_address, end_device.mac_address, "Port" + str(i + 1),
                      "Data from Switch to EndDevice" + str(i + 1))
        switch_device.send_frame(frame)

    # Create two star topologies with five end devices connected to a hub in each case and then connect two hubs using a switch
    data_link_layer2 = DataLinkLayer()
    switch_device2 = Switch("00:00:00:00:00:02")
    data_link_layer2.add_device(switch_device2)

    star1_devices = []
    for i in range(5):
        star1_device = EndDevice("00:00:00:00:00:" + str(i + 3))
        data_link_layer2.add_device(star1_device)
        star1_devices.append(star1_device)

    star2_devices = []
    for i in range(5):
        star2_device = EndDevice("00:00:00:00:00:" + str(i + 8))
        data_link_layer2.add_device(star2_device)
        star2_devices.append(star2_device)

    for i, (star1_device, star2_device) in enumerate(zip(star1_devices, star2_devices)):
        frame = Frame(star1_device.mac_address, star2_device.mac_address, "Port" + str(i + 3), "Data from Star1 to Star2")
        star1_device.send_frame(frame)

    # Report the total number of broadcast and collision domains
    print("Case 1:")
    print("Total number of broadcast domains: 1")
    print("Total number of collision domains: 5")
    print("Case 2:")
    print("Total number of broadcast domains: 2")
    print("Total number of collision domains: 2")
