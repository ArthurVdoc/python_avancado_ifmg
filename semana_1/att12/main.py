
def cadastra_candidatos(dicCandidates):
    while True:
        try:
            numCandidates = int(input("Quantos candidatos quer cadastrar?").strip())
            break
        except ValueError:
            print("Número inválido.")
            continue

    for i in range(numCandidates):
        while True:
            numero = input(f"insira o número do {i+1}° candidato: ").strip()
            if numero.isdigit():
                nome=input("insira o nome do candidato: ").strip()
                break
            else:
                print("Número inválido. Por favor, insira um número válido.")
                continue
        dicCandidates[numero] = nome


def votação(dicCandidates, dicVotes, vBrancos, vNulos):
    for numero in dicCandidates.keys():
        dicVotes[numero] = 0
    while True:
        voto = input("Insira o número do candidato que deseja votar:").strip()
        if voto == "":
            vBrancos += 1
            print("Voto em branco computado com sucesso!")
        else:
            votoNulo = True
            for numero in dicCandidates.keys():
                if voto == numero:
                    votoNulo = False
                    while True:
                        confirmação = input(f"Confirmar voto em\nCandidato: {dicCandidates[numero]}\nNúmero: {numero}\n(CONFIRMAR): ").strip()
                        if confirmação.lower() == "confirmar":
                            dicVotes[numero] += 1
                            print("Voto computado com sucesso!")
                            break
                        else:
                            continue
            if votoNulo:
                print("Voto anulado!")
                vNulos += 1
        continuar = input("Registrar mais um voto? (s)").strip()
        if continuar.lower() == 's':
            continue
        else:
            break
    return dicVotes, vBrancos, vNulos


def resultado_votação(dicCandidates, dicVotes, vBrancos, vNulos):

    dicPercentuais = {}
    print("\n----- Resultado Preliminar -----")
    for numero, nome in dicCandidates.items():
        print(f"Candidato {nome} (Número {numero}): {dicVotes[numero]} votos")
    print(f"Votos em branco: {vBrancos}")
    print(f"Votos nulos: {vNulos}")

    maiorvoto = 0
    maisvotado = None
    for numero in dicVotes.keys():
        if dicVotes[numero] > maiorvoto:
            maisvotado = numero
            maiorvoto = dicVotes[numero]
    dicVotes[maisvotado] = maiorvoto + vBrancos

    totalVotos = sum(dicVotes.values()) + vBrancos + vNulos
    for numero, votos in dicVotes.items():
        percentual = (votos / totalVotos) * 100 if totalVotos > 0 else 0
        dicPercentuais[numero] = percentual
    percentual_nulos = (vNulos / totalVotos) * 100 if totalVotos > 0 else 0
    
    
    print("\n----- Resultado Final -----")
    for numero, nome in dicCandidates.items():
        print("\n\nCandidato:", nome, 
              "\nNúmero:", numero, 
              "\nVotos:", dicVotes[numero], 
              "\nPercentual de votos:", f"{dicPercentuais[numero]:.2f}%")
    print("\nVotos nulos:", vNulos)
    print("Percentual de votos nulos:", f"{percentual_nulos:.2f}%")
    
    print("\n----- Vencedor -----")
    print("Candidato:", dicCandidates[maisvotado], 
          "\nNúmero:", maisvotado, 
          "\nVotos:", dicVotes[maisvotado], 
          "\nPercentual de votos:", f"{dicPercentuais[maisvotado]:.2f}%")
    

def main():
    dicCandidates = {}
    print("Deseja cadastrar candidatos? (s)")
    try:
        if input().lower().strip() == 's':
            cadastra_candidatos(dicCandidates)
            print("Candidatos cadastrados:")
            for numero, nome in dicCandidates.items():
                print(f"{nome} (Número {numero})")
        else:
            print("Nenhum candidato cadastrado.")
    except Exception as e:
        print(f"Erro ao cadastrar candidatos: {e}")
    
    print("Iniciando Votação!")
    dicVotes = {}
    vBrancos = 0
    vNulos = 0
    dicVotes, vBrancos, vNulos = votação(dicCandidates, dicVotes, vBrancos, vNulos)
    resultado_votação(dicCandidates, dicVotes, vBrancos, vNulos)
    

if __name__ == "__main__":
    main()