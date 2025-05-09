from .dados import *
        
lines = Linha("Diamante")
json = lines.dados

lines.estado(True)

"""
for data in json:
    print ("="*10)
    for key, value in data.items():
        string_estado= f"{key}: {value}"
        print(string_estado)
"""
linhas = lines.ver_nomes()

print(linhas)

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

print(
da_linha("Diamante"))
print(da_linha(7))
print(lines.numero)
print(lines.nome)
