
print("Hello World")

def display(arr):
    for x in arr:
        res = x[0]+"|"+x[1]+"|"+x[2]+"\n"
        bottom = "______\n"
        print(res)
        print(bottom)

#Add Change
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
     
