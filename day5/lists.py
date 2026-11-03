#Exercise 5-Level 1
#1
empty_list = []
#2
list_with_elements = [1, 2, 3, 4, 5]
#3
print(len(list_with_elements))
#4
first_element = list_with_elements[0]
last_element = list_with_elements[-1]
middle_element = list_with_elements[len(list_with_elements)//2]
#5
mixed_data_types = ['Dhanush', 21, 162.5, False, 'Chittoor']
#6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7
print(it_companies)
#8
print(len(it_companies))
#9
first_company = it_companies[0]
last_company = it_companies[-1]
middle_company = it_companies[len(it_companies)//2]
print(first_company, last_company, middle_company)
#10
it_companies[0] = 'Tesla'
print(it_companies)
#11
it_companies.append('Cognizant')
#12
it_companies.insert(3, 'Infosys')
#13
it_companies[0] = it_companies[0].upper()
#14
print('#'.join(it_companies))
#15
print('Facebook' in it_companies)
#16
it_companies.sort()
print(it_companies)
#17
it_companies.reverse()
print(it_companies)
#18
print(it_companies[0:3])
#19
print(it_companies[-3:])
#20
print(it_companies[len(it_companies)//2:(len(it_companies)//2)+3])
#21
it_companies.pop(0)
print(it_companies)
#22
it_companies.pop(len(it_companies)//2)
print(it_companies)
#23
it_companies.pop(-1)
print(it_companies)
#24
it_companies.clear()
print(it_companies)
#25
print(it_companies.clear())
#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
fullstack = front_end + back_end
#27
full_stack=fullstack.copy()
full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)

#Exercise 5-Level 2
#1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
median_age = ages[len(ages)//2] if len(ages) % 2 != 0 else (ages[len(ages)//2 - 1] + ages[len(ages)//2]) / 2
average_age = sum(ages) / len(ages)
range_age = max_age - min_age
res1 = abs(min_age - average_age)
res2 = abs(max_age - average_age)
if min_age < average_age < max_age:
    print("Average age is between min and max age")

#1
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
middle_index = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[middle_index - 1:middle_index + 1]
else:
    middle_countries = [countries[middle_index]]
print("Middle country/countries:", middle_countries)

#2
first_half = countries[:middle_index]
second_half = countries[middle_index:]
print("First half:", first_half)
print("Second half:", second_half)

#3
countries_1=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
unpack_countries = countries_1[:3] + countries_1[-4:]
print("Unpacked countries:", unpack_countries)
