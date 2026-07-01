# ml_utils.py - Simple Machine Learning helper file

import joblib
import numpy as np
import os

# Get path to the model directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "random_forest_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "model", "scaler.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "model", "label_encoder.pkl")

# List of 37 features in exact order used by the model
FEATURE_COLUMNS = [
    'SSC Percentage', 'HSC Percentage', 'Gender', 'Age', 'CGPA', 'Backlogs',
    'Python Skill', 'Java Skill', 'C++ Skill', 'JavaScript Skill',
    'SQL Skill', 'Data Structures', 'Algorithms', 'DBMS', 'Operating System',
    'Computer Networks', 'Software Engineering', 'Machine Learning', 'Deep Learning',
    'Statistics', 'Data Analysis', 'Data Visualization', 'AWS', 'Azure', 'Docker',
    'Kubernetes', 'CI/CD', 'Communication', 'Leadership', 'Teamwork', 'Presentation',
    'Problem Solving', 'Number of Projects', 'Certifications Count',
    'Internship Experience', 'Hackathon Participation', 'Research Papers'
]

# Simple prediction function
def predict(form_data):
    # Load model files
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    encoder = joblib.load(ENCODER_PATH)

    # Convert Gender: 'Female' becomes 1, others become 0
    gender_input = form_data.get('Gender', 'Male')
    if gender_input == 'Female':
        gender_val = 1
    else:
        gender_val = 0

    # Build the feature list
    features = []
    for col in FEATURE_COLUMNS:
        if col == 'Gender':
            features.append(gender_val)
        else:
            value = form_data.get(col, 0)
            features.append(float(value))

    # Scale the features and predict
    features_array = np.array(features).reshape(1, -1)
    scaled_features = scaler.transform(features_array)
    
    pred_class_encoded = model.predict(scaled_features)[0]
    probabilities = model.predict_proba(scaled_features)[0]

    # Get predicted domain name and confidence
    predicted_domain = encoder.inverse_transform([pred_class_encoded])[0]
    confidence_score = float(round(max(probabilities) * 100, 1))

    # Get top 3 recommended careers
    classes = encoder.classes_
    sorted_indices = np.argsort(probabilities)[::-1]
    top_careers = []
    for i in range(3):
        idx = sorted_indices[i]
        top_careers.append({
            'domain': classes[idx],
            'confidence': float(round(probabilities[idx] * 100, 1))
        })

    # Calculate simple readiness score (0-100)
    cgpa = float(form_data.get('CGPA', 0))
    python_skill = float(form_data.get('Python Skill', 0))
    projects = float(form_data.get('Number of Projects', 0))
    
    # Simple weighted formula: CGPA (40%) + Python Skill (30%) + Projects (30%)
    # Scale CGPA to 0-10, Python to 0-10, Projects to 0-10 (capped at 5 projects)
    cgpa_score = cgpa * 10 # cgpa is out of 10, so e.g. 8.5 becomes 85
    python_score = python_skill * 10 # skill is 1 to 10, so e.g. 8 becomes 80
    project_score = min(projects, 5) * 20 # 5 projects = 100
    
    readiness_score = (cgpa_score * 0.40) + (python_score * 0.30) + (project_score * 0.30)
    readiness_score = round(readiness_score, 1)

    # Readiness categories
    if readiness_score >= 80:
        readiness_cat = "Excellent"
    elif readiness_score >= 60:
        readiness_cat = "Good"
    elif readiness_score >= 40:
        readiness_cat = "Average"
    else:
        readiness_cat = "Need Improvement"

    # Calculate missing skills based on a simple required minimum threshold of 6/10
    required_threshold = 6
    missing_skills = []
    skills_to_check = ['Python Skill', 'SQL Skill', 'Data Structures', 'Algorithms', 'DBMS']
    for skill in skills_to_check:
        user_val = int(form_data.get(skill, 0))
        if user_val < required_threshold:
            missing_skills.append({
                'skill': skill,
                'current': user_val,
                'required': required_threshold,
                'gap': required_threshold - user_val
            })

    return {
        'predicted_domain': predicted_domain,
        'confidence': confidence_score,
        'readiness_score': readiness_score,
        'readiness_category': readiness_cat,
        'top_careers': top_careers,
        'missing_skills': missing_skills
    }
