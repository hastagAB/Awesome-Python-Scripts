#!/usr/bin/env python3
import csv
import sys
from typing import Iterable, List


def main():
    content_lines = sys.stdin.buffer.readlines()
    reader = csv.reader(line.decode('utf-8') for line in content_lines)
    headers = next(reader)
    print(create_table(reader, headers))


def create_table(rows: Iterable[List[str]], headers: List[str]) -> str:
    table = [headers]
    column_lengths = [len(header) for header in headers]
    for row in rows:
        for i, text in enumerate(row):
            column_length = column_lengths[i]
            text_length = len(text)
            if text_length > column_length:
                column_lengths[i] = text_length
        table.append(list(row))

    result = []
    for row in table:
        row_text = []
        for i, text in enumerate(row):
            column_length = column_lengths[i]
            row_text.append(space_pad(text, column_length))
        result.append('    '.join(row_text))
    return '\n'.join(result)


def space_pad(text: str, length: int) -> str:
    temp = text + ''.join(' ' for _ in range(length))
    return temp[:length]


if __name__ == '__main__':
    main()
