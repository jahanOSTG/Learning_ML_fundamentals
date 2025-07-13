thisset={"Apple","Banana","Apple","Grape",True,0,67} #Duplicate doesn't allow here
print(thisset) # Dont follow any order
                 # Dont follow any indexing
                 
thisset.add("Orange")
print(thisset)# serial is not matter

tropical={"Pineapple","Mango","Papaya"}
thisset.update(tropical)
print(thisset)
print(tropical)

thisset.remove("Papaya")
print(thisset)

thisset.discard(0) #discard==remove
print(thisset)

set1={"a","b","c"}
set2={1,2,3,"a","b"}
set3=set1.union(set2)  #union only works in set
print(set3)

set4=set1.intersection(set2)
print(set4)

set5=set1.difference(set2)
print(set5)