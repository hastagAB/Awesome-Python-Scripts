import os
borderstyle = "║"

def drawboxtext(dat):
    height = len(dat)
    y = 0
    while y < height:
        dat[y] = " "+dat[y]+" "
        y += 1
    width = len(max(dat, key=len))+1
    counter = 0
    x = 0
    line = "╔"
    while x < width-1:
        line = line + "═"
        x += 1
    line = line + "╗"
    print(line)
    while counter < height:
        reqspaces = width -1- len(dat[counter])
        xsp = ""
        while reqspaces > 0:
            xsp = xsp + " "
            reqspaces -= 1
        print(borderstyle+dat[counter]+xsp+borderstyle)
        counter += 1
    x = 0
    line = "╚"
    while x < width-1:
        line = line + "═"
        x += 1
    line = line + "╝"
    print(line)


print("Framed text generator by Julian Drake.\n")
print("")
while True:
    print("Enter the items in the frame. (Leave blank to submit.)")

    items=[]
    i=0
    while 1:
        i+=1
        item=input('Enter item %d: '%i)
        if item=="":
                break
        items.append(item)

    print("")
    drawboxtext(items)
    print("")
    input("")
    os.system('cls')

