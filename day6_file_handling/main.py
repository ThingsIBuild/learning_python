import os
# create new file
f = open('example.txt','w')
f.write('hello world')
f.close()


# method 2
with open('hello.txt','w') as f:

    f.write('Hello world 2')
    
    
# read file

f = open('example.txt','r')
content = f.read()
print(content)


with open('example.txt','r') as f:
    content = f.read()
    print(content)
    
    
# append to file
f = open('example.txt','a')
f.write('\nThis is an appended line.')
f.close()

with open('example.txt','a') as f:
    f.write('\nThis is an appended line.')
    

# delete file 

if os.path.exists("example.txt"):
    os.remove("example.txt")
    print("File deleted")
else:
    print('file not found')
    
    

# create folder dynamically

if not os.path.exists('new_folder'):
    os.makedirs('new_folder')
    print("Folder created")
  
else:
    print("Folder already exists")  
    