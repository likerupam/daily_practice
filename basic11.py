# insert into dictionary
def insert_dict(query, dict):
    # query format: ['i', 'name', 'marks']
    key = query[1]
    value = int(query[2])
    dict[key] = value
    print("Inserted")


# deleting from dictionary
def del_dict(query, dict):
    # query format: ['d', 'name']
    key = query[1]
    if key in dict:
        del dict[key]
        print("Deleted")
    else:
        print("-1")


# print marks of required name
def print_dict(key, dict):
    if key in dict:
        print(f"Marks of {key} is {dict[key]}")
    else:
        print("-1")
