from datetime import datetime, timedelta
import json
from flask_app import app,render_template,bcrypt,redirect,request,session,flash
from flask import after_this_request, jsonify
import stripe
import requests

import re

from flask_app.models.sign_up_list import Sign_Up_List
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
import os
from PIL import Image
import random


def get_user_location():
    """Get user location and extract state"""
    try:
        response = requests.get('https://ipapi.co/json/')
        if response.status_code == 200:
            data = response.json()
            state = data.get('region')
            return state
    except Exception as e:
        print(f"Error getting user location: {e}")
    return None


@app.route('/splash_signup', methods=['POST'])
def splash_signup():
    print("Received splash signup request with data:", request.form)
    state = get_user_location()
    print("Detected state:", state)
    
    # Clean and validate input data
    name = request.form.get('name', '').strip()
    email = request.form.get('email', '').strip().lower()
    
    # Validate name
    if not name or len(name) < 2:
        return jsonify({'success': False, 'message': 'Name must be at least 2 characters.'}), 400
    
    # Validate email format
    if not EMAIL_REGEX.match(email):
        return jsonify({'success': False, 'message': 'Invalid email address.'}), 400
    
    formatted_data = {
        'name': name,
        'email': email,
        'state': state if state else 'Unknown'}
      
    Sign_Up_List.save(formatted_data)
    print("Signup saved to database:", formatted_data)
    return jsonify({'success': True, 'message': 'Successfully added to waitlist!'})




