import requests


def main():
    artwork = input("Artwork:")
    artworks = get_artowrks(query=artwork, limit=5)
    response = requests.get("https://api.artic.edu/api/v1/artworks/search")
    content = response.json()
    for artwork in content["data"]:
     print(f"$ {artwork['title']}")

def get_artowrks(query, limit):
   try: 
      response= response.get(
            "https://api.artic.edu/api/v1/artworks/search",
            params={"query": query, "limit": limit}
      )
      response.raise_for_status()
   except requests.HTTPError:
      return []
   
   content = response.json()
   return [artwork["title"] for artwork in content["data"]]


main()
