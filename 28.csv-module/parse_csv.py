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

# with open('new_csv.csv', 'r') as csv_file:
#     # csv_reader = csv.reader(csv_file)
#     csv_reader = csv.reader(csv_file, delimiter='\t')

#     for line in csv_reader:
#         print(line)

# with open('random_csv.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     # print(csv_reader)
#     for line in csv_reader:
#         # print(line)
#         print(line['Period'])


with open('random_csv.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_csv.csv', 'w') as new_file:
        fieldnames = ['Series_reference','Period','Data_value','Suppressed','STATUS','UNITS','Magnitude','Subject','Group','Series_title_1','Series_title_2','Series_title_3','Series_title_4','Series_title_5']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        
        for line in csv_reader:
            csv_writer.writerow(line)