distances = {
    "voyager 1": 163,
    "voyager 2": 138,
    "new horizons": 44,
    "cassini": 1.2,
    "pioneer 10": 132,
    "pioneer 11": 105,
}


def main():
    for spacecraft, distance in distances.items():
        print(f"{spacecraft} is {distance} AU from the sun, which is {convert(distance)} km")

def convert(au):
    return au * 149597871

main()