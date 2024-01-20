meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobación",
            "CREEPY": "Aterrador o siniestro",
            "AGGRO": "Ponerse agresivo o enojado",
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(f"Esta es el significado de {word} , {meme_dict[word]}")
else:
    print("Losiento, esta palabra no ha sido encontrada")
