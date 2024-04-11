user = input("Enter your name : ")
password = input("Enter your password : ")

pwd_len = len(password)
pwd_hidden = '*' * pwd_len

print(f"Hey {user} your password {pwd_hidden} has the length of {pwd_len} ")