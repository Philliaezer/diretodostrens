import sys
import requests

# todos(futuro):
    # - separar linhas por metrô, trem, viamobilidade e viaquatro
    # - colorizar com colorama
        # diferenciar cores entre linhas e empresas
class Linhas:
    """
    Representa todas as linhas do transporte ferroviário paulista, suportadas pela API:
         
     https://www.diretodostrens.com.br/api
    """
    __lista = [
    "Azul","Verde","Vermelha",
    "Amarela", "Lilás","Rubi",
    "Diamante","Esmeralda", 
    "Turquesa", "Coral",
    "Safira", "Jade", "Prata"
     ]
     
    def __init__(self):
        self.dados = self.__api_request()
        self.nomes = self.lista()
        self.numeros = self.ver_nomes().keys
        self.status = False
    
    @classmethod
    def lista(cls):
        return cls.__lista
        
    def estado(self, escrever: bool=False):
        valores = ""
        
        for data in self.dados:
            valores += ("="*10)+"\n"
            for key, value in data.items():
                valores += f"{key}: {value}\n"
                
        if not escrever:
            return valores
        print(valores)
            
    def ver_nomes(self) -> dict:
        return  {
        str(dados["codigo"]): 
        self.nomes[indice]
            for indice, dados in 
            enumerate(self.dados)
        }
    
    def codigos() -> list:
        """
        Retorna uma lista com todos os números das linhas
        
        :return: Lista
        """
        return [ infos["codigo"] for infos in self.dados]
        
    def geral():
        """
        Exibe o estado das linhas.
        Se todas estiverem em Operação Normal, retornará True
        Mas, se tiver pelo menos uma linha com estado anormal, será mostrado a situação dela(s) em formato string.
        
        :return: Bool ou string
        """
        for i in self.dados:
            if not "Operação Normal" in i.situacao:
                 return True
        return False
        
    def __api_request(self) -> dict:
        """
        Método privado para fazer requisições a API
        
        :return: JSON com todos os dados retornados
        """
        try:
            resposta = requests.get("https://www.diretodostrens.com.br/api/status")
            if resposta.status_code == 200:
                return resposta.json()
            return {None: None}
        except requests.exceptions.ConnectionError:
            print("Sem conexão!")
            
            sys.exit()
        
class Linha(Linhas):
    """
    Representa uma linha dentre as 13 existentes
    """
    def __init__(self, nome):
        super().__init__()
        self.nome = nome if nome in self.nomes else None
        self.numero = 8
        self.status = "status"
        self.situacao = "normal"
        
    def status():
        """
        Retorna o estado apenas da linha referenciada no atributo :attr:`nome`
        
        :return: Booleano
        """
        return self.status
        
    @property
    def numero(self):
        return self._numero
        
    @numero.setter
    def numero(self, valor):
        self._numero = valor+1