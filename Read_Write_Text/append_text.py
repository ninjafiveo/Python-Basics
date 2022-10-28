with open('Read_Write_Text\\append_me.txt', 'a') as f:
    note = input("Add a note: ")
    f.write(f'{note}\n')
    
# the above will overwrite the file.