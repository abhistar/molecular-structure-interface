from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/")
@app.route("/index", methods=['GET', 'POST'])
def index():
	smiles = ''
	if request.method == "POST":
		smiles = request.form.get("smiles")

	return render_template("index.html", smiles=smiles)


@app.route("/result", methods=["POST"])
def result():
	smiles = request.form.get("smiles")
	return render_template("layout.html", smiles=smiles)


if __name__ == '__main__':
    app.run(debug=True)