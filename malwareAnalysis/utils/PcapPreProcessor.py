from malwareAnalysis.utils.ProtocalDictionary import ProtocolDictionary
from typing import Type
from scapy.all import *
import pandas as pd


class PcapStatistic:
    """
    Data class to contain packets statistic info
    """

    # All packets number
    all = 0
    # All packets' protocols
    all_protocol = []
    # All TCP packets number
    tcp = 0
    # All TCP packets' protocols
    tcp_protocol = []
    # All UDP packets number
    udp = 0
    # All UDP packets' protocols
    udp_protocol = []
    # All Other(neither TCP nor UDT) packets number
    other = 0
    # All Other(neither TCP nor UDT) packets' protocols
    other_protocol = []


class PcapPreProcessor:
    """
    Preprocessor for *.pcap files
    """

    # Input *.pcap file path
    __input_file = None
    # Input *.csv label file path
    __label_file = None
    # Data range to load
    __range = None
    # Packets array
    __packets = []
    # Corresponding label to packets array
    __label = []
    # TCP packets array
    __tcp_packets = []
    # Corresponding label to TCP packets array
    __tcp_label = []
    # UDP packets array
    __udp_packets = []
    # Corresponding label to UDP packets array
    __udp_label = []
    # Other(neither TCP nor UDT) packets array
    __other_packets = []
    # Corresponding label to Other(neither TCP nor UDT) packets array
    __other_label = []
    # Statistic info of packets
    __statistic = None

    def __init__(self, input_file, data_range=None, label_file=None):
        """
        :param input_file: input *.pcap file path
        :param data_range: range for rows to load in
        :param label_file: corresponding label file(*.csv file with a 'Protocol' column) for input *.pcap file
        """

        # Load packets from <input_file>
        self.__input_file = input_file
        self.__range = data_range
        packets = rdpcap(input_file)
        if data_range is not None:
            self.__packets = packets[data_range]
        else:
            self.__packets = packets

        # Load label from <label_file>
        if label_file is not None:
            if data_range is not None:
                self.__label = pd.read_csv(label_file)['Protocol'][data_range].tolist()
            else:
                self.__label = pd.read_csv(label_file)['Protocol'].tolist()
            # Check <input_file> is as long as <label_file> or not
            if len(self.__packets) != len(self.__label):
                raise Exception('<input_file\'{0}\'> is not corresponding to <label_file\'{1}\'>: '
                                'Length of two file is not the same, please check it.\n'.format(input_file, label_file))

        # Group pcap by TCP/UDP/Other and do statistic
        self.__statistic = PcapStatistic
        length = len(self.__packets)
        for i in range(length):
            if self.__packets[i].haslayer('TCP'):
                self.__statistic.tcp += 1
                self.__tcp_packets.append(self.__packets[i])
                if label_file is not None:
                    self.__tcp_label.append(self.__label[i])
                    if self.__label[i] not in self.__statistic.tcp_protocol:
                        self.__statistic.tcp_protocol.append(self.__label[i])
                        self.__statistic.all_protocol.append(self.__label[i])
            elif self.__packets[i].haslayer('UDP'):
                self.__statistic.udp += 1
                self.__udp_packets.append(self.__packets[i])
                if label_file is not None:
                    self.__udp_label.append(self.__label[i])
                    if self.__label[i] not in self.__statistic.udp_protocol:
                        self.__statistic.udp_protocol.append(self.__label[i])
                        self.__statistic.all_protocol.append(self.__label[i])
            else:
                self.__statistic.other += 1
                self.__other_packets.append(self.__packets[i])
                if label_file is not None:
                    self.__other_label.append(self.__label[i])
                    if self.__label[i] not in self.__statistic.other_protocol:
                        self.__statistic.other_protocol.append(self.__label[i])
                        self.__statistic.all_protocol.append(self.__label[i])
        self.__statistic.all = self.__statistic.tcp + self.__statistic.udp + self.__statistic.other

    def all(self) -> array:
        """
        :return: packets array
        Return all packets
        """
        return self.__packets

    def tcp(self) -> array:
        """
        :return: packets array
        Return TCP packets
        """
        return self.__tcp_packets

    def udp(self) -> array:
        """
        :return: packets array
        Return UDP packets
        """
        return self.__udp_packets

    def other(self) -> array:
        """
        :return: packets array
        Return Other packets
        """
        return self.__other_packets

    def statistic(self) -> Type[PcapStatistic]:
        """
        :return: PcapStatistic
        Return statistic info of the *.pcap file
        """
        return self.__statistic

    def label(self) -> array:
        """
        :return: label
        Return label('Protocol') array for packets if <label_file> is specified
        """
        return self.__label

    def to_csv_in_image(self, output_file: str, pixel: int = 28, mode: str = 'all', label: bool = False,
                        column_name: bool = True):
        """
        :param output_file: output *.csv file path
        :param pixel: every packet will be formatted into a pixel*pixel image by first pixel*pixel bytes in dec value
        :param mode: 'all' - select all packets;
                     'tcp' - select tcp packets;
                     'udp' - select udp packets;
                     'other' - select other packets
        :param label: if true, add label for every packets if <label_file> is specified
        :param column_name: if true add name for every column in *.csv file
        Convert *.pcap file to *.csv file in image format
        """

        # print('Started converting pcap packets to CSV file in image({0}*{0})...'.format(pixel))
        # Define <image_size>(data vector dimension)
        image_size = pixel * pixel
        # Select packets(and label if <label_file> is specified) to do converting
        selected_packets = None
        selected_label = None
        packets_size = 0
        if mode == 'all':
            selected_packets = self.__packets
            selected_label = self.__label
            packets_size = self.__statistic.all
        elif mode == 'tcp':
            selected_packets = self.__tcp_packets
            selected_label = self.__tcp_label
            packets_size = self.__statistic.tcp
        elif mode == 'udp':
            selected_packets = self.__udp_packets
            selected_label = self.__udp_label
            packets_size = self.__statistic.udp
        elif mode == 'other':
            selected_packets = self.__other_packets
            selected_label = self.__other_label
            packets_size = self.__statistic.other

        # print('Preprocessing...')
        # Convert raw pcap packet into dec data vector
        csv_arr = []
        progress = 0.2
        for i in range(packets_size):
            if (i / packets_size) > progress:
                # print('Preprocessed: {}%'.format(int(progress * 100)))
                progress += 0.2
            # Divide the packet by every two hex bit(two hex bit = one byte)
            hex_arr = linehexdump(selected_packets[i], onlyhex=1, dump=True).split(' ')
            # Cast hex number to dec number
            dec_arr = []
            for j in range(len(hex_arr)):
                dec_arr.append(int(hex_arr[j], 16))
            # Pad the vector if length is shorter than <image_size>(data vector dimension)
            if len(dec_arr) < image_size:
                while len(dec_arr) < image_size:
                    dec_arr.append(0)
            # Cut the vector if length is longer than <image_size>(data vector dimension)
            elif len(dec_arr) > image_size:
                dec_arr = dec_arr[0:image_size]
            csv_arr.append(dec_arr)
        # print('Preprocessed: {}%'.format(int(progress * 100)))

        # print('Converting...')
        # Add every column
        csv = pd.DataFrame()
        for i in range(image_size):
            column = [x[i] for x in csv_arr]
            if column_name:
                csv['pixel' + str(i)] = column

        # Add label column
        if label & (selected_label is not None):
            dictionary = ProtocolDictionary
            for i in range(packets_size):
                if dictionary.dict.get(selected_label[i]) is not None:
                    selected_label[i] = dictionary.dict.get(selected_label[i])
                else:
                    selected_label[i] = dictionary.dict.get('UNKNOWN')
            csv['label'] = selected_label

        # Save dec data vector to CSV file
        csv.to_csv(output_file, index=False)
        # print('Finished converting. Output file is \'{}\'.'.format(output_file))