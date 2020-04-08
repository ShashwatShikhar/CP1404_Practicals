name = input("Enter your name: ")
write_in_file = open('name.txt', 'w')
print(name,file=write_in_file)

write_in_file = open('name.txt', 'r')
print("Your name is "+ write_in_file.readline())
write_in_file.close

write_in_file1 = open('numbers.txt', 'r')
print("Sum of first two numbers in numbers.txt: "+str(int(write_in_file1.readline()) + int(write_in_file1.readline())))

sum = 0
write_in_file1 = open('numbers.txt', 'r')
for x in write_in_file1:
    sum = sum+int(x)
print("Sum of all numbers in numbers.txt: "+str(sum))

write_in_file1.close



