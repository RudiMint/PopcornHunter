import re

def input_split(command):
    pattern = r'("[^"]*"|\'[^\']*\'|\S+)'
    result = re.findall(pattern, command)

    return result