# It is a well-known fact that Mr. Krabs owns a very popular restaurant, known as the Krusty Krab. He makes a lot of money from his restaurant, and all day long he's only counting his money. Not satisfied with his billions, he also opened an amusement park, called Krustyland, which contains lots of famous attractions, like roller coasters and ferris wheels. Recently, he has decided to open a haunted house. It is the scariest haunted house ever! In fact, it is so scary, that most people don't even want to go inside alone.
#
# There are N people who want to visit the haunted house. The ith person will only go if at least Li other people will go with him. Additionally, that person doesn't want to go with more than Hi other people, since it would ruin the experience for them.
#
# What is the maximum number of people that can visit the haunted house at one time so that no constraint is violated?
#
# Input Format
#
# The first line contains a single integer, N, the number of people.
#
# N lines follow. The ith line contains two integers, Li and Hi, which are the minimum and maximum number of people the ith person wants to go with, respectively.
#
# Constraints
# 1≤N≤3×105
# 0≤Li≤Hi<3×105
# Output Format
#
# Output a single integer, the maximum number of people Mr. Krabs can lure into the haunted house.
# n = int(raw_input())
# x = []

for i in range(n):
	x.append(map(int, raw_input().split()))

def haunted(n):
	people_going = 0
	temp_max = 0
	max_going = 0

	for people_going in range(n,0,-1) :
		for j in range(n):
			if x[j][0]+1 <= people_going and x[j][1]+1 >=people_going :
				temp_max += 1
			if temp_max == people_going:
					max_going = temp_max
					return max_going

		temp_max = 0


answer = haunted(n)
print answer
