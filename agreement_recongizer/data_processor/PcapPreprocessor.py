from typing import Type

from scapy.all import *
import pandas as pd


class PcapStatistic:
    all = 0
    tcp = 0
    udp = 0
    other = 0


class PcapPreprocessor:
    __input_file = None
    __range = None
    __packets = []
    __tcp_packets = []
    __udp_packets = []
    __other_packets = []
    __statistic = None

    def __init__(self, input_file, data_range=None):
        """
        :param input_file: input *.pcap file path
        :param data_range: range for rows to load in

        Preprocessor for *.pcap files
        """

        # Load packets from input_file
        self.__input_file = input_file
        self.__range = data_range
        packets = rdpcap(input_file)
        if data_range is not None:
            self.__packets = packets[data_range]
        else:
            self.__packets = packets
        # Group pcap by TCP/UDP/Other and do statistic
        self.__statistic = PcapStatistic
        for unknown_packet in self.__packets:
            if unknown_packet.getlayer('TCP') is not None:
                self.__statistic.tcp += 1
                self.__tcp_packets.append(unknown_packet)
            elif unknown_packet.getlayer('UDP') is not None:
                self.__statistic.udp += 1
                self.__udp_packets.append(unknown_packet)
            else:
                self.__statistic.other += 1
                self.__other_packets.append(unknown_packet)
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

    def to_csv_in_image(self, output_file: str, pixel: int = 28, mode: str = 'all'):
        """
        :param output_file: output *.csv file path
        :param pixel: every packet will be formatted into a pixel*pixel image by first pixel*pixel bytes in dec value
        :param mode: 'all' - select all packets;
                     'tcp' - select tcp packets;
                     'udp' - select udp packets;
                     'other' - select other packets

        Convert *.pcap file to *.csv file in image format
        """
        image_size = pixel * pixel
        print('Started converting pcap packets to CSV file in image({0}*{0})...'.format(pixel))
        selected_packets = None
        packets_size = 0
        if mode == 'all':
            selected_packets = self.__packets
            packets_size = self.__statistic.all
        elif mode == 'tcp':
            selected_packets = self.__tcp_packets
            packets_size = self.__statistic.tcp
        elif mode == 'udp':
            selected_packets = self.__udp_packets
            packets_size = self.__statistic.udp
        elif mode == 'other':
            selected_packets = self.__other_packets
            packets_size = self.__statistic.other

        csv_arr = []
        for i in range(packets_size):
            hex_arr = linehexdump(selected_packets[i], onlyhex=1, dump=True).split(' ')
            dec_arr = []
            for j in range(len(hex_arr)):
                dec_arr.append(int(hex_arr[j], 16))
            if len(dec_arr) < image_size:
                while len(dec_arr) < image_size:
                    dec_arr.append(0)
            elif len(dec_arr) > image_size:
                dec_arr = dec_arr[0:image_size]
            csv_arr.append(dec_arr)
        csv = pd.DataFrame()
        for i in range(image_size):
            column = [x[i] for x in csv_arr]
            csv['pixel' + str(i)] = column
        csv.to_csv(output_file, index=False)
        print('Finished converting. Output file is \'{}\'.'.format(output_file))
