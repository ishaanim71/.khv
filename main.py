with open("codingal.txt","w") as f:
     f.write("pokemon")
f.close()

with open("abc.txt","r") as f:
    data=f.readlines()
    print("Words in the file:")
    for line in data:
        word=line.split()
        print(word)
f.close()       

          