### Change History
# Ben Evans - 01/09/2026 - Created the Sign_Up_List model to handle the message table in the database.
# Ben Evans - 01/09/2026 - Added CRUD methods for database operations.





from pymysql import NULL
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, session
import random


DATABASE = 'splash_page'

class Sign_Up_List:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.email = data['email']
        self.state = data['state']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # CREATE
    @classmethod
    def save(cls, data):
        """Insert a new signup into the database"""
        query = """
        INSERT INTO sign_up_list (name, email, state)
        VALUES (%(name)s, %(email)s, %(state)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # READ ALL
    @classmethod
    def get_all(cls):
        """Retrieve all signups from the database"""
        query = "SELECT * FROM sign_up_list ORDER BY created_at DESC;"
        results = connectToMySQL(DATABASE).query_db(query)
        if not results:
            return []
        signups = []
        for row in results:
            signups.append(cls(row))
        return signups
    
    # READ ONE BY ID
    @classmethod
    def get_by_id(cls, data):
        """Retrieve a single signup by ID"""
        query = "SELECT * FROM sign_up_list WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return None
        return cls(results[0])
    
    # READ ONE BY EMAIL
    @classmethod
    def get_by_email(cls, data):
        """Check if email already exists in the database"""
        query = "SELECT * FROM sign_up_list WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if not results:
            return None
        return cls(results[0])
    
    # UPDATE
    @classmethod
    def update(cls, data):
        """Update an existing signup"""
        query = """
        UPDATE sign_up_list 
        SET name = %(name)s, email = %(email)s, state = %(state)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # DELETE
    @classmethod
    def delete(cls, data):
        """Delete a signup by ID"""
        query = "DELETE FROM sign_up_list WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # COUNT
    @classmethod
    def count_all(cls):
        """Get total count of signups"""
        query = "SELECT COUNT(*) as count FROM sign_up_list;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            return results[0]['count']
        return 0
    
    # VALIDATE
    @staticmethod
    def validate_signup(data):
        """Validate signup data"""
        is_valid = True
        
        # Validate name
        if len(data['name'].strip()) < 2:
            flash("Name must be at least 2 characters.", "signup")
            is_valid = False
        
        # Validate email format
        import re
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not email_regex.match(data['email']):
            flash("Invalid email address 2.", "signup")
            is_valid = False
        
        # Check if email already exists
        existing_user = Sign_Up_List.get_by_email({'email': data['email']})
        if existing_user:
            flash("This email is already registered.", "signup")
            is_valid = False
        
        return is_valid