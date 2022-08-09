#Reverse the order of words in a given sentence.

str_val = "Hello World"
str_val1=str_val.split()
str_val1.reverse()
print(" ".join(str_val1))

#Write a program  that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#list2 = []
list1 = [10, 23, 23, 5, 67, 10]
list2 = set(list1)
print(list2)

#Write a password strength verifier in Python that checks if user password is strong.
#strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.

password1 = 'food'
import string
n=len(password1)
up, low, num, sym = False, False, False, False
for i in range(0, n):
    if password1[i].isupper() == True:
        up = True
    if password1[i].islower() == True:
        low = True
    if password1[i].isnumeric() == True:
        num = True
    if password1[i].isalpha() == True:
        sym = True
if up == True and low == True and num == True and sym == True:
    print("OK")
else: print("NOT OK")

password2 = '1EggPerD@y'
n=len(password2)
up, low, num, sym = False, False, False, False
for i in range(0, n):
    if password2[i].isupper() == True:
        up = True
    if password2[i].islower() == True:
        low = True
    if password2[i].isnumeric() == True:
        num = True
    if password2[i].isalpha() == True:
        sym = True
if up == True and low == True and num == True and sym == True:
    print("OK")
else: print("NOT OK")

#Write a program to reverse row sort in list of lists
list3= [[4,1,6], [7,9], [8,9,2,4]]
for i in list3:
    i.sort(reverse=True)
print(str(list3))

#Write a program to pair elements with rear element in matrix row

list4 = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
test =[]
for i in list4:
    test.append([[j, i [-1]] for j in i [:-1]])
print(str(test))

#Replace each special symbol with # in the following string
str1 = "%There &are three( students$ and& 1 trainer!"
import string
test1=''
for i in str1:
    if i in string.punctuation:
        test1='#'
    else:
        test1 += i
print(test1)

#Remove all characters for string except integers
str2 = "My mum has a 10 year old dog and 2 fishes"
numeric_filter=filter(str.isdigit, str2)
numeric_string = "".join(numeric_filter)
print(numeric_string)

#Remove all empty strings from a list of strings
name_list = ['orange', None, 'pineapple', "", 'apples', 'mangoes','Hello Dear','', 'Hello Sir']
name_list = list(filter(None, name_list))
print(str(name_list))