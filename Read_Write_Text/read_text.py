read_text = open("Read_Write_Text\\read_me.txt", 'r')

print(read_text.read())

#read(size) – read some contents of a file based on the optional size and return the contents as a string. If you omit the size, the read() method reads from where it left off till the end of the file. If the end of a file has been reached, the read() method returns an empty string.
#readline() – read a single line from a text file and return the line as a string. If the end of a file has been reached, the readline() returns an empty string.
#readlines() – read all the lines of the text file into a list of strings. This method is useful if you have a small file and you want to manipulate the whole text of that file.

read_text.close()

# The following automatically closes the file for you. "with open" auto closes the file when done.

with open("Read_Write_Text\\read_me.txt", 'r') as the_file:
    contents = the_file.readlines()
    print(f'the contents {contents}')

read_text_2 = open("Read_Write_Text\\read_me.txt", 'r')
contents_2 = read_text_2.readlines()
for i in contents_2:
    print(i)
    print("Next")