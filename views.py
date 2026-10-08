from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from models import db, Aluno, Professor
views = Blueprint("views", __name__)

@views.route("/")
def main_page():
    return render_template("index.html")

@views.route("/login_professores")
def login_professores():
    return render_template("login_professores.html")

@views.route("/login_alunos")
def login_alunos():
    return render_template("login_alunos.html")

@views.route("/cadastro_professores", methods = ["GET", "POST"])
def cadastro_professores():
    if request.method == "POST":
        nome=request.form["nome"]
        email=request.form["email"]
        disciplina=request.form["disciplina"]
        senha=request.form["senha"]

        novo_professor = Professor(
            nome=nome,
            email=email,
            disciplina=disciplina,
            senha_hash=generate_password_hash(senha)
            )
        db.session.add(novo_professor)
        db.session.commit() 

        return "Certinho papai"   

    return render_template("cadastro_professores.html")

@views.route("/cadastro_alunos", methods = ["GET", "POST"])
def cadastro_alunos():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        matricula = request.form["matricula"]
        senha = request.form["senha"]

        novo_aluno = Aluno(
            nome=nome,
            email=email,
            matricula=matricula,
            senha_hash=generate_password_hash(senha)
        )

        db.session.add(novo_aluno)
        db.session.commit()

        return "Deu certo pai"
    
    return render_template("cadastro_alunos.html")
        