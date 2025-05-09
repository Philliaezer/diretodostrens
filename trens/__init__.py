from .dados import *
        
lines = Linha("Diamante")
json = lines.dados

lines.geral(True)

linhas = lines.ver_nomes()

#todo: 
    # - remover
    # - ou servir de alias para um método da classe Linha
    # - ou ser mais otimizado
def da_linha(valor, completo=True, verboso=True):
    valor = str(valor)
    linhas = lines.ver_nomes()
    
    if valor.isnumeric():
        if valor in linhas.keys():
            if verboso:
                print("Numero da linha encontrado")
            if completo:
                return [y for y in filter(
                lambda x: True 
                    if x["codigo"] == int(valor) 
                else False, json
                )]
            return linhas[valor]
        else:
            return "Número da linha inválido"
    elif valor in linhas.values():
        if verboso:
            print("Nome encontrado")
        nome=next((k for k, v in linhas.items() if v == valor), None)
        return nome
    else:
        return "Nome da linha inválido"

print('== Função "da_linha" ==')
print(
da_linha("Diamante"))
print(da_linha(7))

print('Instancia da Classe "Linha"')
print(f"Linhas: {linhas}")
print(lines.numero)
print(lines.nome)
