from collections import Counter
items=[]
try:
    while True:
            name=input().strip().upper()
            items.append(name)

except EOFError:
    print()
    grocery=Counter(items)
    for item in sorted(grocery.keys()):
        print(grocery[item], item)


