from __future__ import print_function
import os
import string
import argparse

try:
    maketrans = string.maketrans  # python2
except AttributeError:
    maketrans = str.maketrans  # python3


def caeser_cipher(string_: str, offset: int, decode: bool, file_: string) -> None:
    """ Caeser Cipher implementation, reads file or string.  Also decodes.

    Default implementation is ROT13 encoding.

    To decode, specify the same offset you used to encode and your ciphertext / file.

    :param string_: string to encode / decode
    :param offset:  # of chars to rotate by
    :param decode:  decode instead of encode
    :param file_:   file to read in then encode/decode
    """
    if file_ and os.path.exists(file_):
        with open(file_, 'r') as f:
            string_ = f.read()

    if decode:
        offset *= -1

    lower_offset_alphabet = string.ascii_lowercase[offset:] + string.ascii_lowercase[:offset]
    lower_translation_table = maketrans(string.ascii_lowercase, lower_offset_alphabet)

    upper_offset_alphabet = string.ascii_uppercase[offset:] + string.ascii_uppercase[:offset]
    upper_translation_table = maketrans(string.ascii_uppercase, upper_offset_alphabet)

    lower_converted = string_.translate(lower_translation_table)
    final_converted = lower_converted.translate(upper_translation_table)

    if file_:
        extension = 'dec' if decode else 'enc'
        with open("{}.{}".format(file_, extension), 'w') as f:
            print(final_converted, file=f)
    else:
        print(final_converted)


def check_offset_range(value: int) -> int:
    """ Validates that value is in the allowable range.

    :param value:  integer to validate
    :return:  valid integer
    :raises: argparse.ArgumentTypeError
    """
    value = int(value)
    if value < -25 or value > 25:
        raise argparse.ArgumentTypeError("{} is an invalid offset".format(value))
    return value


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Simple Caeser Cipher [En,De]coder")

    parser.add_argument('-d', '--decode', action='store_true', dest='decode',
                        help='decode ciphertext (offset should equal what was used to encode)', default=False)
    parser.add_argument('-o', '--offset', dest='offset', default=13, type=check_offset_range,
                        help='number of characters to shift')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', dest='file', help='file to encode', default=None)
    group.add_argument('-s', '--string', dest='string', help='string to encode', default=None)

    args = parser.parse_args()

    caeser_cipher(args.string, args.offset, args.decode, args.file)
