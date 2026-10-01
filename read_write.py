# HW 7th, Reading and ZWriting to Files
 
with open("practice.txt", "r+") as file: #r+ lets you read and write and appending

    content = file.read() #to read the files
    content = "Chapter 1: \n" + content + "And Christopher Robin was sitting on his doorstep putting on his big boot."
    file.write(content)

with open("practice.txt", "a") as file:
    file.write("\n Winnie the Pooh and the Blustery Day")
