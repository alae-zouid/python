import requests

def obtenir_info_anime(nom_introd):
    url = f"https://api.jikan.moe/v4/anime?q={nom_introd.lower()}"
    resposta_api = requests.get(url)

    if resposta_api.status_code == 200:
        dades_anime = resposta_api.json()
        primer_anime = dades_anime['data'][0]

        titol = primer_anime['title']
        print(f"\nTítol: {titol}")

        sinopsis = primer_anime['synopsis']
        print(f"\nSinopsis:\n{sinopsis}")
        
        puntuacio = primer_anime['score']
        print("\nPuntuació:")
        print(f"- {puntuacio}")

        episodis = primer_anime['episodes']
        print("\nEpisodis:")
        print(f"- {episodis}")

        url_anime = primer_anime['url']
        print("\nURL:")
        print(f"- {url_anime}")

        with open("anime_info.json", "w", encoding="utf-8") as fitxer:
            fitxer.write("{\n")
            fitxer.write(f'  "titol": "{titol}",\n')
            fitxer.write(f'  "sinopsis": "{sinopsis}",\n')
            fitxer.write(f'  "puntuacio": "{puntuacio}",\n')
            fitxer.write(f'  "episodis": "{episodis}",\n')
            fitxer.write(f'  "url": "{url_anime}"\n')
            fitxer.write("}")

    else:
        print("Hi ha alguna cosa que no està bé")

nom_usuari = input("Introdueix el nom d’un anime: ")
obtenir_info_anime(nom_usuari)
