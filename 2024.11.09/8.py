file = input().strip().split('; ')

count = {}
new_file = []

for i in file:
    if i in count:
        count[i] += 1
        new_name = f"{i.rsplit('.', 1)[0]}_{count[i]}{'.' + i.rsplit('.', 1)[-1] if '.' in i else ''}"
        new_file.append(new_name)
    else:
        count[i] = 1
        new_file.append(i)

p = new_file.sort()
for name in p:
    print(name)
    
# 1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar.gz
# 1.py
# 1_2.py
# 1_3.py
# src.tar.gz
# src_2.tar.gz
# aux.h
# main.cpp
# main_2.cpp
# main_3.cpp
# functions.h