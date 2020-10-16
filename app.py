from flask import Flask, render_template, request
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
import time


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/", methods=['GET', 'POST'])
@app.route("/index", methods=['GET', 'POST'])
def index():
	smiles = ''
	if request.method == "POST":
		smiles = request.form.get("smiles")
		if smiles != '':
			m = Chem.MolFromSmiles(smiles)
			AllChem.EmbedMolecule(m)
			w = Chem.SDWriter('static/molecule.sdf')
			w.write(m)

	return render_template("index.html", smiles=smiles)

if __name__ == '__main__':
    app.run(debug=True)