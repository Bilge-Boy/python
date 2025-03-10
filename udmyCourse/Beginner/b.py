import random as rn
import string as str
#simple list example
# a_list = ["a","b","c","d"]
# print(len(a_list))
# total_sum = max(a_list)
# print(total_sum)
#----------------------#
#exe
# array = []
# for i in range(10):
#     print(i)
#     array.append(rn.randint(0,100))
# print(array)
# max = 0
# for num in array:
#     if num > max:
#         max = num
# print(max)
##--------------------##
#password generation:
cap_letter_list = []
letter_list = [] 
numbers = []
symbols = [] 
pick_list = ["letter","number","symbol"]
generated_pass = []

for char in str.ascii_uppercase:
    cap_letter_list.append(char)
for char in str.ascii_lowercase:
    letter_list.append(char)
for char in str.punctuation:
    symbols.append(char)
for char in str.digits:
    numbers.append(char)

users_choise_contain_cap = int(input('is the password should contain capital letters? press 0 for NO and 1 for YES\n'))
if users_choise_contain_cap!=0 and users_choise_contain_cap!=1:
    print("illegal choise, try run the script again")
    quit()
letter_size = int(input('how many letters? insert a number bigger than 0\n'))
if  letter_size  < 0:
    print("illegal choise, try run the script again\n")
    quit()
number_size = int(input('how many numbers? insert a number bigger than 0\n'))
if number_size < 0:
    print("illegal choise, try run the script again")
    quit()
symbol_size = int(input('how many synbols? insert a number bigger than 0\n'))
if symbol_size < 0:
    print("illegal choise, try run the script again")
    quit()

loop_size = letter_size+number_size+symbol_size
for i in range(loop_size):
    if letter_size == 0 :
        if "letter" in pick_list:
            pick_list.remove("letter")
    if number_size == 0 : 
        if "number" in pick_list:
            pick_list.remove("number")
    if symbol_size == 0 : 
        if "symbol" in pick_list:
            pick_list.remove("symbol")
    pick = rn.choice(pick_list)   #pick_list[rn.randint(0,len(pick_list)-1)]
    match pick:
        case "letter":
            if users_choise_contain_cap == 1:
                match rn.randint(0,1):
                    case 0:
                        generated_pass.append(rn.choice(cap_letter_list))    #append(cap_letter_list.pop(rn.randint(0,len(cap_letter_list)-1)))
                    case 1:
                        generated_pass.append(rn.choice(letter_list))        #.append(letter_list.pop(rn.randint(0,len(letter_list)-1)))
            else:
                generated_pass.append(rn.choice(letter_list))                #.append(letter_list.pop(rn.randint(0,len(letter_list)-1)))
            letter_size-=1
        case "number":
            generated_pass.append(numbers.pop(rn.randint(0,len(numbers)-1)))
            number_size -=1
        case "symbol":
            generated_pass.append(symbols.pop(rn.randint(0,len(symbols)-1)))
            symbol_size -=1
                                  

    
print(''.join(generated_pass))
