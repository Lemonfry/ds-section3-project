import pickle

model = None
with open('xgbc.pkl','rb') as pickle_file:
   model = pickle.load(pickle_file)

X_test = [[1, 1, 1, 37, 1, 1, 2, 0, 0, 1, 0, 1, 0, 5 , 0, 0, 1, 1, 10, 6, 5]]
y_pred = model.predict(X_test)

print(y_pred)