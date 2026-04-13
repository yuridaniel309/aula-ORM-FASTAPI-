#models é o arquivo onde fica as classes
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base



#TABELA CURSOS E ALUNOS (1:N)

class Curso (Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column (String(100), nullable=False)
    carga_horaria = Column (Integer, nullable=False)
    
    alunos = relationship("Aluno", back_populates="curso")



    def __repr__(self):
        return f"Curso = id: {self.id} - nome: {self.nome} - carga horária: {self.carga_horaria}"
    
class Aluno (Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column (String(100), nullable=False)
    email = Column (Integer, nullable=False)
    
    curso_id = Column(Integer, ForeignKey ("cursos.id"))

    curso = relationship("Curso", back_populates="alunos")

    def __repr__(self):
        return f"Curso = id: {self.id} - Nome: {self.nome} - Email: {self.email}"