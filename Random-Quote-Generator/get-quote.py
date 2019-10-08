import random
def primary():
  
  
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 15
  rnd1 = random.randint(0, last)
  rnd2 = random.randint(0, last)

  print(quotes[rnd1],quotes[rnd2])

if __name__== "__main__":
  primary()
