import random


random_number=random.randint(1,100)

print(random_number)

# randint for whole number random is a module
#
# random.randrange(start, stop, step)
# start	Starting value
# stop	Ending value (not included)
# step	Difference between numbers

# random.random(): Returns a random float in the range ([0.0, 1.0]).

random_number=random.random()
print(random_number)

# random.uniform(a, b): Returns a random float N such that \(a <= N <= b)

random_number=random.uniform(1,100)
print(random_number)