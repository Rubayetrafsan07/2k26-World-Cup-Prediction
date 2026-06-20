import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
import joblib

df = pd.read_csv("data/processed/match_ml_dataset_v2.csv")


X = df.drop("result", axis=1)

# ENCODE TARGET
le = LabelEncoder()
y = le.fit_transform(df["result"])



X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# XGBOOST MODEL(Tuning)

model = XGBClassifier(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric="mlogloss",
    random_state=42
)


model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))


joblib.dump(model, "models/xgb_match_predictor.pkl")
joblib.dump(le, "models/label_encoder.pkl")

print("Model + Label Encoder saved successfully!")

