from flask import Flask, render_template, abort
import requests

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/perfil/<string:username>")
def perfil(username):
	token = "?access_token=cfa85615a38d9b6ae192a97549452e404c6bc659"
	url = 'https://api.github.com/users/' + username + token
	r = requests.get(url)
	if r.status_code == 200:
		url_repos = r.json()['repos_url'] + token
		repos = requests.get(url_repos).json()
		return render_template("perfil.html", usuario=r.json(), repos=repos)
	else:
		return abort(404)

if __name__ == '__main__':
	app.run(debug=True)