from models.clientes import Clientes
from flask import render_template

def homeController():
    try:
        user = Clientes("Maria Joana", "senhaDaMaria")
        return render_template('home.html', user=user)
    except Exception as e:
        return "Error ao fazer algo. Erro {}".format(str(e)), 405