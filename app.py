from flask import Flask
import pandas as pd

import sys
import os

from util.service.Transformer import Transformer
from util.datastore.PgInterface import PgInterface


app = Flask(__name__)
pg = PgInterface()

def etl():
    transformer = Transformer()


    # Extract CSV files
    data_path = os.path.join(os.getcwd(), 'data')
    csv_list = os.listdir(data_path)

    dataframes = []

    usersData: pd.DataFrame
    experimentsData: pd.DataFrame
    compoundsData: pd.DataFrame

    for index, file_name in enumerate(csv_list):
        table_name = file_name.replace('.csv', '')
        df = pd.read_csv(os.path.join(data_path, file_name), delimiter=',\t')
        dataframes.append(df)
        dataframes[index].table_name = table_name
        if(table_name == 'users'):
            usersData = df
        if(table_name == 'user_experiments'):
            experimentsData = df
        if(table_name == 'compounds'):
            compoundsData = df
    
    
    # Transform data to derive features
    # 1. Total experiments a user ran.
    totalExperiments = transformer.total_experiments(usersData, experimentsData)
    
    
    # 2. Average experiments amount per user.
    averageExperiments = len(usersData.index) / len(experimentsData.index)

    # 3. User's most commonly experimented compound.
    usersCompounds = transformer.users_compounds(usersData, experimentsData, compoundsData)

    # Load processed data into a database
    for dataframe in dataframes:
        pg.load_data(dataframe)
    
    return { 'total_experiments_per_user': totalExperiments, 'average_experiments_amount_per_user': averageExperiments, 'most_compounds_per_user': usersCompounds }

@app.route('/trigger')
def trigger():
    data = etl()
    return {"message": "ETL process ran", "data": data}, 200


@app.route('/')
def ping():
    return {"message": "Server running..."}, 200

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)