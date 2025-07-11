# list dictioanr func
snacks=["chips","Soda","Cake"]
print(snacks)
# # After adding cookies 
snacks.append("cookies")
print(snacks)

snacks.remove("Soda")
print(snacks)

# sort
snacks.sort()
print(snacks)

print("Middle index snacks :",snacks[-2])
snacks[1]="juice"
print(snacks)

snacks.insert(1,"chocolate")
print(snacks)

del snacks[3]
print(snacks)


party_bag=[
    ["chips","cookies"],
    ["cake","Juice"],
    ["soda","pizza"]
]

for bag in party_bag:
    for item in bag:
       print(item)
table1=["chips","juices"]
table2=["cake","cookie"]
print(table1+table2)
