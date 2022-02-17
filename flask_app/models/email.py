from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash 
import re 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')





class Email:

    db_name = "email_validation"

    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']




    @classmethod 
    def save(cls, data):
        query = "INSERT INTO email ( email) VALUES (%(email)s); "
        print(query)
        return connectToMySQL(cls.db_name).query_db(query, data)


    @staticmethod
    def validate_email(email):
        is_valid = True 
        if not EMAIL_REGEX.match(email['email']):
            flash("Invalid email", "error")
            is_valid = False 
        elif EMAIL_REGEX.match(email['email']):
            flash("Success your email is valid", "success")
        
        return is_valid

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM email;"
        results =connectToMySQL(cls.db_name).query_db(query)
        all_emails=[]
        for row in results:
            all_emails.append(cls(row))
        return all_emails