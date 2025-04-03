def main():
    miles =int(input("Enter the number of miles: "))
    minutes = int(input("Enter the number of minutes you have to finish: "))
    pace = get_pace(miles, minutes)
    print(f"you need to run each mile in {round(pace, 2)} minutes")



def get_pace(miles,minutes):
    if not minutes > 0:
        raise ValueError("Minutes must be greater than 0")
    return minutes / miles

main()