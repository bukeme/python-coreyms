import random 

# value = random.random()
# value = random.uniform(1, 10)
# value = random.randint(1, 6) # 6 included

# greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
# value = random.choice(greetings)
# print(value + ', Corey!')

# colors = ['Red', 'Black', 'Green']

# # results = random.choices(colors, k=10)
# results = random.choices(colors, weights=[18, 18, 2], k=10)
# print(results)

deck = list(range(1, 53))
# random.shuffle(deck)
hand = random.sample(deck, k=5)
print(hand)
