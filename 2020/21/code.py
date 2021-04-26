def read_file():
    foods = {}
    with open('input.txt', 'r') as f:
        return f.read().strip().split('\n')

def get_foods_info(data):
    all_ingredients = []
    all_allergens = {}

    for line in data:
        ingredients, allergens = line.split(' (contains ')
        i_list = ingredients.strip().split(' ')
        a_list = allergens.strip(')').split(', ')
        all_ingredients += i_list
        for allergen in a_list:
            if allergen in all_allergens:
                all_allergens[allergen] &= set(i_list)
            else:
                all_allergens[allergen] = set(i_list)
    return all_allergens, all_ingredients

def part1(data):
    all_allergens, all_ingredients = get_foods_info(data)
    allergen_foods = set([i for v in all_allergens.values() for i in v])
    safe_foods = [i for i in all_ingredients if i not in allergen_foods]
    return len(safe_foods)

def part2(data):
    all_allergens, _ = get_foods_info(data)
    al_to_ing = {}

    while all_allergens:
        known = [(k, list(v)[0]) for k, v in all_allergens.items() if len(v) == 1]
        for k, v in known:
            al_to_ing[k] = v
            del all_allergens[k]
            for a in all_allergens:
                if v in all_allergens[a]:
                    all_allergens[a].remove(v)

    return ','.join([v for _, v in sorted(al_to_ing.items())])

if __name__ == '__main__':
    data = read_file()
    print(part1(data))
    print(part2(data))
