#Exercise 1: Level 1
#1
tuple=()
print(tuple)
#2
members=('dhanush','vtp','charan','mounika','yuva')
#3
brothers=('dhanush','vtp','charan')
sisters=('mounika','yuva')
siblings=brothers+sisters
print(siblings)
#4
print(len(siblings))    
#5
family_members=siblings+('father','mother')
print(family_members)
#Exercise 2: Level 2
#1
print("Siblings:", family_members[:5])
print("Parents:", family_members[-2:])
#2
fruits=('banana','orange','mango','lemon')
vegetables=('tomato','potato','cabbage','onion','carrot')
animal_products=('milk','meat','eggs','honey')
food_stuffs=fruits+vegetables+animal_products
print(food_stuffs)
#3
food_stuff_lt=list(food_stuffs)
print(food_stuff_lt)
#4
middle_index=len(food_stuff_lt)//2
print("Middle item:", food_stuff_lt[middle_index])
#5
print("First three items:", food_stuff_lt[:3])
print("Last three items:", food_stuff_lt[-3:])
#6
del food_stuff_lt[0:12]
print(food_stuff_lt)
#7
nordic_countries=('Denmark','Finland','Iceland','Norway','Sweden')
print("Is 'Estonia' a nordic country?", 'Estonia' in nordic_countries)
print("Is 'Iceland' a nordic country?", 'Iceland' in nordic_countries)