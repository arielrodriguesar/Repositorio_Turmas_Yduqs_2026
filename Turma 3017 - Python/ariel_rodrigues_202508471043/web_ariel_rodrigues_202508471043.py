from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "<h1>Olá, alunos!</h1>"
if __name__ == "__main__":
    app.run(port=8080, debug=True)