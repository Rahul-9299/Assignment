with open("grocery.txt","w") as f:
    f.write("ID\t\tNAME\t\tPRICE\t\t\tCATEGORY\n")
    records=[
        {"name":"rice","price":120,"category":"grocery"},
        {"name":"wheat","price":220,"category":"grocery"},
        {"name":"sugar","price":320,"category":"grocery"},
        {"name":"cereal","price":420,"category":"grocery"},
    ]
    for i in range(len(records)):
        data=records[i]
        f.write(f"{i+1}\t\t{data["name"]}\t\t{data["price"]}\t\t\t{data["category"]}\n")

with open("grocery.txt","r") as f:
    content= f.read()
    print(content)
    