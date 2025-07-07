print("Welcome new world")
#fuel=0.5
# home=38880

home=int(input("Enter ditance : "))
fuel=float(input("Enter fuel :"))
need=home*fuel
print("Need :",int(need),"unit")

chocolate=3
sprinkle=2
price_choco=5
price_sprin=6
total=(chocolate*price_choco)+(sprinkle*price_sprin)
print("Total Cost : ",total)


tax=total*0.1
final_cost=total+tax
print("Final Cost :",final_cost)

total_slices=8
aliens=3

slices_per_alien=total_slices/aliens
print("Per alien gets : ",slices_per_alien,"Pices")

full_slices=total_slices // aliens
print("Each aliens will get ",full_slices,"Pices of full slices")
left=total_slices % aliens
print("Left Over slices : ",left)
size=[54,234,65,123,65,23]
print(min(size))
print(max(size))
movement= -15
distance=abs(movement)
print("Distance :",distance)
power=pow(3,4)
print(power)
