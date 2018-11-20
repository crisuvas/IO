write_file = open("text.txt", "w")
write_file.write("Not closing files is VERY BAD")
write_file.close()

read_file = open("text.txt", "r")
print(read_file.read())
read_file.close()
