import regex as re

class Leitor:
    """Classe com o caminho definido no main, dunther metodo"""
    def __init__(self, caminho: str):
        self.caminho = caminho
        
    
    """Abre o arquivo pelo caminho, lê ele, e manda a str dele lido"""
    def abrir(self) -> str:
        with open(self.caminho, "r", encoding="UTF-8") as arquivo:
            return arquivo.read()
        
    """Acha a palavra pela letra inicial ignorando maiusculo e minusculo, junta numa lista, e  manda"""
    def FindFirstWord(self) -> list[str]:
        letra = input(str("Qual letra você quer achar?:"))
        conteudo = self.abrir()
        config = rf'\b{letra}\w*'
        palavras = re.findall(config, conteudo, re.IGNORECASE)
        return palavras
    
    """Acha a palavra pela letra, independente de onde esteja, ignorando se é maiusculo ou minusculo"""
    def FindWord(self) -> list[str]:
        letra = input(str("Qual letra você quer achar?:"))
        print("-"*40)
        conteudo = self.abrir()
        config = rf'\w*{letra}\w*'
        palavras = re.findall(config, conteudo, re.IGNORECASE)
        return palavras
    
    """substitui , por . e manda ele corrigido"""
    def SubsWord(self) -> str:
        print("-"*40)
        conteudo = self.abrir()
        texto = re.sub(r",",".", conteudo)
        return texto
    
    """acha datas no texto e manda elas"""
    def Dates(self) -> list[str]:
        print("-"*40)
        conteudo = self.abrir()
        config = r'\b\d{2}[\/\-\.]\d{2}[\/\-\.]\d{4}\b'
        datas = re.findall(config, conteudo)
        return datas
    
    """Esconde emails, numeros e cpfs no texto e retorna ele corrigido"""
    def Hiden(self) -> str:
        print("-"*40)
        conteudo = self.abrir()
        
        telefone = r'(\(?\d{2}\)?\s?\d{4,5}[-\s]?\d{4})'
        email = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        cpf = r'\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b'

        conteudo = re.sub(telefone, "(Conteudo Restrito)", conteudo)
        conteudo = re.sub(email, "(Conteudo Restrito)", conteudo)
        conteudo = re.sub(cpf, "(Conteudo Restrito)", conteudo)
        
        return conteudo
