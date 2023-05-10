a = "7i3"
b = "Tsi"
c = "h%x"
d = "i #"
e = "sM "
f = "$a "
g = "#t%"
h = "^r!"

lst = [a, b, c, d, e, f, g, h]
lst_1 = []
lst_2 = []
lst_3 = []

for i in lst:
    lst_1.append(i[0])
    lst_2.append(i[1])
    lst_3.append(i[2])

all_lst = lst_1 + lst_2 + lst_3

filtered_all_lst = []

for i in all_lst: #clean from digits and spaces, leave only letters and special symbols
    if not i.isdigit() and i != ' ':
        filtered_all_lst.append(i)

filtered_all_lst_1 = []

for i in range(len(filtered_all_lst)): #clean from all special symbols which go after another special symbol
    if i < len(filtered_all_lst) - 1:
        next_element = filtered_all_lst[i + 1]
        if not filtered_all_lst[i].isalpha() and not next_element.isalpha():
                continue
        else:
            filtered_all_lst_1.append(filtered_all_lst[i])

for i in range(len(filtered_all_lst_1)): #replace single special symbols which left by spaces.
    if not filtered_all_lst_1[i].isalpha():
       filtered_all_lst_1[i] = " "

final_string = ''.join(filtered_all_lst_1)
print(final_string)




