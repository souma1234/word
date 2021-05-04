import random

x=[]
hal=[]
z=input("number of letters desired:  ")

for i in range(int(z)):
    
        y=input("please inter the letter: ")

        if y in x:
            print("letter exists already")
            break

        else:
                x.append(y)
    
for i in range(len(x)):
        s=random.choice(x)
        hal.append(s)

k=[''.join(hal[0:len(hal)])]

print(k)
