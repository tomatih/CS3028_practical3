#!/usr/bin/env python

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a second number: "))

def do_action_on_numbers(a,b,action_name,action):
	print(f"The {action_name} is: {action(a,b)}")

actions = {
	"sum": lambda x,y : x+y,
	"difference": lambda x,y: x-y,
	"product": lambda x,y: x*y,
    "quotient": lambda x,y: x/y
}

for action in actions:
	do_action_on_numbers(num1,num2,action,actions[action])
