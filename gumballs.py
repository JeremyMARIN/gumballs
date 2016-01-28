#!/usr/bin/env python
# -*- coding: utf-8 -*-

# simulate buying gumballs

# inspired by python_deck 
# http://cs.nyu.edu/courses/spring16/CSCI-UA.0061-001/assign1_examples/python_deck.txt

import random

DEBUG = False
gumballs = []
bought_list = []

gumballs_by_color = [
	[10, 15],
	[1, 10],
	[6, 15],
	[10, 25],
	[1, 12],
	[5, 10],
	[4, 6],
	[5, 12],
	[0, 10],
	[1, 1]
]

def get_color(i):
	if i == 0:
		return "Yellow"
	elif i == 1:
		return "Blue"
	elif i == 2:
		return "White"
	elif i == 3:
		return "Green"
	elif i == 4:
		return "Black"
	elif i == 5:
		return "Purple"
	elif i == 6:
		return "Silver"
	elif i == 7:
		return "Cyan"
	elif i == 8:
		return "Magenta"
	elif i == 9:
		return "Red"
	else:
		return "UNDEFINED"


def init_gumballs_machine():
	gumballs = []
	for i in range(len(gumballs_by_color)):
		n = random.randint(gumballs_by_color[i][0], gumballs_by_color[i][1])

		if DEBUG:
			print("[d] %d: (%d, %d)\t=> %d" % (i, gumballs_by_color[i][0], gumballs_by_color[i][1], n))

		print("%d\t%s" % (n, get_color(i)))

		for j in range(n): # add n gumballs of color i
			gumballs = gumballs + [i]

	if DEBUG:
		print("[d] There are %d gumballs in all" % len(gumballs))

	return gumballs


def buy_gumball(gumballs):
	# pick a random gumball
	b = random.randint(0, len(gumballs) - 1)

	if DEBUG:
		print("[d] Try gumball number %d..." % b)

	while (gumballs[b] >= 99):
		# try another gumball until we find a unused one
		b = random.randint(0, len(gumballs) - 1)
		if DEBUG:
			print("[d] Try gumball number %d..." % b)

	# found a gumball that's never used!
	# print the color and check it off so it cannot be used again
	color = gumballs[b]

	if DEBUG:
		print("[d] b=%d is a %s gumball" % (b, get_color(color)))

	print("%s" % get_color(color))
	gumballs[b] = 99

	return color


def get_max_bought_gumballs(bought_list):
	counted_gumballs = []
	for i in range(len(gumballs_by_color)):
		counted_by_color = 0
		for j in range(len(bought_list)):
			if bought_list[j] == i:
				counted_by_color = counted_by_color + 1
		counted_gumballs = counted_gumballs + [counted_by_color]

		if DEBUG:
			print("[d] There are %d of %s color" % (counted_by_color, get_color(i)))

	# find the maximum(s)
	maximum = max(counted_gumballs)

	if DEBUG:
		print("The maximum by color is %d" % maximum)

	max_colors = [i for i, j in enumerate(counted_gumballs) if j == maximum]

	return max_colors


def main():
	# initialization
	print("[*] Welcome to the CIMS Gumball Machine Simulator")
	print("[*] You are stating with the following Gumballs:")
	gumballs = init_gumballs_machine()
	if DEBUG:
		print(gumballs)

	# buy gumballs
	bought_list = []
	print("[*] Here are your random purchases:")
	bought_gumball = buy_gumball(gumballs)
	bought_list = bought_list + [bought_gumball]
	while (bought_gumball != 9):
		bought_gumball = buy_gumball(gumballs)
		bought_list = bought_list + [bought_gumball]

	print("You purchased %d Gumballs, for a total of $%0.2f." % (len(bought_list), len(bought_list) * 0.5))
	if DEBUG:
		print(bought_list)

	# print out which color(s) have been bought the most 
	max_colors = get_max_bought_gumballs(bought_list)

	print("The color(s) purchased most:", end="")
	for i, j in enumerate(max_colors):
		print(" %s" % get_color(j), end="")
	print("")


main()