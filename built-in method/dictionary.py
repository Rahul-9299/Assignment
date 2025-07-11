dict_1={"rahul":1, "rohit":2, "sita":3, "gita":4}

#method: get
dict_get = dict_1.get("rahul")
print("Value for 'rahul' in dict_1:", dict_get)

#method: keys
dict_keys = dict_1.keys()   
print("Keys in dict_1:", dict_keys)

#method: values
dict_values = dict_1.values()
print("Values in dict_1:", dict_values)

#method: setdefault
dict_setdefault = dict_1.setdefault("ram", 5)   
print("Set default for 'ram' in dict_1:", dict_setdefault)