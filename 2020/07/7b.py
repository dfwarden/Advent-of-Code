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
    result = get_bag_count("shiny gold")
    print(f'got result: {result}')


def get_bag_count(parent_bag):
    # How many sub-bags does parent_bag require?
    if child_rules[parent_bag] == []:
        return 0  # no additional bags required
    children_count = 0
    for (child_count, child_type) in child_rules[parent_bag]:
        # For each rule, add to children the number of immediately necessary child bags
        # and the recursive count for those immediately necessary bags.
        children_count += int(child_count) + (int(child_count) * get_bag_count(child_type))
    #print(f'1 {parent_bag} requires {child_count} {child_type} bags, {children_count} total inside {parent_bag}')
    return children_count




if __name__ == '__main__':
    run()
