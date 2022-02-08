# TTS - Text to Speech Mp3

Write spoken mp3 data to a file, a file-like object (bytestring) for further audio manipulation, or stdout.
This example uses the Python library [gTTS](https://pypi.org/project/gTTS/) (Google Text-to-Speech), to interface with Google Translate's text-to-speech API. 

## Installation

``$ pip install requirements.txt``

## Quickstart

```
>>> from gtts import gTTS
>>> tts = gTTS('hello')
>>> tts.save('hello.mp3')
```

## Disclaimer

[gTTS](https://pypi.org/project/gTTS/) project is not affiliated with Google or Google Cloud. Breaking upstream changes can occur without notice. This project is leveraging the undocumented Google Translate speech functionality and is different from Google Cloud Text-to-Speech.
