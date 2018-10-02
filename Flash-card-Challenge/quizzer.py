import random
import argparse

parser = argparse.ArgumentParser(description="Get the quiz questions file")
parser.add_argument('file', help="a quiz file containing questions and answers")
args = parser.parse_args()
file = args.file

state_capitals = {}
with open(file) as f:
	for line in f:
		(key, val) = line.strip().split(',')
		state_capitals[key] = val
		
while(True):
	choice = random.choice(list(state_capitals.keys()))
	answer = input(('{}? '.format(choice)))
	if answer == state_capitals[choice]:
		print("Correct! Nice job.")
	elif answer.lower() == "exit":
		print("Goodbye")
		break
	else:
		print("Incorrect. The correct answer is {}".format(state_capitals[choice]))