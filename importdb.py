from pymongo import MongoClient
import csv

client = MongoClient("mongodb+srv://rjs2114:1357@cluster0.7tqlw.mongodb.net/projectDB?retryWrites=true&w=majority")

heart_db = client["db_1"]
heart_collection = heart_db["collection_1"]

def read_csv(FILENAME, COLUMNS):
    reader = open(FILENAME, 'r')
    csv_dict = csv.DictReader(reader, COLUMNS)
    next(csv_dict)
    return csv_dict

FILENAME = './heart_disease_health_indicators_BRFSS2015.csv'
COLUMNS = ('HeartDiseaseorAttack', 'Sex', 'Age', 'HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'Diabetes', 'PhysActivity',
'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth', 'MentHlth', 'PhysHlth',
'DiffWalk')

data = list(read_csv(FILENAME, COLUMNS))
col_float = ['HeartDiseaseorAttack', 'Sex', 'Age', 'HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'Diabetes', 'PhysActivity',
'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth', 'MentHlth', 'PhysHlth',
'DiffWalk']

for row in data:
    for col in col_float:
        row[col] = float(row[col])

# print(data)
heart_collection.insert_many(data)