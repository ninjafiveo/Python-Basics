with open('Read_Write_Text\write_me.txt', 'w') as f:
    note = input("Write Something: \n")
    f.write(f'{note}\n')
    
# the above will overwrite the file.