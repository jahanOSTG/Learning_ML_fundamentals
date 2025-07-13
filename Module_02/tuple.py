mytuple=("apple","banana","cherry")
print(mytuple)

print(len(mytuple))

print(mytuple[2:5])

convert_to_list=list(mytuple)
print(convert_to_list)

convert_to_list[1]="kiwi"
convert_to_list.append("orange")
mytuple=tuple(convert_to_list)
print(mytuple)

















