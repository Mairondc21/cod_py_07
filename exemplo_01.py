from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine) 

Session = sessionmaker(bind=engine)
session = Session()

usuario = session.query(Usuario).filter_by(nome='João').first()
print(f"Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}")

#outra faorma de fazer
try:
    novo_usuario = Usuario(nome='Ana', idade=25)
    session.add(novo_usuario)
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()

#melhor forma de fazer e mais recomendada
with Session() as session:
    novo_usuario = Usuario(nome='Ana', idade=25)
    session.add(novo_usuario)
    # O commit é feito automaticamente aqui, se não houver exceções
    # O rollback é automaticamente chamado se uma exceção ocorrer
    # A sessão é fechada automaticamente ao sair do bloco with    


