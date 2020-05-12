import argparse


def fun_a():
    print('fun_a()')


def fun_b(arg):
    print('fun_b({})'.format(arg))


def fun_c(arg_a, arg_b):
    print('fun_c({0}, {1})'.format(arg_a, arg_b))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Private Agreement Recognizer\n'
                    '  Help you analyze the network packets\' type of agreement.\n'
                    '----- Copyright (C) Hyperzsb 2020 -----',
        epilog='\n\nContact us @ hyperzsb@outlook.com\n\n')
    parser.formatter_class = argparse.RawDescriptionHelpFormatter
    parser.add_argument('-v', '--version', action='version', version='Private Agreement Recognizer v1.0')
    parser.add_argument('-I', '--interact', action='store_const', const=True,
                        help='operate in interactive mode')
    parser.add_argument('-i', '--input', metavar='input_file', type=str, nargs='+',
                        help='*.pcap file(s) to analyze')
    parser.add_argument('-o', '--output', metavar='output_file', type=str, nargs=1,
                        help='file to store the analyzing result')
    args = parser.parse_args()
    print(args.__getattribute__('interact'))
