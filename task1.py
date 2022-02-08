users = ("admin","user1","user2","user3","user4")
for x in users:
    if x == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello "+x)
