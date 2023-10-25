import random
print("wassup hommie, care to play a game?")
print("i'll try to guess the number YOU choose.")
print("please tell me the borders: ")

a = int(input("Min: "))
b = int(input("Max: "))
while True:
 if(a > b):
    (print("error, min can't be more than max. "))
    a = int(input("Min: "))
    b = int(input("Max: "))
 else:
     break;
breaking = "------------"
print("now type in the number: ")
c = int(input(" "))
tries = 1;
d = random.randint(a, b)
while True:
   if(d == c and tries == 1):
            print("guess 1: " + str(d))
            print("HA, gotcha. I got it in 1 time!")
            print("Wanna go again? y for yes and anykey for no. ")
            i = input("");
            if(i == "y"):
               print(breaking * 10);
               a = int(input("Min: "))
               b = int(input("Max: "))

               print("now type in the number")
               c = int(input(" "))
               tries = 1;
               if(a > b):
                      print("error, min can't be more than max. ")
                      a = int(input("Min: "))
                      b = int(input("Max: "))
                      print("now type in the number")
                      c = int(input(" "))
               else:
                d = random.randint(a, b)
               
            else:
              break;
   elif(d == c):
            print("HA, gotcha. I got it in " + str(tries - 1) + " times!")
            print("Wanna go again? y for yes and anykey for no. ")
            i = input("");
            if(i == "y"):
              print(breaking * 10);
              a = int(input("Min: "))
              b = int(input("Max: "))

              print("now type in the number")
              c = int(input(" "))
              tries = 1;
              if(a > b):
                      print("error, min can't be more than max. ")
                      a = int(input("Min: "))
                      b = int(input("Max: "))
                      print("now type in the number")
                      c = int(input(" "))
              else:
                d = random.randint(a, b)
          
            else:
              break;
    
   elif(c > b):
      print("error, number can't be bigger than max.");
      print("Wanna go again? y for yes and anykey for no. ")
      i = input("");
      if(i == "y"):
          print(breaking * 10);
          a = int(input("Min: "))
          b = int(input("Max: "))

          print("now type in the number")
          c = int(input(" "))
          tries = 1;
          if(a > b):
                (print("error, min can't be more than max. "))
                a = int(input("Min: "))
                b = int(input("Max: "))
                print("now type in the number")
                c = int(input(" "))
          else:
             d = random.randint(a, b)

      else:
          break;
   elif(c < a):
      print("error, number can't be smaller than min.");
      print("Wanna go again? y for yes and anykey for no. ")
      i = input("");
      if(i == "y"):
          print(breaking * 10);
          a = int(input("Min: "))
          b = int(input("Max: "))

          print("now type in the number")
          c = int(input(" "))
          tries = 1;
          if(a > b):
                      print("error, min can't be more than max. ")
                      a = int(input("Min: "))
                      b = int(input("Max: "))
                      print("now type in the number")
                      c = int(input(" "))
          else:
            d = random.randint(a, b)
      else:
            break;
   elif(d < c):
          a = d + 1;
          d = random.randint(a, b)
          print( "guess " + str(tries) + " :" + str(d));
          tries += 1;

   elif(d > c):
      b = d - 1;
      d = random.randint(a, b)
      print( "guess " + str(tries) + " :" + str(d))  
      tries += 1

input=""

