import re

def input_split(command):
    """
    Split a raw command string into CLI-style arguments.
    :param command: Raw input command string.
    :return: List of parsed argument tokens.
    """
    pattern = r'("[^"]*"|\'[^\']*\'|\S+)'
    result = re.findall(pattern, command)

    return result