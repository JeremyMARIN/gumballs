#!/usr/bin/env python
# -*- coding: utf-8 -*-

# deal a bunch cards

import random

deck = [0] * 52 # create a shuffled deck 52 places long
                # 0 == card not been used (yet)

def get_rank():
	# create a rank 0 - 12
	the_rank = random.randint(0, 12)
	return the_rank

def get_suit(): # couleur (coeur, trêfle, carreau, pique)
	# create a suit 0 - 3
	return random.randint(0, 3)

def print_rank(the_rank):
	if the_rank == 0:
		print("Ace ", end="")
	elif the_rank == 1:
		print("Jack ", end="") # valet
	elif the_rank == 11:
		print("Queen ", end="")
	elif the_rank == 12:
		print("King ", end="")
	else:
		print(the_rank, end=" ")

def print_suit(the_suit):
	if the_suit == 0:
		print("of Hearts") # coeur
	elif the_suit == 1:
		print("of Clubs") # trêfle
	elif the_suit == 2:
		print("of Diamonds") # carreau
	else:
		print("of Spades") # piques

def print_unique_card(cards_left):
	# this first code "reshuffles" the deck after 52 cards!
	if cards_left == 0:
		for i in range(52):
			deck[i] = 0 # make all cards available again
			cards_left = 52
		print("*******************")

	possible_rank = get_rank()
	possible_suit = get_suit()

	possible_card = possible_suit * 13 + possible_rank # unique num 0 - 51

	while (deck[possible_card] > 0): # if true, card has been used - try another
		possible_rank = get_rank()
		possible_suit = get_suit()
		possible_card = possible_suit * 13 + possible_rank

	# wow found a card that's never used! So, check it off so it can't be used again
	print(possible_card, end="\t")
	deck[possible_card] = 1
	cards_left = cards_left - 1

	# and print out the unique card

	print_rank(possible_rank)
	print_suit(possible_suit)

	return cards_left


def main():
	cards_left = 52
	for cards in range(53):
		cards_left = print_unique_card(cards_left)

main()