# Projeto Exemplo

Este é um projeto de exemplo que demonstra o uso de várias bibliotecas para manipulação de banco de dados, hashing de senhas e manipulação de caminhos. Abaixo estão listadas as bibliotecas necessárias para executar este projeto.

## Bibliotecas Necessárias

### SQLAlchemy

O SQLAlchemy é usado para interagir com o banco de dados. Ele fornece uma ORM (Object Relational Mapping) que facilita a manipulação dos dados no banco.

Instalação:
```bash
pip install sqlalchemy
```

Importação no projeto:
```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import select, String, Boolean, create_engine
```

### Werkzeug

O Werkzeug é utilizado para hashing de senhas, oferecendo métodos seguros para gerar e verificar hashes de senhas.

Instalação:
```bash
pip install werkzeug
```

Importação no projeto:
```python
from werkzeug.security import generate_password_hash, check_password_hash
```

### Pathlib

A biblioteca pathlib é usada para manipulação de caminhos de forma mais intuitiva e segura. Ela faz parte da biblioteca padrão do Python, então não é necessário instalá-la separadamente.

Importação no projeto:
```python
from pathlib import Path
```

## Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/projeto-exemplo.git
```

2. Navegue até o diretório do projeto:
```bash
cd projeto-exemplo
```

3. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute o projeto:
```bash
python main.py
```

## Contribuindo

1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature-nova-funcionalidade`).
3. Faça suas alterações e commit (`git commit -m 'Adiciona nova funcionalidade'`).
4. Envie suas alterações (`git push origin feature-nova-funcionalidade`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

## Arquivo `requirements.txt`

Para facilitar a instalação das dependências, você pode criar um arquivo `requirements.txt` com o seguinte conteúdo:

```
sqlalchemy
werkzeug
```

Isso permitirá que os usuários instalem todas as dependências necessárias com um único comando:

```bash
pip install -r requirements.txt
```

---


## Personagens de "Anos Incríveis"

- **Kevin Arnold (Fred Savage)**: O protagonista, cujas experiências de vida são narradas à medida que ele cresce.
- **Winnie Cooper (Danica McKellar)**: O interesse amoroso de Kevin e sua amiga de infância.
- **Paul Pfeiffer (Josh Saviano)**: O melhor amigo de Kevin, conhecido por seu comportamento nerd e leal.
- **Jack Arnold (Dan Lauria)**: O pai de Kevin, um veterano da Segunda Guerra Mundial que trabalha duro para sustentar a família.
- **Norma Arnold (Alley Mills)**: A mãe de Kevin, uma dona de casa dedicada e compreensiva.
- **Karen Arnold (Olivia d'Abo)**: A irmã mais velha de Kevin, que tem um espírito rebelde e é parte da contracultura dos anos 60.
- **Wayne Arnold (Jason Hervey)**: O irmão mais velho de Kevin, que frequentemente o atormenta, mas também se preocupa com ele.
