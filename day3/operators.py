# #Arithmetic operators
# print('Addition: ', 1 + 2)      
# print('Subtraction: ', 2 - 1)     
# print('Multiplication: ', 2 * 3)  
# print ('Division: ', 4 / 2)             
# print('Division without the remainder: ', 7 // 2)   
# print('Modulus: ', 3 % 2)         
# print('Exponentiation: ', 2 ** 3) 

# # Complex numbers
# print('Complex number: ', 1 + 1j)
# print('Multiplying complex numbers: ',(1 + 1j) * (1 - 1j))

# a=3
# b=2

# # Arithmetic operations and assigning the result to a variable
# total = a + b
# diff = a - b
# product = a * b
# division = a / b
# remainder = a % b
# floor_division = a // b
# exponential = a ** b

# print(total) 
# print('a + b = ', total)
# print('a - b = ', diff)
# print('a * b = ', product)
# print('a / b = ', division)
# print('a % b = ', remainder)
# print('a // b = ', floor_division)
# print('a ** b = ', exponential)

# #comparison operators
# print(3 > 2)     
# print(3 >= 2)    
# print(3 < 2)     
# print(2 < 3)     
# print(2 <= 3)    
# print(3 == 2)    
# print(3 != 2)    
# print(len('mango') == len('avocado'))  
# print(len('mango') != len('avocado'))  
# print(len('mango') < len('avocado'))   
# print(len('milk') != len('meat'))      
# print(len('milk') == len('meat'))      
# print(len('tomato') == len('potato'))  
# print(len('python') > len('dragon'))

# #logical operators
# print(3 > 2 and 4 > 3)
# print(3 > 2 or 4 > 3)
# print(not 3 > 2)
# print(not not True)

#Excercise 01
# age=21
# height=162.5
# complex=1+2j
# #area of traingle
# base=int(input("Enter Base:"))
# height=int(input("Enter Height:"))
# area_of_traingle=0.5*base*height
# print("The area of Traingle is ",area_of_traingle)
# #perimetre of a traingle
# a=int(input("Enter side a:"))
# b=int(input("Enter side b:"))
# c=int(input("Enter side c:"))
# per_of_traingle=a*b*c
# print("The Perimetre of the Traingle:",per_of_traingle)
# #area and perimetre of rectangle
# l=int(input("Enter length="))
# w=int(input("Enter width="))
# area=l*b
# perimetre=2*(l+b)
# print("area",area)
# print("perimetre",perimetre)
# #area and circumference of circle
# r=float(input("Enter the radius:"))
# ar_circle=3.14*r*r
# cir_circle=2*3.14*r
# print("area of circle",ar_circle)
# print("circum of circle",cir_circle)
# #   slope of y=2x-2
# slope=2
# x=1
# y=-2
# print("x intercept",x)
# print("y intercept",y)
# #Eucldian distance
# x1 = int(input("Enter x1: "))
# y1 = int(input("Enter y1: "))
# x2 = int(input("Enter x2: "))
# y2 = int(input("Enter y2: "))
# slope = (y2 - y1) / (x2 - x1)
# distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# print("Slope:", slope)
# print("Euclidean distance:", distance)
# #10
# # Task 8: Slope of y = 2x - 2
# slope1 = 2
# # Task 9: Slope between two points
# x1 = int(input("Enter x1: "))
# y1 = int(input("Enter y1: "))
# x2 = int(input("Enter x2: "))
# y2 = int(input("Enter y2: "))
# slope2 = (y2 - y1) / (x2 - x1)
# print("Slope of task 8:", slope1)
# print("Slope of task 9:", slope2)
# if slope1 == slope2:
#     print("Both slopes are equal")
# else:
#     print("Both slopes are not equal")

# x = int(input("Enter the value of x: "))
# #11
# y = x**2 + 6*x + 9
# print("The value of y is:", y)
# if y == 0:
#     print("The value of y is zero")
# else:
#     print("The value of y is not zero")

# #12
# a = "python"
# b = "dragon"
# print(len(a))
# print(len(b))
# print(len(a) > len(b))


# # 13 & 15
# print('on' in 'python' and 'on' in 'dragon')

# # 14. Use in operator to check if jargon is in the sentence
# sentence = "I hope this course is not full of jargon"
# print('jargon' in sentence)

# # 16. Find the length of the text python and convert the value to float and string
# text = "python"
# length = len(text)
# print("Length:", length)
# print("Float:", float(length))
# print("String:", str(length))

# # 17. Check whether a number is even or odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

#18
print(7//3==int(2.7))

#19
print(type(10)==type(10))

#20
print(int('9.8')==10)

#21
hours=float(input("Enter hours "))
rate=int(input("Enter rate "))
weekly_earnings=hours*rate
print("The Weekly earnings are:",weekly_earnings)

#22
years=int(input("Enter no.of years you have lived:"))
seconds=years*365*24*60*60
print("you have lived for",seconds ,"seconds")

#23
for i in range(1,6):
    print(i, 1,i, i**2,i**3)
