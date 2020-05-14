from malwareAnalysis.utils import PcapPreProcessor


def preprocessData(dataFrom ,dataTo):

    pcapPreProcessor = PcapPreProcessor(input_file=dataFrom)
    pcapPreProcessor.to_csv_in_image(dataTo)

