import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("dataset.csv")

# Remove extra spaces from column names
data.columns = data.columns.str.strip()

# Convert target column
data["Heart Disease Status"] = data["Heart Disease Status"].map({
    "Yes": 1,
    "No": 0
})

# Show dataset balance
print(data["Heart Disease Status"].value_counts())

# 📊 Graph
sns.countplot(x=data["Heart Disease Status"])
plt.title("Heart Disease Distribution")
plt.show()

# Features
X = data[[
    "Age",
    "Blood Pressure",
    "Cholesterol Level",
    "Fasting Blood Sugar"
]]

# Target
y = data["Heart Disease Status"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = DecisionTreeClassifier(max_depth=3, random_state=42)

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("📊 Model Accuracy:", accuracy)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

# Save accuracy
with open("accuracy.txt", "w") as f:
    f.write(str(accuracy))

print("✅ Model trained successfully!")