import requests

def buscar_pokeson(nom):
    url = f"https://pokeapi.co/api/v2/pokemon/{nom.lower()}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dades = resposta.json()
        nom = dades['name']
        numero = dades['id']
        tipus = dades['types']
        habilitats = dades['abilities']
        imatge = dades['sprites']['front_default']

        print(f"\nNom: {nom}")
        print(f"Número Pokédex: {numero}")
        
        print("\nTipus:")
        for t in tipus:
            tipus_nom = t['type']['name']
            print(f"- {tipus_nom}")
        
        print("\nHabilitats:")
        for h in habilitats:
            habilitat = h['ability']['name']
            print(f"- {habilitat}")

        print(f"\nImatge: {imatge}")

    else:
        print("No s'ha trobat el nom d'aquest Pokémon.")

nom_pokemon = input("Introdueix el nom d'un Pokémon: ")
buscar_pokeson(nom_pokemon)
