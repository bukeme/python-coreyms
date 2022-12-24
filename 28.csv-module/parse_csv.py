import csv

# with open('random_csv.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     # print(csv_reader)
#     for line in csv_reader:
#         print(line)
#         print(line[2])


# with open('random_csv.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     with open('new_csv.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')
        
#         for line in csv_reader:
#             csv_writer.writerow(line)

with open('new_csv.csv', 'r') as csv_file:
    # csv_reader = csv.reader(csv_file)
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line)