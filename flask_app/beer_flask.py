from flask import Flask, request, render_template
from forms import beer_recipe_form
import pickle
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from collections import defaultdict

app = Flask(__name__)

app.config['SECRET_KEY'] = 'KeadTUs4Ub&r&oY2$*&nFG^Zy'

with open("rf_predictor.pkl", "rb") as f:
    rf_predictor = pickle.load(f)

@app.route('/')
def beer():
	
	form = beer_recipe_form()
	return render_template('beer.html', form = form)

@app.route('/', methods=['POST', 'GET'])
def predict():

	form = beer_recipe_form()

	if request.method=='POST':
		form_fields = ['abv','ibu','color','boil_size','boil_time','boil_gravity','efficiency','wort_change']
		df_columns = ['ABV','IBU','Color','BoilSize','BoilTime','BoilGravity','Efficiency','ChangeInWort']
		recipe_df = pd.DataFrame(columns=df_columns)
		recipe_dict = defaultdict(int)
		for column in df_columns:
			for field in form_fields:
				recipe_dict[column] = request.form[field]
		recipe_df = recipe_df.append(recipe_dict, ignore_index=True)
		predicted_style = rf_predictor.predict(recipe_df)[0]

	return render_template('beer.html', form = form, prediction= predicted_style)



app.run(debug=True)