# Python signature editor

The present repo contains a Python script to process signature images, it returns a `png` image with transparent background containing only the signature.

## Setup

The Python PIL ([Python Image Library](http://pillow.readthedocs.io/en/latest/)) package with [Python 3](https://www.python.org/downloads/) is used in this repo.

To install PIL via pip:
```bash
pip install pillow
```

## Contents

The main script is [`signature.py`](https://github.com/RodolfoFerro/Signature/blob/master/scripts/signature.py), which contains a set of utility functions developed so far.

### Done so far

* Binarize your signature
* Remove background and make it transparent

### TODO

* Smooth image
* Image orientation
* Crop to get only signature

## Usage

The main script, [`signature.py`](https://github.com/RodolfoFerro/Signature/blob/master/scripts/signature.py) requires a set of parameters that are needed in the parser.

```bash
$ python signature.py -h
usage: signature.py [-h] -i INPUT [-o OUTPUT] [-th THRESHOLD]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input image.
  -o OUTPUT, --output OUTPUT
                        Output image.
  -th THRESHOLD, --threshold THRESHOLD
```

An example to use this script is as follows:

```bash
$ python signature.py -i imgs/example.jpg -o imgs/result.png -th 190
```

### Results

<img src="https://raw.githubusercontent.com/RodolfoFerro/Signature/master/imgs/RudolfoAnaya.jpg" width="50%"><img src="https://raw.githubusercontent.com/RodolfoFerro/Signature/master/imgs/resultado.png" width="50%">

***

#### Reference to:
<https://github.com/RodolfoFerro/Signature>
