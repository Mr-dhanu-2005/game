#Day 2: 30 Days of python programming
#Excersice Level-1
first_name = "Dhanush"
last_name = "V"
full_name = f"{first_name} {last_name}"
country = "India"
city = "Bengaluru"
age = 28
year = 2026
is_married = False
is_true = True
is_light_on = True
first_name,last_name,country,city="Dhanush","V","India","Bengaluru"

#Excercise Level-2
print("first_name:", type(first_name))
print("last_name:", type(last_name))
print("full_name:", type(full_name))
print("country:", type(country))
print("city:", type(city))
print("age:", type(age))
print("year:", type(year))
print("is_married:", type(is_married))
print("is_true:", type(is_true))
print("is_light_on:", type(is_light_on))
print("-" * 30)
print(len(first_name))
first=len(first_name)
last=len(last_name)
if(first<last):
    print("The last name length is big",last)
elif(first>last):
    print("The First name length is big",first)
else:
    print("Both are equal")
#4
n1=5
n2=4
add=n1+n2
sub=n1-n2
mul=n1*n2
div=n1/n2
mod=n1%n2
power=n1**n2
floor_div=n1//n2

r=30
area_of_circle=3.14*r*r
print("Area of circle",area_of_circle)
circum_of_circle=2*3.14*r
print("Circumference of circle",circum_of_circle)
radius=float(input("Enter a radius:"))
area=3.14*radius*radius
print("Area of Circle:",area)

first_name=input("Enter your first name:")
last_name=input("Enter your last name:")
country=input("Enter your country:")
age=int(input("Enter your age:"))
help('keywords')


