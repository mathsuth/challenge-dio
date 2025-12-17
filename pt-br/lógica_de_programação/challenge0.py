def ranking_do_heroi(poder):
    if poder <= 1000:
        return "Ferro"
    elif poder >= 1001 and  poder <= 2000:
        return "Bronze"
    elif poder >= 2001 and poder <= 5000:
        return "Prata"
    elif poder >= 5001 and poder <= 7000:  
        return "Ouro"
    elif poder >= 7001 and poder <= 8000:
        return "Platina"
    elif poder >= 8001 and poder <= 9000:
        return "Ascendente"
    elif poder >= 9001 and poder <= 10000:
        return "Imortal"
    elif poder > 10000:
        return "Radiante"

while True:
    heroi = input("Digite o nome do herói: ")
    poder = int(input("Digite o xp do herói: "))
    print("O herói", heroi, "possui o nivel", ranking_do_heroi(poder))
    prosseguir = input("Deseja colocar mais outro herói? (s/n): ")
    if prosseguir != 's':
        break
