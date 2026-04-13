from fastapi import FastAPI

#inicializar o fastapi
app = FastAPI(title ="gestão escolar")

#roda api
# no terminal: python -m uvicorn main:app --reload


#rota 
# métodos http: GET,POST,PUT,DELETE
@app.get("/")
def tela_inicial():
    return{"mensagem":" bem vindo ao sistema de gestão escolar"}

#banco de dados 
alunos ={
    1: {"nome":"yuri","idade":19},
    2: {"nome":"joana","idade":18},
    3: {"nome":"gabriel","idade":17},
}

@app.get("/alunos")
def listar_alunos():
    return {"alunos":alunos}