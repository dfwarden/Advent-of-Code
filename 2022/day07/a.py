'''
- input that starts with $ are commands we execute, no $ means output from command
- cd can change to /, .., or a directory in the current directory
- ls lists files and directories in current directory

- input does not seem to trick us:
    - no attempting cd into file
    - always ls before attempting cd

- find all directories with total size at most 100,000, sum them
'''
from collections import namedtuple

node_id_next = 0
#Node = namedtuple('Node', ['name', 'type', 'id', 'parent', 'children', 'size'], defaults=(None, [], 0))
#Node = {'name': '', 'id': 0, 'parent': None, 'children': [], 'size': 0}

nodes = {}
root = {'name': '/', 'type': 'dir', 'id': node_id_next, 'parent': None, 'children': [], 'size': 0}
node_id_next += 1
nodes[root['id']] = root
print(f'after incrementing, node_id_next is now {node_id_next}')
cwd = None
with open('input', 'r') as f:
    for line in f:
        line = line.rstrip()
        if line[0] == '$':  # command, cd or ls
            if line[2:4] == 'cd':
                if line[5] == '/':
                    # set cwd to root
                    cwd = root
                elif line[5:7] == '..':
                    print(f'changing cwd to parent {nodes[cwd["parent"]]["name"]}')
                    cwd = nodes[cwd['parent']]
                else:  # descend to named child (should exist already)
                    child_name = line[5:]
                    for child_id in cwd['children']:
                        if nodes[child_id]['name'] == child_name:
                            print(f'changing cwd from {cwd["name"]} ({cwd["id"]}) to {child_name} ({nodes[child_id]["id"]})')
                            cwd = nodes[child_id]
                            break
                    #print(f'after changing to child, cwd is now {cwd}')
        else:  # output from ls
            print(f'processing ls output in {cwd["name"]} ({cwd["id"]})')
            (size_or_dir, name) = line.split(' ')
            if size_or_dir.isnumeric():  # line is a file and has a size
                size = int(size_or_dir)
                child = {'name': name, 'type': 'file', 'id': node_id_next, 'parent': cwd['id'], 'children': [], 'size': size}
                node_id_next += 1
                #print(f'created child file node {child}')
                cwd['children'].append(child['id'])
                nodes[child['id']] = child
                # update self and parents with our newly discovered size
                # we need to be careful not to clobber cwd
                cursor = nodes[cwd['id']]
                while cursor['parent'] is not None:
                    cursor['size'] += size
                    cursor = nodes[cursor['parent']]
            else:  # line is a dir
                child = {'name': name, 'type': 'dir', 'id': node_id_next, 'parent': cwd['id'], 'children': [], 'size': 0}
                #print(f'created child directory node {child}')
                node_id_next += 1
                nodes[child['id']] = child
                cwd['children'].append(child['id'])

# tree should be built now, find all dirs of size <= 100000 and sum them
candidates = []

def find_candidates(cwd):
    #print(f'considering {cwd}')
    if cwd['size'] > 0 and cwd['size'] <= 100000:
        print(f'adding candidate {cwd["name"]} - size {cwd["size"]}')
        candidates.append(cwd)
    for child_id in cwd['children']:
        if nodes[child_id]['type'] == 'dir':
            find_candidates(nodes[child_id])

find_candidates(root)

print(f'Sum of all candidates: {sum(candidate["size"] for candidate in candidates)}')
