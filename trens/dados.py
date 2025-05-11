import sys
import requests
from typing import Optional, Union

# todos(futuro):
    # - colorizar com colorama
        # diferenciar cores entre linhas e empresas
    # utilitário cli (poder importar trens.cli)
class Linhas:
    """
    Representa todas as linhas do transporte ferroviário paulista, suportadas pela API:
         
     https://www.diretodostrens.com.br/api
    """
    
    __lista = {
        1: "Azul", 2: "Verde",
        3: "Vermelha",
        4: "Amarela", 5: "Lilás",
        7: "Rubi", 8: "Diamante",
        9: "Esmeralda", 
        10: "Turquesa", 
        11: "Coral", 12: "Safira", 
        13: "Jade", 15: "Prata"
    }
     
    def __init__(self):
        self.dados = self.__api_request()
        self.nomes = self.lista()
        self.numeros = self.ver_nomes().keys
    
    def _get(self, keys):
        return { k: v for k, v in self.lista().items() if k in keys }
    
    @classmethod
    def lista(cls) -> dict[int, str]:
        return cls.__lista
        
    def geral(self, escrever: bool=False) -> Optional[str]:
        """
        Retorna (ou imprime) a situação de todas as linhas retornadas pela API
        :param escrever: Deve retornar, ou printar o conteúdo?
        
        :return: string
        """
        valores = ""
        
        for data in self.dados:
            valores += ("="*10)+"\n"
            for key, value in data.items():
                valores += f"{key}: {value}\n"
                
        if not escrever:
            return valores
        print(valores)
            
    def teste(self) -> int:
        return 2
        
    def ver_nomes(self) -> dict[int, str]:
        """
        Retorna um dicionário com todas as linhas e seus códigos
        """
        return self.nomes
    
    def codigos() -> list[str]:
        """
        Retorna uma lista com todos os números das linhas
        
        :return: Lista
        """
        return [ infos["codigo"] for infos in self.dados]
        
    def estado(self) -> Union[bool, list[str]]:
        """
        Exibe o estado das linhas.
        Se todas estiverem em Operação Normal, retornará True
        Mas, se tiver pelo menos uma linha com estado anormal, será mostrado a situação dela(s) em formato string.
        
        :return: Bool ou string
        """
        anormais = []
        for i in self.dados:
            if not "Operação Normal" in i["situacao"]:
                 anormais += [i]
        return True if not anormais else anormais
        
    def __api_request(self) -> dict[Union[int, str, None], Optional[str]]:
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
    def __init__(self, nome: Union[str, int]):
        super().__init__()
        self.nome = nome
        self.numero = None
        
    def teste(self) -> int:
        # Todo: remover
        return 1
        
    def estado(self, booleano: bool=False) -> Union[bool, str, None]:
        """
        Retorna o estado apenas da linha referenciada no atributo :attr:`nome`
        
        :return: Booleano
        """
        if not self.nome == None:
            st = next((x for x in self.dados if x["codigo"] == self.numero), None)
            if booleano:
                if st["situacao"] == "Operação Normal":
                    return True
                return False
            return st
        return None
        
    @property
    def numero(self) -> Optional[int]:
        return self._numero
        
    @numero.setter
    def numero(self, valor: Optional[int]):
        self._numero = next((int(k) for k, v in self.ver_nomes().items() if v == self.nome), None)
        
    @property
    def nome(self) -> str:
        return self._name
        
    @nome.setter
    def nome(self, valor: Union[str, int]):
        if str(valor).isnumeric():
            valores = self.nomes.keys()
            valor = self.nomes[int(valor)] if valor in valores else None             
         
        valores = self.nomes.values()
        
        self._name = ( valor 
        if valor in valores
            else None )

class Empresa(Linhas):
    """
    Representa uma das quatro concessionárias de transporte ferroviário paulista
    """
    
    __empresas = ["CPTM", "METRO", "VIAQUATRO", "VIAMOBILIDADE"]
    
    def __init__(self, empresa):
        super().__init__()
        self.nome = empresa
        self.__cptm = self._get([7, 10, 11, 12, 13])
        self.__metro = self._get([1, 2, 3, 15])
        self.__viaquatro = self._get([4])
        self.__viamobilidade = self._get([5, 8, 9])
        self.__todos = [
            self.__cptm, self.__metro,
            self.__viaquatro, self.__viamobilidade
        ]
        
    @property
    def nome(self) -> Optional[str]:
        return self._companhia
        
    @nome.setter
    def nome(self, valor: Optional[str]):
        self._companhia = valor if valor.upper() in self.__empresas else None
        
    @classmethod
    def empresas(cls):
        return cls.__empresas
        
    def estado(self, booleano: bool=False) -> Union[bool, str, None]:
        """
        Retorna o estado apenas das linhas concessionadas pela empresa referenciada no atributo :attr:`nome`
        
        :return: Booleano
        """
        
        if not self.nome == None:
            empresa = self.__set_empresa()
            st = [ x for x in self.dados if x["codigo"] in empresa.keys() ]
            if booleano:
                for stt in st:
                    if stt["situacao"] == "Operação Normal":
                        return True
                return False
            return st
        return None
        
    def __set_empresa(self):
        if not self.nome == None:
            for i, empresa in enumerate(self.empresas()):
                if self.nome.upper() == empresa:
                    return self.__todos[i]
        return None
        
class Zona(Linhas):
    """
    Representa uma das quatro regiões metropolitanas de São Paulo
    """
    
    __zonas = ["NORTE", "SUL", "LESTE", "OESTE"]
    
    def __init__(self, regiao):
        super().__init__()
        self.regiao = regiao
        
        self.__norte = self._get([1, 7, 13])
        self.__sul = self._get([1, 4, 5, 9, 10])
        self.__leste = self._get([2, 3, 10, 11, 12, 13])
        self.__oeste = self._get([7, 8, 9])
        self.__todos = [
            self.__norte, self.__sul,
            self.__leste, self.__oeste
        ]
        
    @property
    def regiao(self) -> Optional[str]:
        return self._local
        
    @regiao.setter
    def regiao(self, valor: Optional[str]):
        self._local = valor if valor.upper() in self.__zonas else None
        
    @classmethod
    def regioes(cls):
        return cls.__zonas
    
    def estado(self, booleano: bool=False) -> Union[bool, str, None]:
        """
        Retorna o estado apenas da zona referenciada no atributo :attr:`regiao`
        
        :return: Booleano
        """
        
        if not self.regiao == None:
            regiao = self.__set_regiao()
            st = [ x for x in self.dados if x["codigo"] in regiao.keys() ]
            if booleano:
                for stt in st:
                    if stt["situacao"] == "Operação Normal":
                        return True
                return False
            return st
        return None
        
    def __set_regiao(self):
        if not self.regiao == None:
            for i, regiao in enumerate(self.regioes()):
                if self.regiao.upper() == regiao:
                    return self.__todos[i]
        return None