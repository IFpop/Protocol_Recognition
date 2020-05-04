from agreement_recongizer.data_processor import PcapPreprocessor

if __name__ == '__main__':
    preprocessor = PcapPreprocessor(input_file='pcap/20200502.pcap', data_range=slice(0, 1000),
                                    label_file='pcap/20200502.csv')
    statistic = preprocessor.statistic()
    print(statistic.tcp_protocol)
    print(statistic.udp_protocol)
    print(statistic.other_protocol)
    preprocessor.to_csv_in_image('data/20200502-label.csv', label=True)
