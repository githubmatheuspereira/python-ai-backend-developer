# Trabalhando com Branches

## O que é uma Branch?

- Simplificando, uma Branch é uma linha de desenvolvimento independente dentro do seu projeto. Ela é como um caminho separado de alterações que diverge do histórico principal do projeto.
- Cada Branch é um ponteiro móvel para um commit específico no histórico do repositório Git.
## Criando uma Branch

- Quando você cria uma nova Branch a partir de outra existente, a nova Branch começa apontando para o mesmo commit que a Branch original.
- Por exemplo, se estamos na Branch "main" e criamos uma nova Branch chamada "teste", a "teste" começará apontando para o mesmo commit que a "main".
## Trabalhando com Branches

- Cada vez que você faz um novo commit em uma Branch, o ponteiro dessa Branch avança para apontar para o novo commit.
- Isso significa que você pode fazer alterações, testes e experimentos em uma Branch sem afetar o código na Branch principal ou em outras Branches.
## Exemplo Prático:

- Imagine que estamos na Branch "main" com o commit 0. Neste ponto, a "main" aponta para o commit 0.
- Se fizermos um novo commit, a "main" avançará para apontar para o novo commit (por exemplo, commit 1).
- Agora, suponhamos que decidimos testar um novo recurso e criamos uma nova Branch chamada "teste". A "teste" começa apontando para o mesmo commit que a "main" (por exemplo, commit 0).
- Se fizermos um terceiro commit na Branch "teste", apenas a "teste" avançará para apontar para o novo commit, enquanto a "main" ainda permanecerá apontando para o commit 1.