import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

df = pd.read_csv("data/processed/match_ml_dataset.csv")

X = df. drop("result", axis = 1)
Y = df["result"]


# train / split
X_train, X_test, Y_train, Y_test = train_test_split(
    X,Y,
    test_size= 0.2,
    random_state= 42
)

# train model
model = RandomForestClassifier() 
model.fit(X_train, Y_train)

# predict
Y_pred = model.predict(X_test)  

# Evaluate Model
print("Accuracy:", accuracy_score(Y_test, Y_pred))
print(classification_report(Y_test, Y_pred))


joblib.dump(model, "models/match_predictor.pkl")

print("Model saved  successfully!")
