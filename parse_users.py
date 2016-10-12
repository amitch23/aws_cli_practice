#!/usr/bin/env python
import sys

def get_list_of_users(users):
	usernames = []
	for u in users:
		usernames.append(u['UserName'])
	return usernames

def main():
	users = json.load(sys.stdin)['Users']
	print(' '.join(get_list_of_users(users)))

if __name__== "__main__":
	main()