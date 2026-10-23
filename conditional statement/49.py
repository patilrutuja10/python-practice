percentage=int(input("enter your percentage"))
match percentage:
    case "90":
        print("result status:destination")
    case "80":
        print("result status:A Grade")
    case "70":
        print("result status:B Grade")
    case "60":
        print("result status:C Grade")
    case "others":
        print("result status:Fail")                