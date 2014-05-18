from __future__ import division
from random import randint

def election():
	return randint(0,1)

candidateATotal = 0
candidateBTotal = 0

total = 10000
for runs in range(0,total):
	a = 0
	b = 0
	if election() < .87:
		a += 1
	else:
		b += 1
	if election() < .65:
		a += 1
	else:
		b +=1
	if election() < .17:
		a += 1
	else:
		b += 1
	if a > b:
		candidateATotal += 1
	else:
		candidateBTotal += 1
print 'Candidate A:', candidateATotal/total, \
'\nCandidate B:', candidateBTotal/total
