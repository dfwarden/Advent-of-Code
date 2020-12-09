import re
from collections import defaultdict

child_rules = {}
parent_rules = defaultdict(list)

def run():
    '''
        File input is a plain text file of lines where each line
        says how many different types of bags can be inside that type.

        Example:
            "plaid indigo bags contain 1 pale violet bag, 4 mirrored violet bags."
    '''
    with open('input') as f:
        lines = f.readlines()
    # Each rule says what kind of bag type can include how many and what kinds of children.
    # Build a dict of parent->child where the key is bag type and value is tuple of (count, bag_type)
    # Build a dict of child->parent where the key is bag type and value is list of bag type
    parent_pattern = r'^(\w+ \w+) bags contain'
    children_pattern = r'([0-9]+) (\w+ \w+)(?: bag[s]?)'
    for line in lines:
        parent = re.match(parent_pattern, line).group(1)
        children = re.findall(children_pattern, line)
        child_rules[parent] = children
        for (count, child) in children:
            parent_rules[child].append(parent)
    result = set(get_bag_parents(["shiny gold"]))
    # We subtract 1 to not include the shiny gold bag itself.
    print(f'testing - {len(result)-1}')


def get_bag_parents(parents_list):
    if parents_list == []:
        return []
    parents = []
    for parent in parents_list:
        parents.extend(parent_rules[parent])
    print(f'{parents_list} + recurse()')
    return parents_list + get_bag_parents(parents)




if __name__ == '__main__':
    run()
