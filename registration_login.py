#--------------------------
#Registration and Login system using Python, file handling 

def choice_type():
    account_ans=""
    while True:
        account_ans=input("Type :  a > Registration     b > Login ")
        if account_ans=="a":
          username=registeration()
        elif account_ans=="b":
          login()
        else:
          break

def registeration():
    print("Registeration details: ")
    username = str(input("Username / Email Id: "))
    print("Password must be 5-16 charater ,one @#$&, one 0-9 , one A-Z ,one a-z")
    password = str(input("Password: "))
    f = open("User_Detail.txt",'r')
    user_detail = f.read()
    if username in user_detail:
        return "Username  alredy registered. Go for Login"
    f.close()
    f = open("User_Detail.txt",'w')
    user_detail = user_detail + " " +username + " " + password
    f.write(user_detail)

def login():
    print("Login details: ")
    username = str(input("Username: "))
    password = str(input("Password: "))
    f = open("User_Detail.txt",'r')
    user_detail = f.read()
    user_detail = user_detail.split()
    if username in user_detail:
        index = user_detail.index(username) + 1
        user_password = user_detail[index]
        if user_password == password:
            return "Welcome Back, " + username
        else:
            return "Password entered is wrong"
    else:
        return "Name not found. Please Sign Up for Registeration."

print(choice_type())
