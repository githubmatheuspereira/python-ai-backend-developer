"""
Objetivo Geral:
Aprender como receber e exibir informações para o usuário.

Etapa 1 - Lendo valores com a função input
Etapa 2 - Exibindo valores com a função print

Função input:
É ultilizada quando queremos ler dados da entrada padrão (teclado). Ela recebe um argumento do tipo String, que é exibido para o usuário na saída padrão (tela). A função lê a entrada, converte para string e retorna o valor.

Função print:
É ultilizada quando queremos exibir dados na saída padrão (tela). Ela recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.

"""

nome = input("Informe o seu nome: ");
idade = input("Informe a sua idade: ")

print(nome, idade)
print(nome, idade, end="...\n")