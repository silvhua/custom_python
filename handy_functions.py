

def print_dict_values_for_key(results_dict, key, zero_indexed=False):
    """
    Prints the values of a dictionary for a given key.

    Parameters:
    - results_dict (dict): Dictionary to print values for.
    - key (str): Dictionary key to print values for.
    - zero_indexed (bool): If True, prints the index of each value starting from 0. If False, prints the index starting from 1.
        """
    for index, item in enumerate(results_dict):
        print(f"{index+1 if zero_indexed==False else index}: {results_dict[item].get(key, 'None').strip()}", end='\n\n')