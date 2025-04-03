def main(): 
    spacecraft = {"name": "Voyager", 
                  "distance": "18 billion km", 
                  "speed": "17 km/s", 
                  "fuel": "100 kg", 
                  "crew": "3"}
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ==================== REPORT ====================

    Name: {spacecraft["name"]}
    Distance : {spacecraft["distance"]}
    Speed    : {spacecraft["speed"]}
    Fuel     : {spacecraft["fuel"]}
    Crew     : {spacecraft["crew"]}
    ================================================
    """

main()