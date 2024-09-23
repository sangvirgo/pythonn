import json

def save_json(d, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(d, json_file, indent=4)

def read_json(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
    return data


data_dict = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}

save_json(data_dict, 'data.json')

read_data = read_json('data.json')
print(read_data)
