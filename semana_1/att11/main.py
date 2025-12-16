
def lista_de_funcionários():
    funcionarios = []
    print("Deseja inserir os funcionários? (s/n)")
    resposta = input().strip().lower()
    try:
        if resposta == 's':
            print("Digite a quantidade de funcionários a serem inseridos:")
            rangeLista = int(input().strip())
            for i in range(rangeLista):
                funcionario = dados_funcionário(indice=i+1)
                funcionarios.append(funcionario)
            
        elif resposta == 'n':
            print("Lista de funcionários encerrada.")
        
        else:
            print("Resposta inválida. Por favor, responda com 's' ou 'n'.")
            lista_de_funcionários()

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    
    return funcionarios

def dados_funcionário(indice):

    print(f"Digite o nome do funcionário {indice}:")
    nome = input().strip()

    print(f"Digite o salário do funcionário {indice}:")
    try:
        salario = float(input().strip())
    except ValueError:
        print("Salário inválido. Por favor, insira um número.")
        return dados_funcionário(indice)
    salario = round(salario, 2)

    funcionario = (nome, salario)
    
    return funcionario

def atualizar_salarios(funcionarios):
    funcionariosAtualizados = []
    for funcionario in funcionarios:
        nome, salario = funcionario
        if salario <= 2000:
            novoSalario = salario*1.2
        elif salario > 2000 and salario <= 5000:
            novoSalario = salario*1.15
        elif salario > 5000:
            novoSalario = salario*1.05
        novoSalario = round(novoSalario, 2)

        novoFuncionario = (nome, novoSalario)

        funcionariosAtualizados.append(novoFuncionario)
    return funcionariosAtualizados

def calcular_aumento(funcionariosOrig, funcionariosAtl):
    aumento = 0
    for i in range(len(funcionariosOrig)):
        nomeOrig, salarioOrig = funcionariosOrig[i]
        nomeAtl, salarioAtl = funcionariosAtl[i]
        aumento += salarioAtl - salarioOrig
    return aumento

def listar_pobres(funcionarios):
    pobres = []
    for funcionario in funcionarios:
        nome, salario = funcionario
        if salario < 2000:
            pobres.append(funcionario)
    return pobres

def main():
    funcOrig = lista_de_funcionários()
    funcAtl = atualizar_salarios(funcOrig)
    aumento = calcular_aumento(funcOrig, funcAtl)
    aumento = round(aumento, 2)
    pobres = listar_pobres(funcAtl)

    print("O aumento total foi de: R$", aumento)
    print("Lista de funcionários com salário abaixo de R$2000 após o reajuste:")
    for pobre in pobres:
        nome, salario = pobre
        print(f"Nome: {nome}, Salário: R$ {salario}")

if __name__ == "__main__":
    main()
    