# 🧪 Testes Automatizados com Selenium — Caltech

Projeto desenvolvido para a disciplina de **Qualidade de Software**, com o objetivo de aplicar testes automatizados utilizando **Selenium + Pytest** no site da Caltech.

## 🎯 Objetivo

Validar elementos da interface web do site : https://www.caltech.edu  
Aplicando diferentes tipos de seletores (**ID, CSS, XPath**) e seguindo o padrão **Page Object Model (POM)**.

## 🏗️ Arquitetura

O projeto segue o padrão:

- **Page Object Model (POM)** → separação da lógica de interação com páginas
- **Pytest** → execução e organização dos testes
- **Selenium WebDriver** → automação do navegador

### Estrutura do projeto
```
📁 pages/
 ├── home_page.py
 ├── directory_page.py
 └── login_page.py

📁 tests/
 └── test_homepage.py

📄 conftest.py
📄 requirements.txt
📄 README.md
```


---

## ✅ Cobertura de Testes

O projeto contempla testes sobre diferentes elementos da interface, como:

- Menu de navegação
- Dropdown (hover)
- Logo (redirecionamento)
- Seções da página (Hero, News, Life, Events)
- Imagens
- Links
- Rodapé
- Busca (Directory)
- Login (Access)

⚠️ **Importante (regra do trabalho):**  
Cada elemento conta como **1 item testado**, mesmo que existam vários cenários sobre ele.

## 🧪 Casos de Teste Implementados

### 🏠 Home Page (caltech.edu)

- Menu visível
- Itens do menu
- Dropdown via hover
- Logo redireciona para home
- Seção Hero
- Seção Featured Events
- Seção News
- Seção Life at Caltech
- Ícones sociais
- Rodapé
- Links da página
- Título da página

### 📂 Directory (directory.caltech.edu)

- Campo de busca
- Botão de busca
- Digitação no campo

### 🔐 Access (login)

- Campo de usuário
- Campo de senha
- Botão de login
- Login inválido (teste negativo)

## ⚙️ Pré-requisitos

- Python 3.12.3
- Google Chrome instalado
- ChromeDriver compatível

## 📦 Instalação

### 1. Clonar o projeto
```bash
git clone <link-deste-repositorio>
cd T2-QualidadeDeSoftware
```
### 2. Criar/ativar ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate
```
#### ⚠️ Problema comum (Windows)
Se aparecer 
```Bash
execution of scripts is disabled
```
Execute no PowerShell como admin:
```Bash
execution of scripts is disabled
```
### 3. Instalar dependências
```Bash
pip install -r requirements.txt
```
### 4. Executar Testes
```Bash
pytest -v -s
```
- -v → detalhado
- -s → mostra logs no terminal

## 🧠 Observações Importantes

- Cada teste abre um navegador novo por padrão (isolamento de testes)
- Isso é comportamento esperado no Pytest
- Garante que um teste não interfira no outro

## 🚀 Tecnologias Utilizadas

- Python
- Selenium WebDriver
- Pytest