# Autenticação via Chave SSH no Git GitHub - Passo a Passo

## 1. Gere uma Chave SSH

- Abra o Terminal.
- Execute o seguinte comando para gerar uma nova chave SSH:
  ```bash
  ssh-keygen -t rsa -b 4096 -C "seu-email@example.com"
  ```
  Substitua `"seu-email@example.com"` pelo seu endereço de e-mail associado à sua conta do GitHub.
- Você será solicitado a escolher um local para salvar a chave. Pressione Enter para aceitar o local padrão (`~/.ssh/id_rsa`) ou especifique um local diferente, se desejar.
- Você também será solicitado a digitar uma frase secreta. Isso é opcional, mas pode adicionar uma camada extra de segurança.

## 2. Adicione sua Chave SSH à sua Conta do GitHub

- Copie o conteúdo da chave SSH pública. Você pode usar o comando `pbcopy` para copiá-lo diretamente para a área de transferência:
  ```bash
  pbcopy < ~/.ssh/id_rsa.pub
  ```
- Acesse o GitHub e faça login na sua conta.
- Clique na sua foto de perfil no canto superior direito e selecione "Settings".
- No menu lateral esquerdo, clique em "SSH and GPG keys".
- Clique em "New SSH key" ou "Add SSH key".
- Cole a chave SSH pública que você copiou anteriormente no campo "Key".
- Dê um título à sua chave SSH para identificá-la (opcional).
- Clique em "Add SSH key" para salvar a chave.

## 3. Teste sua Conexão SSH

- No Terminal, execute o seguinte comando para testar sua conexão SSH com o GitHub:
  ```bash
  ssh -T git@github.com
  ```
- Você pode receber uma mensagem de aviso sobre autenticidade do host. Digite `yes` para confirmar.
- Se tudo estiver configurado corretamente, você verá uma mensagem de confirmação indicando que você está autenticado com sucesso.

## 4. Use SSH ao Clonar ou Interagir com Repositórios do GitHub

- Ao clonar um repositório existente, use o URL SSH em vez do URL HTTPS:
  ```bash
  git clone git@github.com:usuario/repositorio.git
  ```
- Se você já tiver clonado um repositório usando HTTPS e desejar mudar para SSH, você pode mudar o URL remoto usando o seguinte comando:
  ```bash
  git remote set-url origin git@github.com:usuario/repositorio.git
  ```

## 5. Autenticação Concluída

- Agora você está autenticado no GitHub usando sua chave SSH. Todas as operações Git, como push, pull e clone, serão autenticadas automaticamente usando sua chave SSH.
- As chaves SSH oferecem uma forma segura e conveniente de autenticar com o GitHub, eliminando a necessidade de inserir suas credenciais a cada operação.

Lembre-se de proteger sua chave SSH privada e não compartilhá-la com ninguém. Ela oferece acesso à sua conta do GitHub e deve ser mantida em segurança.