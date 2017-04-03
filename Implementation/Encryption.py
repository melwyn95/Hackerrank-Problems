import math
string = raw_input()
row = int(math.ceil(len(string) ** 0.5))
col = int(math.ceil(len(string) ** 0.5))
spaces = row * col
spaces -= len(string)
for i in range(spaces):
    string += " "
encrypt = []
i = 0
j = 0
k = 0
while i < row and k < len(string):
    j = 0
    new_list = []
    while j < col and k < len(string):
        new_list.append(string[k])
        k += 1
        j += 1
    encrypt.append(new_list)
    i += 1
#print encrypt
encrypt_final = []
for i in range(col):
    new_list = []
    for j in range(row):
        new_list.append(encrypt[j][i])
    encrypt_final.append(new_list)
string_final = ""
for i in range(col):
    for j in range(row):
        if encrypt_final[i][j] != " ":
            string_final += encrypt_final[i][j]
    string_final += " "
print string_final
