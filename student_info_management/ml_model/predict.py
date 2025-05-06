import joblib
import os
import pandas as pd  # Import pandas

# Load model and encoders
base_dir = os.path.dirname(__file__)
model = joblib.load(os.path.join(base_dir, 'course_predictor_model.pkl'))
le_gender = joblib.load(os.path.join(base_dir, 'gender_encoder.pkl'))
le_interest = joblib.load(os.path.join(base_dir, 'interest_encoder.pkl'))
le_course = joblib.load(os.path.join(base_dir, 'course_encoder.pkl'))

def predict_course(age, gender, interest):
    try:
        # Encode the gender and interest
        gender_encoded = le_gender.transform([gender])[0]
        interest_encoded = le_interest.transform([interest.lower()])[0]

        # Prepare the input data as a DataFrame with proper column names
        input_df = pd.DataFrame({
            'Age': [age],
            'gender_encoded': [gender_encoded],
            'interest_encoded': [interest_encoded]
        })

        # Predict using the model
        prediction = model.predict(input_df)  # Using the DataFrame here
        print(f"Raw prediction: {prediction}")  # Print the raw prediction output

        # Convert the prediction back to the course name
        course_name = le_course.inverse_transform(prediction)[0]
        print(f"Predicted course name: {course_name}")  # Print the predicted course

        return course_name
    except Exception as e:
        return f"Prediction error: {str(e)}"

