from gtts import gTTS

def main():
  tts = gTTS('hello')
  tts.save('hello.mp3')

if __name__ == "__main__":
  main()
