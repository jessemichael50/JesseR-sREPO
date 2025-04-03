def main():
    x = get_int()
    print(f"x is {x}")



def get_int():
    while True:
        try:
            x = int(input("what's X?"))
        except ValueError:
            print("X must be a number")
        else: 
            return x

main()