#Exercise-Day 4
#1
def concatenate(*args):
    return " ".join(args)

print(concatenate("Thirty", "Days", "Of", "Python"))

#2 
def concatenate(*args):
    return " ".join(args)

print(concatenate("Coding", "For", "all"))

#3
company = "Coding For All"
#4
print(company)
#5
print(len(company))
#6
print(company.upper())
#7
print(company.lower())
#8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9
print(company[7:10])
#10
print(company.index('C'))
print(company.find('F'))
print(company.replace("Coding", "Python"))
#11
print(company.replace("Coding For All", "Python For Everyone"))
#12
print(company.replace("Python For Everyone", "Python For All"))
#13
print(company.split())
#14
apps="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(apps.split(","))
#15
print(company[0])
#16
print(company[-1])
#17
print(company[10])
#18
text = "Python For Everyone"
words = text.split()
acronym = "".join(word[0] for word in words)
print(acronym)
#19
text = "Coding For All"
words = text.split()
acronym = "".join(word[0] for word in words)
print(acronym)
#20
print(company.index('C'))
#21
print(company.index('F'))
#22
print(company.rindex('l'))
#23
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.find("because"))
#24
print(sentence.rfind("because"))
#25
print(sentence[31:54])
#26
print(sentence.index("because"))
#27
print(sentence[31:54])
#28
print(company.startswith("Coding"))
#29
print(company.endswith("Coding"))
#30
print('   Coding For All      '.strip())
#31
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())
#32
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid','Falcon']
print(" ".join(python_libraries))
#33
print("I am enjoying this challenge.\nI just wonder what is next.")
#34
print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")
#35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area}.")
#36
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")