import pandas as pd
from pathlib import Path
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

data_path = Path(__file__).with_name("Delinquency_prediction_dataset.csv")
df = pd.read_csv(data_path)

features = ["Income", "Credit_Utilization", "Missed_Payments"]
target = "Delinquent_Account"

X = df[features].copy()
y = df[target]

X.loc[:, "Income"] = X["Income"].fillna(X["Income"].median())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = DecisionTreeClassifier(
    max_depth=4,
    min_samples_leaf=10,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
print(export_text(model, feature_names=features))
