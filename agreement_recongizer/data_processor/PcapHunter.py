from scapy.all import *


class PcapHunter:
    """
    Pcap sniffer and processor
    """

    # Max packets number to sniff
    __count: int = 0
    # Longest time to sniff
    __timeout: int = None
    # Sniffed packets
    __packets: array = []

    def __init__(self, count: int = 0, timeout: int = None):
        """
        :param count: max packets number to sniff
        :param timeout: longest time to sniff
        """
        self.__count = count
        self.__timeout = timeout

    def hunt(self, count: int = -1, timeout: int = -1) -> array:
        """
        :param count: override the max packets number to sniff
        :param timeout: override the longest time to sniff
        :return: sniffed packets

        Sniff net packets on all interfaces
        """
        if count == -1:
            count = self.__count
        if timeout == -1:
            timeout = self.__timeout
        print('Started hunting... (args: count={0}, timeout={1})'.format(count, timeout))
        self.__packets = sniff(count=count, timeout=timeout)
        print('Finished hunting.')
        return self.__packets

    def packets(self) -> array:
        """
        :return: sniffed packets

        Return sniffed packets during last hunting
        """
        if len(self.__packets) == 0:
            print('Never hunted. Please call hunt() method first.')
            return None
        else:
            return self.__packets

    def to_pcap(self, output_file: str):
        """
        :param output_file: <output_file>(*.pcap) file path

        Convert hunting result to *.pcap file
        """
        print('Started saving packets to pcap file: {0}...'.format(output_file))
        wrpcap(output_file, self.__packets)
        print('Finished saving')
