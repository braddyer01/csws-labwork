users = ()
if len(users) == 0:
    print("We need to find more users!")
else:
    for x in users:
        if x == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello "+x)
