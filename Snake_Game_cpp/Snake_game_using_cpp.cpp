// This is a CLI snake game made in cpp which makes it very fast.

// ! This game will only run in windows.
// As I have used the windows.h and conio.h which through which I have used some functions which only work in windows.
// * You can change the value of sleep() function A/c to your system specification for making the refresh rate of the CLI slow or fast.

#include <iostream>
#include <conio.h>   // for _kbhit() and _getch() functions
#include <windows.h> // for Sleep() function
using namespace std;
int what;
bool gameover;
const int width = 50;
const int height = 20;
int x_axis, y_axis, fruitX_axis, fruitY_axis, score;
int tailX_axis[100], tailY[100];
int nTail;
enum Direction
{
    STOP = 0,
    LEFT,
    RIGHT,
    UP,
    DOWN
}; // enum is here it is used for direction of snake, by default it is STOP
Direction dir;

void Setup()
{
    cout<<"Welcome to the SNAKE-GAME"<<endl;
    cout<<"Use W-A-S-D for moving the snake"<<endl;
    cout << "What type of game do you want to play?" << endl
         << "Press 1 for Infinite game (you will never die)" << endl
         << "Press 0 for The REAL snake-game (game-over if you touched the wall)" << endl;
    cin >> what;
    gameover = false;
    dir = STOP;
    x_axis = width / 2;
    y_axis = height / 2;
    fruitX_axis = rand() % width;
    fruitY_axis = rand() % height;
    score = 0;
    nTail = 0;
}

void Draw()
{
    system("cls"); // for windows using system("cls"); for linux use system("clear");

    for (int i = 0; i < width + 2; i++)
    {
        cout << "#";
    }
    cout << endl;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (j == 0)
            {
                cout << "#"; // wall
            }
            if (i == y_axis && j == x_axis)
            {
                cout << "O"; // head of snake in center of screen
            }
            else if (i == fruitY_axis && j == fruitX_axis)
            {
                cout << "F"; // fruit at random
            }
            else
            {
                bool print = false;
                for (int k = 0; k < nTail; k++)
                {
                    if (tailX_axis[k] == j && tailY[k] == i)
                    {
                        cout << "o";
                        print = true;
                    }
                }
                if (!print)
                {
                    cout << " ";
                }
            }
            if (j == width - 1)
            {
                cout << "#";
            }
        }
        cout << endl;
    }
    for (int i = 0; i < width + 2; i++)
    {
        cout << "#";
    }
    cout << endl;
    cout << "Score: " << score << endl;
}

void Input()
{
    if (_kbhit())
    { // returns 1 if key is pressed else 0

        switch (_getch())
        { // return the key pressed ASCII value

        case 'a':
            dir = LEFT;
            break;
        case 'd':
            dir = RIGHT;
            break;
        case 'w':
            dir = UP;
            break;
        case 's':
            dir = DOWN;
            break;
        case 'x':
            gameover = true;
            break;
        }
    }
}

void Logic()
{
    int prevX_axis = tailX_axis[0];
    int prevY = tailY[0];
    int prev2X_axis, prev2Y;
    tailX_axis[0] = x_axis;
    tailY[0] = y_axis;
    for (int i = 1; i < nTail; i++)
    {
        prev2X_axis = tailX_axis[i];
        prev2Y = tailY[i];
        tailX_axis[i] = prevX_axis;
        tailY[i] = prevY;
        prevX_axis = prev2X_axis;
        prevY = prev2Y;
    }
    switch (dir)
    {
    case LEFT:
        x_axis--;
        break;
    case RIGHT:
        x_axis++;
        break;
    case UP:
        y_axis--;
        break;
    case DOWN:
        y_axis++;
        break;
    }
    if (what == 1)
    {
        if (x_axis >= width)
            x_axis = 0;
        else if (x_axis < 0)
            x_axis = width - 1;
        if (y_axis >= height)
            y_axis = 0;
        else if (y_axis < 0)
            y_axis = height - 1;
    }
    else if (what == 0)
    {
        if (x_axis > width || x_axis < 0 || y_axis > height || y_axis < 0)
        {
            gameover = true;
            // Tail touch= game-over
            for (int i = 0; i < nTail; i++)
            {
                if (tailX_axis[i] == x_axis && tailY[i] == y_axis)
                {
                    gameover = true;
                }
            }
        }
    }

    if (x_axis == fruitX_axis && y_axis == fruitY_axis)
    {
        score += 10;
        fruitX_axis = rand() % width;
        fruitY_axis = rand() % height;
        nTail++;
    }
}

int main()
{
    Setup();
    while (!gameover)
    {
        Draw();
        Input();
        Logic();
        Sleep(50);
    }

    return 0;
}
