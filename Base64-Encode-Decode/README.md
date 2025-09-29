# Base64 Encode And Decode
## Usage
``` bash
usage: Base64 [-h] [-d | --decode | --no-decode] text

Base64 encode adn decode string

positional arguments:
  text                  The text to decode or encode

options:
  -h, --help            show this help message and exit
  -d, --decode, --no-decode
                        Decode text (default: False)
```

## Example
### Encode
```
python3 base64_encode_decode.py "abcxyz 123"
```
Result:
```
YWJjeHl6IDEyMw==
```

### Decode: 
```
python3 base64_encode_decode.py -d YWJjeHl6IDEyMw==
```
Result: 
```
abcxyz 123
```
