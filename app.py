# app.py - Simple Internship Recommendation System

import os
import sqlite3
import json
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from ml_utils import predict
from roadmap_data import ROADMAPS

app = Flask(__name__)
app.secret_key = "simple_secret_key_123"

DB_FILE = "internship.db"

# Helper function to connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row # Allows dictionary-like access to rows
    return conn

# Create tables if they do not exist
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(150) UNIQUE NOT NULL,
        password_hash VARCHAR(256) NOT NULL,
        institution VARCHAR(200),
        year VARCHAR(20),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Create Predictions Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        predicted_domain VARCHAR(100),
        confidence FLOAT,
        readiness_category VARCHAR(50),
        readiness_score FLOAT,
        input_data TEXT,
        top_careers TEXT,
        missing_skills TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    conn.commit()
    conn.close()

# Run database setup
init_db()

# Enforce authentication for all pages
@app.before_request
def require_login():
    allowed_endpoints = ['login', 'register', 'static']
    if 'user_id' not in session and request.endpoint not in allowed_endpoints:
        return redirect(url_for('login'))


# ══════════════════════════════════════════════════════════════
# PAGES
# ══════════════════════════════════════════════════════════════

# Home Page
@app.route('/')
def home():
    # Check if a user is logged in using session
    user = None
    if 'user_id' in session:
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE id = ?", (session['user_id'],)).fetchone()
        conn.close()
    return render_template('home.html', user=user)


# Register Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if 'user_id' in session:
        return redirect(url_for('home'))
        
    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip().lower()
        password = request.form['password']
        institution = request.form['institution'].strip()
        year = request.form['year']

        if not name or not email or not password:
            flash("Please fill in all required fields.", "danger")
            return render_template('register.html')

        conn = get_db_connection()
        
        # Check if email already exists
        existing_user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        if existing_user:
            conn.close()
            flash("Email is already registered. Please log in.", "danger")
            return redirect(url_for('login'))

        # Insert new user
        hashed_password = generate_password_hash(password)
        conn.execute(
            "INSERT INTO users (name, email, password_hash, institution, year) VALUES (?, ?, ?, ?, ?)",
            (name, email, hashed_password, institution, year)
        )
        conn.commit()
        
        # Get the new user to log them in automatically
        user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        conn.close()

        session['user_id'] = user['id']
        session['user_name'] = user['name']
        
        flash("Registration successful! Welcome to the system.", "success")
        return redirect(url_for('assessment'))

    return render_template('register.html', user=None)


# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        email = request.form['email'].strip().lower()
        password = request.form['password']

        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        conn.close()

        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            flash("Welcome back!", "success")
            return redirect(url_for('home'))
        else:
            flash("Invalid email or password.", "danger")

    return render_template('login.html', user=None)


# Logout
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for('login'))


# Assessment Page
@app.route('/assessment')
def assessment():
    # Pass user details to templates for layout rendering
    user = None
    if 'user_id' in session:
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE id = ?", (session['user_id'],)).fetchone()
        conn.close()
    return render_template('assessment.html', user=user)


# Prediction Page
@app.route('/prediction')
def prediction():
    user = None
    if 'user_id' in session:
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE id = ?", (session['user_id'],)).fetchone()
        conn.close()
        
    # Get last prediction data stored in the session
    result = session.get('last_prediction')
    if not result:
        flash("Please take the assessment first.", "danger")
        return redirect(url_for('assessment'))
        
    return render_template('prediction.html', result=result, user=user)


# Learning Roadmap Page
@app.route('/roadmap')
def roadmap():
    user = None
    if 'user_id' in session:
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE id = ?", (session['user_id'],)).fetchone()
        conn.close()

    domain = request.args.get('domain')
    
    # If no domain is provided, use the last predicted domain from session
    if not domain:
        last_pred = session.get('last_prediction')
        if last_pred:
            domain = last_pred.get('predicted_domain')
        else:
            domain = "Machine Learning Engineer"

    roadmap_info = ROADMAPS.get(domain, {})
    all_domains = list(ROADMAPS.keys())
    
    return render_template(
        'roadmap.html',
        domain=domain,
        roadmap=roadmap_info,
        all_domains=all_domains,
        user=user
    )


