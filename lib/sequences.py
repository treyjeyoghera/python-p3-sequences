#!/usr/bin/env python3

# With range:

def print_fibonacci(length):

	new= []
	if length > 0:
		new.append(0)
	if length >= 2:
		new.append(1)
		for i in range(2, length):
			new.append(new[-1] + new[-2])

	print(new)
