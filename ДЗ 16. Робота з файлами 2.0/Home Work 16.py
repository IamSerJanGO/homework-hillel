import pickle

#  1
list_dict = [{'key': 'value'}, {'key': 'value'}, {'key': 'value'}, {'key': 'value'}]
with open('file.txt', 'wb') as file:
    pickle.dump(list_dict, file)


# 2
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            if isinstance(merged_dict[key], list):
                merged_dict[key].append(value)
            else:
                merged_dict[key] = [merged_dict[key], value]
        else:
            merged_dict[key] = value
    return merged_dict


A = {'key': 1, 'key2': True}
B = {'key': 'Hello'}
C = merge_dictionaries(A, B)
print(C)
