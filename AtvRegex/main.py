from src.Leitor import Leitor

def main():
    caminho = input(str("Qual a URL do arquivo?:"))
    leitor = Leitor(caminho)
    
    while True:
        #Print com opcões para o usuario escolher

        print(f"Menu\n {"-"*40}\n [1] Ler Arquivo \n [2] Filtrar Pela Letra Inicial \n [3] Filtrar Pela Letra \n [4] Substituir , Por . \n [5] Achar Datas \n [6] Censurar Conteudo \n [0] Sair")
        print("-"*40)
        opcao = input(str("O que você quer fazer?:"))
        
        if(opcao == "1"):
            #Se ele escolher a opção 1, abre o arquivo e manda ele lido
            print("-"*40)
            conteudo = leitor.abrir()
            print(conteudo)
            print("-"*40)
            
        elif(opcao == "2"):
            #Se ele escolher a opção 2, acha aas palavras pela letra escolhida na class pela letra inicial
            print("-"*40)
            print(leitor.FindFirstWord())
            print("-"*40)
            
        elif(opcao == "3"):
            #Se ele escolher a opção 3, acha as palavras pela letra escolhida na class em qualquer lugar
            print("-"*40)
            print(leitor.FindWord())
            print("-"*40)
            
        elif(opcao == "4"):
            #Se ele escolher a opção 4, substitui vigulas por pontos e printa
            print("-"*40)
            print(leitor.SubsWord())
            print("-"*40)
            
        elif(opcao == "5"):
            #Se ele escolher a opção 5, acha datas no texto e printa
            print("-"*40)
            print("Datas achadas:")
            print(leitor.Dates())
            print("-"*40)
            
        elif(opcao == "6"):
            #Se ele escolher a opção 6, bloqueia coisas sensiveis e printa o texto censurado
            print("-"*40)
            print("Texto censurado(CPF, Numero, Email):")
            print("-"*40)
            print(leitor.Hiden())
            print("-"*40)
            
        elif(opcao == "0"):
            #Se ele escolher a opção 0, sai do looping
            break
        
        else:
            print("Erro, escolha uma opção válida")

if __name__ == "__main__":
    main()