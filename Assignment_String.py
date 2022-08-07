input = "JhonDipPeta"
mi = int(len(input) / 2)
res= input[mi-1 : mi+2]
print(res)

s1 = "Aunt"
s2 = "Sister"
s3 = s2[:3] + s1 + s2[3:]
print(s3)

s4= "America"
s5= "Japan"

s6 =s4[0] + s5[0] + s4[int(len(s4) /2)] + s5[int(len(s5) /2)]+ s4[-1] +s5[-1]
print(s6)

s7 = "Yn"
s8 = "PYnative"
print(s7 in s8)

s9 = "Ynf"
s10 = "PYnative"
print(s9 in s10)


str1 = "Emma-is-a-data-scientist"
str2 = str1.split("-")
print(str2[0] + ", " + str2[-1])

str3 = "Emma is a data scientist who knows Python. Emma works at google."
str4 = str3[::-1]
print(str4)
str5=str3.rfind("Emma")
print(str5)