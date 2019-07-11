import sys


args = sys.argv[1:]
print(args)


def greet_users(usernames):
    for name in usernames:
        print("Hello, "+name[0].upper()+name[1:]+"!")


greet_users(args)