import re

data_name = input("tsvfile name: ")

# tsv2csv

# def tsv2csv(data_name):
#   with open(data_name + ".tsv", 'r', encoding='utf-8') as myfile:
#     with open(data_name + ".csv", 'w', encoding='utf-8') as csv_file:
#       for line in myfile:
#           fileContent = re.sub("\t", ",", line)
#           csv_file.write(fileContent)