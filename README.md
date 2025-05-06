# 🏦 Projeto Validador de Cartão de Crédito

Este projeto em Python permite validar números de cartões de crédito e identificar sua bandeira com base em padrões predefinidos.

## 📌 Passo a passo para utilizar o projeto

### 1️⃣ **Instalar o Python**
Caso ainda não tenha Python instalado, baixe e instale a versão mais recente através do site oficial:

🔗 [Download Python](https://www.python.org/downloads/)

---

### 2️⃣ **Clonar o repositório**
Abra o terminal ou prompt de comando e execute:

  ```sh
  git clone https://github.com/seuusuario/validador-cartao.git

📂 Isso criará uma cópia local do projeto no seu computador.

3️⃣ Acessar o diretório
Navegue até a pasta onde o projeto foi clonado:
  sh
  cd validador-cartao

4️⃣ Executar o script
Rode o script Python com o seguinte comando:
  sh
  python validador_cartao.py

5️⃣ Inserir o número do cartão
Digite um número de cartão de crédito quando solicitado. O programa validará a bandeira do cartão.

🔍 Como funciona?
O usuário digita um número de cartão de crédito.

O programa remove espaços e traços do número.

O código verifica se o número corresponde a alguma bandeira de cartão pré-definida usando expressões regulares (Regex).

O programa retorna o nome da bandeira correspondente ou informa que o cartão é inválido.

📊 Exemplos de Entrada e Saída

✅ Entrada:
Digite o número do cartão de crédito: 4111 1111 1111 1111

📢 Saída:
Bandeira identificada: Visa

📜 Bandeiras Suportadas
O programa identifica as seguintes bandeiras de cartão de crédito:

✅ Visa

✅ MasterCard

✅ American Express

✅ Diners Club

✅ Discover

✅ JCB

✅ Elo

✅ Hipercard

⚠️ Observações

🔹 O script não verifica se o cartão é válido ou pode ser usado para compras. Apenas identifica sua bandeira com base no número fornecido.
🔹 O programa não armazena os números de cartão inseridos. A entrada do usuário é processada apenas momentaneamente para identificação.

🤝 Contribuições
💡 Caso queira melhorar este projeto, siga estas etapas:

Faça um fork deste repositório.

Crie uma nova branch com suas alterações:
  sh
  git checkout -b minha-melhoria

Commit suas alterações:
  sh
  git commit -m "Adicionando nova funcionalidade"

Envie um pull request para análise.

📄 Licença
Este projeto está sob a licença MIT, permitindo seu uso e modificação livremente. Consulte o arquivo LICENSE para mais detalhes.

🚀 Agora é só testar e usar! Qualquer dúvida, estou por aqui para ajudar! 😃


Esse guia cobre todo o passo a passo necessário, além de fornecer detalhes té
