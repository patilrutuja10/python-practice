purpose=input("enter the purpose of visiting(login,registration,see website visited):")
match purpose:
    case "login":
        print("user")
    case "registration":
        print("guest")
    case "see website visited":
        print("admin")         
