python
from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

data_file = 'Freelancer_Business_Activities_2023.xlsx'
data = pd.read_excel(data_file)

@app.route('/api/freelancer_activities', methods=['GET'])
def get_freelancer_activities():
    category = request.args.get('category')
    language = request.args.get('language', 'English')

    filtered_data = data
    if category:
        filtered_data = data[data['Category'].str.contains(category, case=False, na=False)]

    if language.lower() == 'arabic':
        filtered_columns = ['Activity_ID', 'Arabic_Name']
    else:
        filtered_columns = ['Activity_ID', 'English_Name']

    result = filtered_data[filtered_columns].to_dict(orient='records')
    return jsonify(result)

@app.route('/api/metadata', methods=['GET'])
def get_metadata():
    metadata = {
        'release_date': '2023-11-01',
        'update_frequency': 'Annually',
        'data_owner': 'Abu Dhabi Department of Economic Development',
        'language': ['English', 'Arabic'],
        'access_level': 'Public'
    }
    return jsonify(metadata)

if __name__ == '__main__':
    app.run(debug=True)
