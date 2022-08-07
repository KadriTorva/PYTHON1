#List exercises

info = ['karl', '100', 'red', 'Mangoes']
print(type(info))
info.reverse()
print(info)

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

index = 0
for i, j in zip(list1, list2):
    index+=1
    if index != len(list1):
        print(i+j, end=' ')
    elif index == len(list1):
        print(i+j)

list3 = [10, 20, 4]
mx = max(list3[0], list3[1])
#print(mx)
secondmax = min(list3[0], list3[1])
#print(secondmax)
n = len(list3)
#print(n)
for i in range (2, n):
    #print(list3[i])
    if list3[i] > mx:
        secondmax = mx
        mx=list3[i]
    elif list3[i] > secondmax and \
        mx !=list3[i]:
        secondmax=list3[i]
    elif mx == secondmax and \
        secondmax != list3[i]:
        secondmax = list3[i]
print(secondmax)

list4 = [70, 11, 20, 4, 100]
mx = max(list4[0], list4[1])
#print(mx)
secondmax = min(list4[0], list4[1])
#print(secondmax)
n = len(list4)
#print(n)
for i in range (2, n):
    #print(list3[i])
    if list4[i] > mx:
        secondmax = mx
        mx=list4[i]
    elif list4[i] > secondmax and \
        mx !=list4[i]:
        secondmax=list4[i]
    elif mx == secondmax and \
        secondmax != list4[i]:
        secondmax = list4[i]
print(secondmax)

list5 = ["Hello ", "take "]
list6 = ["Dear", "Sir"]
newlist = []
for i in(list5):
    for j in(list6):
        newlist.append([i] + [j])

print(newlist)


list7 = [5, 10, 15, 20, 25, 50, 20]
index=list7.index(20)
list7[index]=200
print(list7)

list8 = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = list8.count(10)
print(str(x))

list9 = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x2 = list9.count(16)
print(str(x2))

list10 = [5, 20, 15, 20, 25, 50, 20]
number_to_remove = 20
list10 = [value for value in list10 if value != number_to_remove]
print(list10)

list11 = ['Ade', 'orange', 'pineapple', 'apples', 'mangoes']
print(list11[int(len(list11)/2)])

list12 = [10, 3, 45, 67, 89, 0, 45]
print(list12[int(len(list12)/2)])




