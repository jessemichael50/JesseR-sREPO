name = input("What's your name? ")

match name:
    case "harry":
        print("Gryffindor")
    case "hermione":
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case "luna":
        print("Ravenclaw")
    case "cedric":
        print("Hufflepuff")
    case _:
        print("I don't know you")
