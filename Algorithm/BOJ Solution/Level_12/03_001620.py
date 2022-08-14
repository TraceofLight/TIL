import sys

pokemon_number, find_pokemon = list(map(int, sys.stdin.readline().split()))

pokemon_names = []
pokemon_numbers = []
output = []

index = 1
for _ in range(pokemon_number):
    pokemon_name = sys.stdin.readline().strip()
    pokemon_names.append([index, pokemon_name])
    pokemon_numbers.append([pokemon_name, index])
    index += 1

number_to_name = dict(pokemon_names)
name_to_number = dict(pokemon_numbers)

for _ in range(find_pokemon):
    information = sys.stdin.readline().strip()
    if information.isnumeric():
        output.append(number_to_name.get(int(information)))
    else:
        output.append(name_to_number.get(information))

for element in output:
    print(element)
