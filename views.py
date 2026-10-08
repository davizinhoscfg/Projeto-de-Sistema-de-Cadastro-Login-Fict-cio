from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Aluno, Professor
views = Blueprint("views", __name__)

@views.route("/")
def main_page():
    return render_template("index.html")

@views.route("/pagina_alunos")
def pagina_alunos():
    return render_template("pagina_alunos.html")

@views.route("/pagina_professores")
def pagina_professores():
    return render_template("pagina_professores.html")

@views.route("/login_professores")
def login_professores():
    return render_template("login_professores.html")

@views.route("/login_alunos", methods=["GET", "POST"])
def login_alunos():
    if request.method == "POST":
        email=request.form["usuario"]
        senha=request.form["senha"]

        aluno = Aluno.query.filter_by(email=email).first()

        if aluno and check_password_hash(aluno.senha_hash, senha):
            session["usuario_id"] = aluno.id
            session["tipo"] = "aluno"
            return redirect(url_for("views.pagina_alunos"))

        flash("E-mail ou senha incorretos")
        return redirect(url_for("views.login_alunos"))

    
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

        return redirect(url_for("views.pagina_professores"))   

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

        return redirect(url_for("views.pagina_alunos"))
    
    return render_template("cadastro_alunos.html")
        