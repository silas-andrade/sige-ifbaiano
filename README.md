
# SIGE IFBAIANO - README

## 📋 Visão Geral

O SIGE IFBAIANO é um sistema de gestão integrada desenvolvido para o Instituto Federal Baiano. Este projeto visa simplificar processos administrativos e acadêmicos através de uma plataforma centralizada e intuitiva.

## 🚀 Começando


### Pré-requisitos

- Python
- uv
- Django

### Instalação Passo a Passo

1. **Clone o repositório**
    ```bash
    git clone https://github.com/silas-andrade/sige-ifbaiano.git
    cd sige-ifbaiano
    ```

2. **Configure o ambiente**
    ```bash
    uv venv
    ```

3. **Instale as dependências**
    ```bash
    uv pip install -r requirements.txt
    ```

4. **Execute migrações do banco de dados**
    ```bash
    uv run manage.py migrate
    ```

5. **Inicie o servidor**
    ```bash
    uv run manage.py runserver
    ```


6. **Acesse a aplicação**
    - Abra seu navegador e vá para `http://127.0.0.1:8000`


## 🤝 Contribuindo

Siga as convenções de código do projeto e crie pull requests descritivas.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
