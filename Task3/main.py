print("Name: Jatin Kshatriya")
print("Enrollment no: 0108AI201024")
print("Scholar no: 30494")

from csv import reader

opened_file = open('Task3/AppleStore.csv', 'r', encoding='utf-8')
read_file = reader(opened_file)

apps_data = list(read_file)

#Task 1 of 3
# print(len(apps_data))
# print(apps_data[0]) 
# print(apps_data[1]) 
# print(apps_data[2]) 


#Task 2 of 3
my_data = apps_data[:5]

my_dataset = [i for i in my_data]
print(my_dataset)

for data in my_dataset:
    print(data)