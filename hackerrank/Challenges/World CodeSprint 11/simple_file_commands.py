#!/bin/python

import sys

def create(map, parts):
    file_name = parts[1]
    if map.has_key(file_name):
        if map[file_name][1]:
            no = min(map[file_name][1])
            del map[file_name][1][map[file_name][1].index(no)]
        else:
            no = map[file_name][0]
        map[file_name][0] += 1
        if no == 0:
            return parts[1]
        else:
            return parts[1] + '(' + str(no) + ')'
    else:
        map[file_name] = [1, []]
        return parts[1]

def delete(map, parts):
    file_bracket = parts[1].find('(')
    file_no = int(parts[1][file_bracket + 1: parts[1].find(')')]) if file_bracket >= 0 else 0
    file_name = parts[1][0:file_bracket] if file_bracket >= 0 else parts[1]
    map[file_name][1].append(file_no)
    map[file_name][0] -= 1

    return parts[1]

map = {}
q = int(raw_input().strip())
# Process each command
for a0 in xrange(q):
    # Read the first string denoting the command type
    command = raw_input().strip()
    # Write additional code to read the command's file name(s) and process the command
    # Print the output string appropriate to the command
    parts = command.split()
    if(parts[0] == 'crt'):
        print '+ ' + create(map, parts)
    if(parts[0] == 'del'):
        print '- ' + delete(map, parts)
    if(parts[0] == 'rnm'):
        delete_file = parts[1]
        create_file = parts[2]
        delete(map, ['del', delete_file])
        result = create(map, ['crt', create_file])
        print 'r ' + delete_file + ' -> ' + result