# import dependencies
from flask import Flask, render_template, jsonify
# import data
#import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
#from sqlalchemy import create_engine, func


# #################################################
# # Database Setup
# #################################################
#engine = create_engine("postgresql://postgres:postgres@localhost:5432/MLB_DB")

# reflect an existing database into a new model
#Base = automap_base()
# reflect the tables
#Base.prepare(engine, reflect=True)
#print(Base.classes.keys())
# Save reference to the table
#mlb_data = Base.classes.mlb_data
#teams = Base.classes.teams
#salaries = Base.classes.salaries

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/team')
def viz1():
    return render_template('Teamapp.html')

@app.route('/year')
def viz2():
    return render_template('YearApp.html')

@app.route('/mlb')
def viz3():
    return render_template('mlb.html')

@app.route('/final_thoughts')
def endpoint():
    return render_template('end.html')



if __name__ == '__main__':
    app.run(debug=True)
    
