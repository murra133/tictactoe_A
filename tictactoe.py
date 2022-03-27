
print("Hello World")

def display(arr):
    for x in arr:
        res = x[0]+"|"+x[1]+"|"+x[2]+"\n"
        bottom = "______\n"
        print(res)
        print(bottom)

#Add Change
#   y0,y1,y2
#x0[- ,- ,-]
#x1[- ,- ,-]
#x2[- ,- ,-]
l=0
k="O"
arr = [["-","-","-"],["-","-","-"],["-","-","-"]]
display(arr)
while(l < 3):
    
    x = int(input("Please input the X Value of your attack:"))
    y = int(input("Please input the Y Value of your attack:"))
    arr[x][y] = k
    display(arr)
    l=l+1
     
## Win Condition (A)

##Draw Conditions ()

#Modes 2 Players or 1 Player (A)

#Double Win ()

#Listener to not place item in already filled slot Ex. If X exists O cannot be placed (A)

# Listener to swap players ()