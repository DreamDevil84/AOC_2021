def convert_binary_to_decimal(binary_string: str) -> int:
    power = len(binary_string) - 1
    num = 0
    for char in range(len(binary_string)):
        num += int(binary_string[char]) * pow(2, power)
        power -= 1
    return num


class Packet:
    def __init__(self, string: str):
        decoder = Decoder()
        self.version = decoder.convert_binary_to_hex(string[:3])
        self.type = decoder.convert_binary_to_hex(string[3:6])
        self.id = -1
        self.literal_value: int = 0
        self.sub_packets = []
        content = string[6:]
        if self.type == '4':
            write_content = True
            index = 0
            content_value = ''
            while write_content:
                if content[index] == '0':
                    write_content = False
                content_value += content[index + 1: index + 5]
                index += 5
            self.literal_value = convert_binary_to_decimal(content_value)
        else:
            self.id = content[0]
            content = content[1:]
            if self.id == '0':
                packet_length: int = convert_binary_to_decimal(content[:15])
                packets = content[15: 15 + packet_length]
                self.sub_packets = self.generate_sub_packets(packets)
            elif self.id == '1':
                nr_of_sub_packets: int = convert_binary_to_decimal(content[:11])
                packet_length = self.type_1_length(content[11:], nr_of_sub_packets)
                packets = content[11: 11 + packet_length]
                self.sub_packets = self.generate_sub_packets(packets)

    def type_1_length(self, packet_string: str, iterations: int):
        decoder = Decoder()
        string = packet_string
        packets_left = iterations
        total_packet_length = 0

        while True:
            if packets_left < 1:
                break
            packet_type = decoder.convert_binary_to_hex(string[3:6])
            # Generate literal sub packet
            if packet_type == '4':
                index = 6
                if len(string) < 6:
                    break
                while True:
                    if string[index] == '1':
                        index += 5
                    if string[index] == '0':
                        index += 5
                        string = string[index:]
                        total_packet_length += index
                        packets_left -= 1
                        break
            elif len(string) > 0:
                packet_id = string[6]
                string = string[7:]
                total_packet_length += 7
                if packet_id == '0':
                    packet_length: int = convert_binary_to_decimal(string[:15])
                    string = string[15 + packet_length:]
                    total_packet_length += 15 + packet_length
                    packets_left -= 1
                elif packet_id == '1':
                    nr_of_sub_packets: int = convert_binary_to_decimal(string[:11])
                    packet_length = self.type_1_length(string[11:], nr_of_sub_packets)
                    string = string[packet_length + 11:]
                    total_packet_length += packet_length + 11
                    packets_left -= 1
            else:
                break

        return total_packet_length

    def generate_sub_packets(self, packet_string: str):
        decoder = Decoder()
        string = packet_string
        sub_packets = []

        while True:
            packet_type = decoder.convert_binary_to_hex(string[3:6])
            # Generate literal sub packet
            if packet_type == '4':
                index = 6
                while True:
                    if string[index] == '1':
                        index += 5
                    if string[index] == '0':
                        index += 5
                        sub_packets.append(Packet(string[:index]))
                        string = string[index:]
                        break
            # Generate nested sub packets
            elif len(string) > 10:
                packet_id = string[6]
                # string = string[7:]
                if packet_id == '0':
                    packet_length: int = convert_binary_to_decimal(string[7:22])  # 15 + 7 = 22
                    packets = string[:22 + packet_length]
                    sub_packets.append(Packet(packets))
                    string = string[22 + packet_length:]
                elif packet_id == '1':
                    nr_of_sub_packets: int = convert_binary_to_decimal(string[7:18])  # 11 + 7 = 18
                    packet_length = self.type_1_length(string[18:], nr_of_sub_packets)
                    packets = string[:18 + packet_length]
                    sub_packets.append(Packet(packets))
                    string = string[18 + packet_length:]
            else:
                break
        return sub_packets

    def print_self(self, layer):
        layers = ''
        for _ in range(layer):
            layers += '\t'
        string = '\n' + layers + 'Version: ' + str(self.version) \
            + '\n' + layers + 'Type: ' + str(self.type)\
            + '\n' + layers + 'Literal: ' + str(self.literal_value)
        print(string)
        for packet in self.sub_packets:
            packet.print_self(layer + 1)


class Decoder:
    def __init__(self):
        self.hex_converter = {
            '0': '0000',
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'A': '1010',
            'B': '1011',
            'C': '1100',
            'D': '1101',
            'E': '1110',
            'F': '1111'
        }
        self.binary_converter = {
            '0000': '0',
            '0001': '1',
            '0010': '2',
            '0011': '3',
            '0100': '4',
            '0101': '5',
            '0110': '6',
            '0111': '7',
            '1000': '8',
            '1001': '9',
            '1010': 'A',
            '1011': 'B',
            '1100': 'C',
            '1101': 'D',
            '1110': 'E',
            '1111': 'F'
        }

    def convert_hex_to_binary(self, hex_string: str):
        string = ''
        for char in hex_string:
            string += self.hex_converter[char]
        return string

    def convert_binary_to_hex(self, bin_string: str):
        string = bin_string
        while len(string) < 4:
            string = '0' + string
        return self.binary_converter[string]


def part_1(raw_input):
    decoder = Decoder()

    data_binary = decoder.convert_hex_to_binary(raw_input[0])
    packet = Packet(data_binary)

    def get_versions(package: Packet):
        version = int(package.version)
        for pack in package.sub_packets:
            version += get_versions(pack)

        return version

    return get_versions(packet)


def part_2(raw_input):
    decoder = Decoder()

    data_binary = decoder.convert_hex_to_binary(raw_input[0])
    packet = Packet(data_binary)

    def get_value(pack: Packet) -> int:
        if pack.type == '0':
            val = 0
            for p in pack.sub_packets:
                val += get_value(p)
            return val
        if pack.type == '1':
            val = 1
            for p in pack.sub_packets:
                val *= get_value(p)
            return val
        if pack.type == '2':
            val = get_value(pack.sub_packets[0])
            for index in range(1, len(pack.sub_packets)):
                sub_val = get_value(pack.sub_packets[index])
                if val > sub_val:
                    val = sub_val
            return val
        if pack.type == '3':
            val = 0
            for p in pack.sub_packets:
                sub_val = get_value(p)
                if val < sub_val:
                    val = sub_val
            return val
        if pack.type == '4':
            return pack.literal_value
        if pack.type == '5':
            if get_value(pack.sub_packets[0]) > get_value(pack.sub_packets[1]):
                return 1
            else:
                return 0
        if pack.type == '6':
            if get_value(pack.sub_packets[0]) < get_value(pack.sub_packets[1]):
                return 1
            else:
                return 0
        if pack.type == '7':
            if get_value(pack.sub_packets[0]) == get_value(pack.sub_packets[1]):
                return 1
            else:
                return 0

    return get_value(packet)
