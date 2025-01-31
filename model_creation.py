import pandas as pd
import pickle


data = pd.read_excel('PlacementDataset.xlsx')
x = data.iloc[:, :-1]
y = data.iloc[:, -1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33,random_state=100)
print(x_train)


from sklearn.ensemble import RandomForestRegressor
regr = RandomForestRegressor(max_depth=4, random_state=0)
regr.fit(x_train, y_train)
score_rf = regr.score(x_test,y_test)
print("random forest score = {}%".format(round(score_rf*100)))


pkl_filename = "Model/model.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(regr, file)