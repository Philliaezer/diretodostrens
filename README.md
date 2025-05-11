# Direto dos Trens API

Essa biblioteca em python utiliza a seguinte API REST:
 
https://static.diretodostrens.com.br/swagger/

Para obter informações sobre o estado das linhas de trem da região metropolitana de São Paulo.

Obrigado ao [@CTassisF](https://github.com/CTassisF) pela API pública :)

> [!NOTE]
> Esse projeto está em fase beta – ainda que sem Semver, porém já acho que faz sentido chama-lo assim.
>
> Ele está disponível no PyPI! Digite no seu terminal:
    
```sh
$ pip install diretodostrens
```

## Usos:
    
```python
from trens.dados import Linha, Zona, Empresa

diamante = Linha("Diamante")
# ou
esmeralda = Linha(9)

print(diamante.estado())
print(esmeralda.estado())

# também é possível ver os dados da região
oeste = Zona("Oeste")
print(oeste.estado())

# ... E da concessionária
cptm = Empresa("CPTM")
print(cptm.estado())
```