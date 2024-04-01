import re

def replace_whitespace_with_commas(string):
    result = re.sub(r"\s+", ", ", string.strip())
    return result

def string_to_list(string, convert_to_int=True):
    result = replace_whitespace_with_commas(string).split(', ')
    if convert_to_int:
        result = [int(i) for i in result]
    print(f'Length of list: {len(result)}')
    return sorted(result)