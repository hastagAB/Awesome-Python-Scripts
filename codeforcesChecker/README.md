# codeforcesChecker
CodeforcesChecker is a useful tool for Competitive Programmers using the Codeforces website. <br>
The main motive of this project is to help users save time while solving the problems and reduce the hassels of checking validity of their sample outputs with the expected sample outputs.

Before using the script some dependencies need to be installed<br>
		1. You need to have python3 installed on your system<br>
		2. You need to have various modules installed viz. selenium, chromedriver_binary, beautifulSoup4, requests, shutil, filecmp, sys, termcolor, coloroma, os and any other dependencies absent on your system.

You can install these using pip3(Example: pip3 install chromedriver_binary )<br>
 <b>To install all the dependencies you can simply type this command in your terminal: pip3 install -r requirements.txt</b>

Procedure to use the script: <br>

1. The first thing you need to do is to copy-paste or write your C++ template to the template.cpp file. (I have provided a sample template)<br>
2. After the template, you should run the main.py file by typing <b>python3 main.py</b> onto your terminal.<br>
3. Then you need to enter the URL of the site.<br>
  Now URL's can be of two type<br>
			3.1. If you need to clone the entire contest, may it be live or virtual or just upsolving.<br>
      3.2. You only need a problem from the problemset.<br>
4. After the exection of main.py file a folder will be created either of the contest or the problem you wish to solve.Each problem of the contest will have a specific folder having the soln.cpp file(containing the template), the checker.py file and all the sample input and output files.<br>
5. You now need to change your current working directory to the Problem folder using <b>cd</b> command. After this you need to write your solution in the <b>soln.cpp</b> file, save it and then close it.<br>
6. Type <b>python3 checker.py</b> on your terminal and press Enter key. This script will check your code against sample inputs and sample outputs and give "VERDICT OK", if all the test cases pass or "VERDICT NOT OK", if either some or all testcases fail. For the testcases which fail, you will also get your output along with the expected output on the terminal screen. <br>
7. The similar process can be followed for all the problems.
