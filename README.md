# Compdistapp
**Descrição**

Este pequeno projeto implementa um pequeno sistema distribuido, segundo os requisitos para a avaliação "Prova 01" para a disciplina de Computação distribuída, turma P01, segundo semestre de 2024

## Sumário
- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Pré-requisitos](#pré-requisitos)
- [Configuração](#configuração)
- [Uso da Aplicação](#uso-da-aplicação)
- **[Relatório](#relatório)**

## Sobre o Projeto
Este projeto consiste na implementação, build e deploy de um sistema trivial em um ou dois *containers*. O sistema implementa um serviço de autorização e logging à partir de dados persistidos em banco. O sistema também é capaz visualizar e cadastrar usuários por meio de uma interface *admin*. 

## Tecnologias Utilizadas
- Python - versão 3.11
- MySQL - versão 8.0
- Docker - versão 27.2.0
- Docker Compose - versão v2.29.2-desktop.2
- Outras dependências listadas em `requirements.txt`

## Estrutura do Repositório
```
├── src/                     # Código fonte da aplicação
├── Dockerfile               # Arquivo para criação da imagem Docker
├── docker-compose.yml       # Arquivo composição com container MySql
├── requirements.txt         # Dependências da aplicação
├── .gitignore               # Arquivo .gitignore
├── README.md                # Documentação do projeto
└── Relatorio.pdf            # Relatório final do projeto
```
## Pré-requisitos
Antes de iniciar, é necessário instalar:

- Docker
- Docker Compose

## Configuração

**Construir a imagem Docker:**

No terminal, execute:

```bash
docker build -t nome-da-imagem .
```
**Configurar as variáveis de ambiente:**

Edite o arquivo docker-compose.yml, configurando as variáveis de ambiente necessárias (como credenciais do MySQL).

```yml
    image: nome-da-imagem #tostole/compdistapp (imagem disponível dem Docker Hub)
    environment:
        # Key for encryption (there is a default one)
        SECRET_KEY: d5zmAsUt3bZdZrBjhcpJ7T2ocQgmVXfM

        # Database URI (default: sqlite:///usersdb.sqlite3)
        # mysql+pymysql://{user}:{password}@{host}:{port}/{schema}
        DATABASE: mysql+pymysql://root:123@mysql:3306/db

        # Admin credentials (default: admin 123)
        ADMIN_USER: admin
        ADMIN_PASSWORD: 123
    ports:
      - 8080:8080 #Mapped ports (default: 8080)

```

**Subir os containers:**

Execute o comando abaixo para iniciar a aplicação e o banco de dados:
```bash
docker-compose up -d
```
## Uso da aplicação
- Para acessar a funcionalidade de autenticação somente `localhost:8080`
- Para acessar a funcionalidade de admin
`localhost:8080/admin`

Em ambos endereços, será necessário entrar com credenciais validas. Sendo a primeira vez, apenas o usuário admin padrão estará disponível (conforme as variáveis em docker-compose).

Em `/admin` é possível visualizar um painel com a tabela `profiles`, por onde é possível realizar operações *CRUD*

Os logins são registrados em log no diretorio ./docker/log/ (relativo ao docker-compose)

# Relatório
O relatório, em formato SBC, trata todas as decisões de mudanças no código original e expões as justificativas de decisões de projeto  
