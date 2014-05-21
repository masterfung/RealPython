from random import choice

nouns = ["fossil", "Obama", "Romney", "horse", "Alice", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla", "chimp", "superhero", "katana"]
verbs = ["kicks", "jingles", "fights", "interviews", "cuddles", "punches", "bounces", "slurps", "meows", "explodes", "curdles", "hurdles", "jumps", "cuts"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening", "tasty", "baffaled", "sensual"]
prepositions = ["against", "on", "before", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within", "without", "notwithstanding"]
adverbs = ["curiously", "faithfully", "extravagantly", "tantalizingly", "furiously", "sensuously", "joyously", "religiously"]

def makePoem():
	n1 = choice(nouns)
	n2 = choice(nouns)
	n3 = choice(nouns)
    # Make sure that all the nouns are different
	while n1 == n2:
		n2 = choice(nouns)
	while n1 == n3 or n2 == n3:
		n3 = choice(nouns)   

    # Pull three different verbs
	v1 = choice(verbs)
	v2 = choice(verbs)
	v3 = choice(verbs)
	while v1 == v2:
		v2 = choice(verbs)
	while v1 == v3 or v2 == v3:
		v3 = choice(verbs)

    # Pull three different adjectives
	adj1 = choice(adjectives)
	adj2 = choice(adjectives)
	adj3 = choice(adjectives)
	while adj1 == adj2:
		adj2 = choice(adjectives)
	while n1 == n3 or n2 == n3:
		adj3 = choice(adjectives)   
	     
	# Pull two different prepositions
	prep1 = choice(prepositions)
	prep2 = choice(prepositions)
	while prep1 == prep2:
		prep2 = choice(prepositions)

	# Pull one adverb
	adv1 = choice(adverbs)

	if "aeiou".find(adj1[0]) != -1: # first letter is a vowel
		article = "An"
	else:
		article = "A"

	# add lines to poem
	poem = "{} {} {}\n\n".format(article, adj1, n1)
	poem = poem + "{} {} {} {} {} the {} {}\n".format(article, adj1, n1, v1, prep1, adj2, n2)
	poem = poem + "{}, the {} {}\n".format(adv1, n1, v3)
	poem = poem + "the {} {} {} a {} {}".format(n2, v2, prep2, adj3, n3)
	return poem


print makePoem()