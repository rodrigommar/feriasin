# import library
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import select, String, Boolean, create_engine

# bibliotecas usada para hashing e senhas
from werkzeug.security import generate_password_hash, check_password_hash

# biblioteca usada para definir o caminho
from pathlib import Path


# apontar o diretorio da base de dados
actual_folder = Path(__file__).parent
PATH_TO_BD = actual_folder / 'bd_user.sqlite'


# definição da subclasse Base
class Base(DeclarativeBase):
    pass


# definição da subclasse Usuario
class Usuario(Base):

    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(128))
    email: Mapped[str] = mapped_column(String(30), unique=True)
    access_manager: Mapped[bool] = mapped_column(Boolean(), default=False)

    def __repr__(self) -> str:
        return f'Usuario ({self.id=}, {self.name=})'

    def generate_password(self, password_user):
        self.password = generate_password_hash(password_user)

    def check_password(self, password_user):
        return check_password_hash(self.password, password_user)


# create a SQLite conection specificed by PATH_TO_BD
engine = create_engine(f'sqlite:///{PATH_TO_BD}')
Base.metadata.create_all(bind=engine)


# function to create new user, focus in "Session(bind=engine)"
def create_user(
        name,
        password,
        email,
        **kwargs
):
    with Session(bind=engine) as session:
        user = Usuario(
            name=name,
            email=email,
            **kwargs
        )
        user.generate_password(password)
        session.add(user)
        session.commit()


def read_all_users():
    with Session(bind=engine) as session:
        comando_sql = select(Usuario)
        usuarios = session.execute(comando_sql).fetchall()
        usuarios = [user[0] for user in usuarios]
        return usuarios


def read_one_user(id):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        one_user = session.execute(comando_sql).fetchall()
        return one_user[0][0]


def update_user(
        id,
        **kwargs
):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuarios = session.execute(comando_sql).fetchall()
        for usuario in usuarios:
            for key, value in kwargs.items():
                if key == 'password':
                    usuario[0].generate_password(value)
                else:
                    setattr(usuario[0], key, value)
        session.commit()


def delete_user(id):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuarios = session.execute(comando_sql).fetchall()
        for usuario in usuarios:
            session.delete(usuario[0])
        session.commit()


if __name__ == '__main__':

    create_user(
        name='Karen Arnold',
        password='123456',
        email='karen@wonder.com',
    )

    # usuarios = read_all_users()
    # usuario_0 = usuarios[0]
    # print(usuario_0)
    # print(usuario_0.name, usuario_0.email)

    # user_0 = read_one_user(id=1)
    # print(user_0)
    # print(user_0.name, user_0.email, user_0.check_password('123456'))

    # update_user(id=1, password='arnold123')

    # delete_user(id=2)
