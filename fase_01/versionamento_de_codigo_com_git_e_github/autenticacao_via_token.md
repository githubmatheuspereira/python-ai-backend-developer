# Autenticação via Token Git GitHub - Passo a Passo

## 1. Crie um Token de Acesso Pessoal no GitHub

- Acesse o GitHub e faça login na sua conta.
- Clique na sua foto de perfil no canto superior direito e selecione "Settings".
- No menu lateral esquerdo, clique em "Developer settings" e depois em "Personal access tokens".
- Clique em "Generate new token".
- Dê um nome ao seu token, selecione as permissões necessárias (por exemplo, `repo` para acessar repositórios) e clique em "Generate token".
- Copie o token gerado. **Atenção**: Este token será exibido apenas uma vez. Certifique-se de copiá-lo e guardá-lo em um local seguro.

## 2. Configure o Token como sua Credencial Git

- Abra o Terminal.
- Configure o Git para usar seu token como credencial:
    ```bash
  git config --global credential.helper store
    Isso fará com que o Git armazene suas credenciais (nome de usuário e token) em cache em um arquivo de texto. Nota: Embora seja conveniente, armazenar suas credenciais em cache pode ser menos seguro em alguns casos. Você pode optar por usar outras formas de autenticação, como SSH, se preferir.

## 3. Faça um Push ou Clone de um Repositório
- Para um repositório já existente:
    ```bash
  git clone https://github.com/usuario/repositorio.git
    Quando solicitado, insira seu nome de usuário do GitHub e, como senha, cole o token de acesso pessoal que você gerou anteriormente.
- Para um novo repositório, faça um push do seu código para o repositório remoto:
    ```bash
    git remote add origin https://github.com/usuario/repositorio.git
    git branch -M main
    git push -u origin main
    Mais uma vez, quando solicitado, insira seu nome de usuário do GitHub e, como senha, cole o token de acesso pessoal.

## 4. Autenticação Concluída
- Agora o Git usará seu token de acesso pessoal para autenticar suas operações com o GitHub. Seu nome de usuário e token serão armazenados em cache e você não precisará inseri-los novamente para operações futuras, a menos que o token expire ou você limpe o cache de credenciais.
    Lembre-se de manter seu token de acesso pessoal seguro e não compartilhá-lo com ninguém. Ele oferece acesso à sua conta no GitHub e pode ser usado para realizar operações em seu nome. Se você acredita que seu token foi comprometido, você pode revogá-lo no GitHub e gerar um novo.
