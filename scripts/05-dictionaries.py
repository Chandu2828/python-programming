sample_dict = {
    'colors': ['orange', 'red', 'blue'],
    'numbers': [1234, 456, 789, 10],
    'tools': ['Ansible', 'Terraform', 'Prometheus', 'Docker', 'Kubernetes'],
    (1234, 456, 789): 'a',
}

# [1234, 456, 789, 10] is a list which is mutable so you can't use it as a key. 
# print(sample_dict)
# print(sorted(sample_dict['colors']))
# sample_dict['numbers'][-1] = 100
# print(sample_dict['numbers'])
# sample_dict['fruits'] = ['apple', 'banana', 'orange']
# print(sample_dict)

# sample_dict = {
#     "employee": {
#         "name": "Purna",
#         "age": 27,
#         "city": "Tanuku"
#     }
# }

# print(sample_dict["employee"]["age"])

# print(sample_dict.keys())
# print(sample_dict.values())
# print(sample_dict.items())

# [
#     ('colors', ['orange', 'red', 'blue']), 
#     ('numbers', [1234, 456, 789, 10]), 
#     ('tools', ['Ansible', 'Terraform', 'Prometheus', 'Docker', 'Kubernetes']), 
#     ((1234, 456, 789), 'a')
# ]