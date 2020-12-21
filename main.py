list_1 = []  
list_2 = []  


with open("file1.txt", "r") as names_file:
    file_1_data = names_file.readlines()  


with open("file2.txt", "r") as names_file:
    file_2_data = names_file.readlines()  


result = [int(num) for num in file_1_data if num in file_2_data]

# Write your code above 👆

print(result)