# Dashboard Page
@app.route('/dashboard')
def dashboard():
    # Check if user is logged in
    if 'user_id' not in session:
        flash("Please log in to view the dashboard.", "danger")
        return redirect(url_for('login'))

    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE id = ?", (session['user_id'],)).fetchone()
    uid = session['user_id']

    # Fetch stats scoped to this user only
    total_predictions = conn.execute(
        "SELECT COUNT(*) FROM predictions WHERE user_id = ?", (uid,)
    ).fetchone()[0]

    # Career distribution for this user
    domain_rows = conn.execute(
        "SELECT predicted_domain, COUNT(*) as count FROM predictions WHERE user_id = ? GROUP BY predicted_domain",
        (uid,)
    ).fetchall()
    domain_counts = {}
    for row in domain_rows:
        domain_counts[row['predicted_domain']] = row['count']

    # Readiness category distribution for this user
    readiness_rows = conn.execute(
        "SELECT readiness_category, COUNT(*) as count FROM predictions WHERE user_id = ? GROUP BY readiness_category",
        (uid,)
    ).fetchall()
    readiness_counts = {'Excellent': 0, 'Good': 0, 'Average': 0, 'Need Improvement': 0}
    for row in readiness_rows:
        if row['readiness_category'] in readiness_counts:
            readiness_counts[row['readiness_category']] = row['count']

    # Get this user's most-recommended domain
    top_domain = "N/A"
    if domain_counts:
        top_domain = max(domain_counts, key=domain_counts.get)

    # Calculate this user's average confidence
    avg_confidence = 0
    if total_predictions > 0:
        avg_confidence = conn.execute(
            "SELECT AVG(confidence) FROM predictions WHERE user_id = ?", (uid,)
        ).fetchone()[0]
        avg_confidence = round(avg_confidence, 1)

    # Get this user's last 5 predictions
    recent_predictions = conn.execute(
        "SELECT * FROM predictions WHERE user_id = ? ORDER BY id DESC LIMIT 5", (uid,)
    ).fetchall()

    # Get logged-in user's latest prediction to show their skill profile
    user_prediction = conn.execute("SELECT * FROM predictions WHERE user_id = ? ORDER BY id DESC LIMIT 1", (session['user_id'],)).fetchone()
    
    conn.close()

    # Parse JSON variables for the template
    user_pred_data = None
    skills_dict = {}
    if user_prediction:
        user_pred_data = {
            'predicted_domain': user_prediction['predicted_domain'],
            'confidence': user_prediction['confidence'],
            'readiness_category': user_prediction['readiness_category'],
            'readiness_score': user_prediction['readiness_score']
        }
        
        # Extract skills for radar chart
        input_data = json.loads(user_prediction['input_data'])
        skills_dict = {
            'Python': float(input_data.get('Python Skill', 0)),
            'Java': float(input_data.get('Java Skill', 0)),
            'JavaScript': float(input_data.get('JavaScript Skill', 0)),
            'SQL': float(input_data.get('SQL Skill', 0)),
            'ML': float(input_data.get('Machine Learning', 0)),
            'DSA': float(input_data.get('Data Structures', 0)),
            'DBMS': float(input_data.get('DBMS', 0)),
            'OS': float(input_data.get('Operating System', 0))
        }

    return render_template(
        'dashboard.html',
        user=user,
        total_predictions=total_predictions,
        top_domain=top_domain,
        avg_confidence=avg_confidence,
        domain_counts_json=json.dumps(domain_counts),
        readiness_counts_json=json.dumps(readiness_counts),
        recent_predictions=recent_predictions,
        user_prediction=user_pred_data,
        skills_json=json.dumps(skills_dict)
    )


# About Me Page
@app.route('/about')
def about():
    user = None
    if 'user_id' in session:
        conn = get_db_connection()
        user = conn.execute("SELECT * FROM users WHERE id = ?", (session['user_id'],)).fetchone()
        conn.close()
    return render_template('about.html', user=user)


# ══════════════════════════════════════════════════════════════
# API ENDPOINT
# ══════════════════════════════════════════════════════════════

# POST request when form is submitted
@app.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        # Get data from form request
        data = request.form.to_dict()
        
        # Run ML model prediction
        result = predict(data)
        
        # Save to database
        user_id = session.get('user_id') # Will be None if user took assessment as guest
        
        conn = get_db_connection()
        conn.execute(
            """
            INSERT INTO predictions 
            (user_id, predicted_domain, confidence, readiness_category, readiness_score, input_data, top_careers, missing_skills)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user_id,
                result['predicted_domain'],
                result['confidence'],
                result['readiness_category'],
                result['readiness_score'],
                json.dumps(data),
                json.dumps(result['top_careers']),
                json.dumps(result['missing_skills'])
            )
        )
        conn.commit()
        conn.close()

        # Store in session for result page display
        session['last_prediction'] = result
        
        return redirect(url_for('prediction'))

    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)