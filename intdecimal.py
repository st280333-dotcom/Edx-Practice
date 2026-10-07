num=float(input("Enter the value:"))
value=int(input("If you want integer value type 1 or deminal then type 2 :"))

if value==1:
    print(int(num))
elif value==2:
    deci=(num-int(num))
    print(f"{deci:.2f}")    
else:
    print("The Number Doesn't exist")    