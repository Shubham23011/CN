class EndDevice:
    def __init__(self, h, device_no):
        self.h = h
        self.device_no = device_no

    def send_ack(self, name):
        self.h.get_data("ack", name, self.device_no)

    def get_data(self, s, device_name, name):
        if device_name == self.device_no:
            if s != "ack":
                print("Received data is: " + s + "; by device " + str(name))
                self.send_ack(name)
            else:
                print("Ack received by device: " + str(self.device_no) + "; and send by device: " + str(name))

    def send_data(self, data, device_name, topo):
        if topo == 1:
            self.h.get_data(data, device_name, self.device_no)
        else:
            pass


class Hub:
    def __init__(self):
        self.list_of_devices = []

    def get_data(self, data, device_name, device_by):
        for device in self.list_of_devices:
            device.get_data(data, device_name, device_by)

    def make_list(self, ar_hub):
        self.list_of_devices = ar_hub


def main():
    h = Hub()
    end_device1 = EndDevice(h, 1)
    end_device2 = EndDevice(h, 2)
    end_device3 = EndDevice(h, 3)
    end_device4 = EndDevice(h, 4)
    end_device5 = EndDevice(h, 5)
    ar_hub = [end_device1, end_device2, end_device3, end_device4, end_device5]
    h.make_list(ar_hub)
    end_device1.send_data("hello bro", 2, 1)


if __name__ == "__main__":
    main()
