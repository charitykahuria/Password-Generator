import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 
'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 
'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 
'M','N','O','P', 'Q', 'R', 'S', 'T', 'U',
 'V', 'W', 'X', 'Y', 'Z']

numbers = ['1','2','3','4','5','6','7','8','9']
special_characters =['!','#','$','%','&','(',')','*','+']

print("Welcome to PyPassword Generator!!!")
prefered_length =int(input('Please specify password length?\n'))
num_of_letters = int(input('How many letters would you like in your password?\n'))
num_of_numbers = int(input('How many numbers would you like in your password?\n'))
num_of_specialchars = int(input('How many special characters would you like in your password?\n'))

##simple (weak password)

# password =''
# for chars in range(1,num_of_letters+1):
#     password += random.choice(letters)
# for chars in range(1,num_of_numbers+1):
#     password += random.choice(numbers)
# for chars in range(1,num_of_specialchars+1):
#     password += random.choice(special_characters)

#strong password
password =[]
password_len = (num_of_letters+num_of_numbers+num_of_specialchars)
if password_len > prefered_length:
    print("Character count is greater than specified password length")
else:
    for chars in range(1,num_of_letters+1):
        password += random.choice(letters)
    for chars in range(1,num_of_numbers+1):
        password += random.choice(numbers)
    for chars in range(1,num_of_specialchars+1):
        password += random.choice(special_characters)

    
    random.shuffle(password)
    password = ''.join(password)

print(password)

   


  


