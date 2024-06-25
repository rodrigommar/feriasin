# Uso do componente ORM

# import library
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from pathlib import Path

# subclasse de DeclarativeBase
class Base(DeclarativeBase):
    pass


# Definindo o schema da subclasse que mapeia a tabela users
# Usando Mapped[] e mapped_column()
class User(Base):

    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[int] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(12))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    access_manager: Mapped[bool] = mapped_column(Boolean(), default=False)


# criando o path onde será salvo a base de dados
path_folder = Path(__file__).parent
BASE_DADOS = path_folder / 'bd_user.sqlite'


# criando o motor de coneção e a tabela no banco de dados
engine = create_engine(f'sqlite:///{BASE_DADOS}')
Base.metadata.create_all(bind=engine)


# criar uma função
def create_user(
        nome,
        password,
        email,
        **kwargs
):
    with Session(bind=engine) as session:
        user = User(
            nome=nome,
            password=password,
            email=email,
            **kwargs
        )
        session.add(user)
        session.commit()


if __name__ == '__main__':

    create_user(
        nome='Paul Pfeiffer',
        password='123456',
        email='pfeiffer@wonder.com'
    )