greeting=input("Type Greeting..")
wish=greeting.lower().strip()
if "hello" in wish:
    print("$0")
elif wish.startswith("h"):
    print("$20")
else:
    print("$100")


