from flask import Flask, render_template
from web import app

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/login_professores")
def login_professores():
    return render_template("login_professores.html")

@app.route("/login_alunos")
def login_alunos():
    return render_template("login_alunos.html")