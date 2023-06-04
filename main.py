import os

#Current Directory
print(os.getcwd())

#Changing  Directory
dir = os.chdir(r"D:\img_txt")
print(os.getcwd())

#Creating seperate directories for images and text files
os.mkdir(r"D:\imgs")
os.mkdir(r"D:\text")

#List of elements in the current directory
files = os.listdir(dir)

#Loop to move the files to their respective directories
for i in files:
    #IMAGES
    if '.jpg' in i:
        print(i)
        destination = r"D:\imgs"
        source_joined = os.path.join(os.getcwd(),i)
        destination_joined = os.path.join(destination, i)
        os.rename(source_joined, destination_joined)
    #TEXT FILES
    elif '.txt' in i:
        print(i)
        destination = r"D:\text"
        source_joined = os.path.join(os.getcwd(), i)
        destination_joined = os.path.join(destination, i)
        os.rename(source_joined, destination_joined)
    else:
        continue