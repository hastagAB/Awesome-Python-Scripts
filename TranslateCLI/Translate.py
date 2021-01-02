#!/usr/bin/env python3

import argparse
from googletrans import Translator

def translate(text, src_lng=None, dest_lng=None):
    translator = Translator()
    if src_lng and dest_lng:
        translated = translator.translate(text, src=src_lng, dest=dest_lng)
    elif src_lng:
        translated = translator.translate(text, src=src_lng)
    elif dest_lng:
        translated = translator.translate(text, dest=dest_lng)
    else:
        translated =  translator.translate(text)

    return translated

parser = argparse.ArgumentParser()
parser.add_argument('text', type=str, help='text to translate')
parser.add_argument('-s', '--src', default=None, help='origin language of the text')
parser.add_argument('-d', '--dest', default=None, help='destiny language of the translation')
parser.add_argument('-v', '--verbose', help='show more information', action='store_true')

args = parser.parse_args()

tr = translate(args.text, args.src, args.dest)

if args.verbose:
    print('original text: %s' % tr.origin)
    print('translated text: %s' % tr.text)
    print('origin language: %s' % tr.src)
    print('destiny language: %s' % tr.dest)
else:
    print(tr.text)
