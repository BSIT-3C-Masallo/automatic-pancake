import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Load dataset
df = pd.read_csv('data/course_data.csv')

# Strip leading/trailing whitespace
df['Gender'] = df['Gender'].str.strip()
df['Interest'] = df['Interest'].str.strip()
df['Course'] = df['Course'].str.strip()

# Encode categorical features
le_gender = LabelEncoder()
le_interest = LabelEncoder()
le_course = LabelEncoder()

df['gender_encoded'] = le_gender.fit_transform(df['Gender'])
df['interest_encoded'] = le_interest.fit_transform(df['Interest'])
df['course_encoded'] = le_course.fit_transform(df['Course'])

# Features and target
X = df[['Age', 'gender_encoded', 'interest_encoded']]
y = df['course_encoded']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Ensure the output directory exists
output_dir = 'ml_model'
os.makedirs(output_dir, exist_ok=True)

# Save model and encoders
joblib.dump(model, os.path.join(output_dir, 'course_predictor_model.pkl'))
joblib.dump(le_gender, os.path.join(output_dir, 'gender_encoder.pkl'))
joblib.dump(le_interest, os.path.join(output_dir, 'interest_encoder.pkl'))
joblib.dump(le_course, os.path.join(output_dir, 'course_encoder.pkl'))

print("✅ Model and encoders saved successfully.")
