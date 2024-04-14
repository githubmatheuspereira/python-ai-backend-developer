"""
Objetivo Geral:
Entender o que são e como utilizar variáveis e constantes.

Etapa 1 - O que são variáveis constantes?
Etapa 2 - Boas práticas.

Variáveis
Em linguagens de programação, variáveis são valores que podem sofrer alterações no decorrer da execução do programa.

Constantes
Assim como as variáveis, constantes são utilizadas para armazenar valores. Uma constante nasce com um valor e permanece com ele até o final da execução do programa, ou seja, o valor é imutável.

Python não tem constantes
Não eciste uma palavra reservada para informar ao interpretador que o valor é constante. Em algumas linguagens por exemplo: Java e C utilizamos final e const, respectivamente para declarar uma constante.
Em Python, usamos a convenção que diz ao programador que a variável é uma constante. Para isso, você deve criar a variável com o nome todo em letras maíusculas.

DEBUG = True
States = [
'SP',
'RJ',
'MG',
]

Boas práticas
- O padrão de nomes deve ser snake case.
- Escolher nomes sugestivos.
- Nome de constantes todo em maiúsculo.
"""
nome = "Matheus"
idade = 72
nome, idade = "Pereira", 46
print(nome, idade)

limite_saque_diario = 1000

BRAZILIAN_STATES = ["SP", "MG", "RJ"]
print(BRAZILIAN_STATES)