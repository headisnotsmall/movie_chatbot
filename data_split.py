import re

data_name = input("tsvfile name: ")

# tsv split

count = 0
with open(data_name + ".tsv", 'r', encoding='utf-8') as myfile:
    for line in myfile:
        count += 1
    print("data len:", count)


    i = 0
    s = 0
    sl = int(input("slice per elements: "))
    with open(data_name + ".tsv", 'r', encoding='utf-8') as myfile:
        for line in myfile:
            i += 1
            if i % sl == 0:
                s += 1
                print("saving data", s)
            with open(data_name + str(s) + ".csv", 'a', encoding='utf-8') as csv_file:
                fileContent = re.sub("\t", ",", line)
                csv_file.write(fileContent)