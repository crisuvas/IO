my_list = [i ** 2 for i in range(1, 11)]

my_file = open("for.txt", "w")

for text in my_list:
    my_file.write(str(text) + "\n")

my_file.close()
