 donuts=["glazed","chocolate","galactic sprinkle","nut"]
 print(donuts)

for dount in donuts:
    print(dount)
    
angle=0
 while angle<90:
    print("Angle :",angle)
    angle=angle+30
    
 i=2
 while i<11:
    print(i)
    i=i+2

for i in range(2,11,2):
     print(i)

 protocols=["ok","ok","bad","ok"]

for i,protocol in enumerate(protocols):
    print(i,protocol)
    if protocol == "bad":
        break
