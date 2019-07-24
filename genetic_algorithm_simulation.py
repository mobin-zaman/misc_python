import random


count = 0


def randmon_number():
    return random.randint(0, 3)


def mutation(chromosome_list):
    for chromosome in chromosome_list:
        index = randmon_number()
        choice = random.randint(0, 1)


        if(choice == 0):
            chromosome[index] += 2
            if(chromosome[index] > 9):
                chromosome[index] = 0

        else:
            chromosome[index] -= 2
            if(chromosome[index] < 0):
                chromosome[index] = 9

    return chromosome_list


def fitness(a):
    return 1/((7-a[0])**3)+((6-a[1])**2)+(2-a[2])+a[3]


def sort_chromosome_list(chrome_list):
    return sorted(chrome_list, key=lambda x: fitness(x), reverse=True)


def crossover(chrome1, chrome2):

    choice = random.randint(1, 3)

    print("parents: ", chrome1, chrome2, end='')

    chrome3 = chrome2[:choice]+chrome1[choice:]
    chrome4 = chrome1[:choice]+chrome2[choice:]

    print(" child: ", chrome3, chrome4)
    return chrome3, chrome4


def giving_birth(c_list):

    new_born = []
    print("crossover process: ")
    new_born.extend(crossover(c_list[0], c_list[1]))
    new_born.extend(crossover(c_list[1], c_list[2]))
    new_born.extend(crossover(c_list[0], c_list[3]))


    return new_born

'''MUST CHANGE THE VALUES OF THE BELOW LINES'''
chromosome_list=[[3, 5, 2, 4], [1, 2, 6, 9], [5, 7, 9, 3], [1, 3, 6, 6]]

count += 1
print("generation: {0}".format(count))
for chrome in chromosome_list:
    print(chrome)

print("fitness:")
for chrome in chromosome_list:
    print(chrome, fitness(chrome))

print("sorted by fitness")
sorted_by_fitness=sort_chromosome_list(chromosome_list)
for chrome in sorted_by_fitness:
    print(chrome)

children=giving_birth(sorted_by_fitness)
print("children of the fittest")
for chi in children:
	print(chi)

print("mutation")
children=mutation(children)
for chrome in children:
    print(chrome)

print("again fitness for mutated")
for chrome in children:
    print(chrome,fitness(chrome))

print("sorted by fitness")
children=sort_chromosome_list(children)
for chrome in children:
    print(chrome)

print()

for i in range(5):
    count+=1
    print("generation: {0}".format(count))
    chromosome_list=children[0:4]
    for chrome in chromosome_list:
        print(chrome)
    
    print("creating child")
    children=giving_birth(chromosome_list)
    for chrome in children:
        print(chrome)
    
    print("mutation")
    children=mutation(children)
    for chrome in children:
        print(chrome)
    
    print("fitness")
    for chrome in children:
        print(chrome, fitness(chrome))

    print("sorted by fitness")
    children=sort_chromosome_list(children)
    for chrome in children:
        print(chrome)

    print()
  