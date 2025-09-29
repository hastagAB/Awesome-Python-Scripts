import base64
from argparse import ArgumentParser, BooleanOptionalAction


def decode(encoded: str) -> str:
    return base64.b64decode(encoded).decode()


def encode(text: str) -> str:
    return base64.b64encode(text.encode()).decode()


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="Base64",
        description="Base64 encode adn decode string",
    )
    parser.add_argument("-d", "--decode", action=BooleanOptionalAction, default=False, type=bool, help="Decode text")
    parser.add_argument("text", type=str, help="The text to decode or encode")
    args = parser.parse_args()
    if args.decode:
        print(decode(args.text))
    else:
        print(encode(args.text))
