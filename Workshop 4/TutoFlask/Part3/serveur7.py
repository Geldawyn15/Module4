from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/bonjour', methods=['POST'])
def hello():
    resultat = request.form
    nom = resultat['Nom']
    prenom = resultat['Prénom']
    nomComplet = prenom + " " + nom
    return render_template("bonjour.html" , message = nomComplet)
app.run()
