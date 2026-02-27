print('HEllo,Word')

meme_dict = {
    "STALKEAR": "Investigar a vida de alguém online",
    "CRINGE": "Algo vergonhoso ou constrangedor",
    "VDD": "Abreviação da palavra 'verdade'",
    "BISCOITAR": "Postar algo apenas para chamar a atenção",
    "HATER": "Pessoa que está constantemente criticando os outros",
    "VLW": "Abreviação da palavra 'valeu'"
}

word = input("Digite uma palavra moderna que você não entende: ").upper()

if word in meme_dict:
    print(meme_dict[word])
else:
    print("Desculpe, essa palavra não tá no dicionário.")
