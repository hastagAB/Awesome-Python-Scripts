import numpy as np, matplotlib.pyplot as plt

def main():
    filename = input('Type name of the file with data to plot: ')
    f = open(filename)
    lines = f.readlines()
    f.close()

    imagetitle = input('Define the title of your graphic: ')
    horizontallabel = input('What label on the x axis? ')
    verticallabel = input('What label on the y axis? ')
    my_color = input('Set color of the line: ')
    my_grid = bool(input('You want grid in your graphic? [True/False] '))

    
    x = []; y = []
    for line in lines:
        splitted = line.split(',')
        x.append(int(splitted[0]))
        y.append(int(splitted[1]))

    print(f'xdata = {x}')
    print(f'ydata = {y}')
    print(f'Generating plot image...')
    fig = plt.figure()
    sp = fig.add_subplot(111)
    sp.plot(x, y, color=my_color, marker='o', )
    sp.set_title(imagetitle)
    sp.set_xlabel(horizontallabel)
    sp.set_ylabel(verticallabel)
    sp.grid(my_grid)
    fig.savefig('MyEasyGraphic.png')
    return


# Call main method
if __name__ == '__main__':
    main()