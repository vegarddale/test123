import os 
os.setuid(1000)
print(os.listdir("./"))
