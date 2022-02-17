from flask_app import app 
from flask import redirect, render_template, session,request
from flask_app.models.email import Email






@app.route('/')
def root_route():
    return render_template('index.html')


@app.route('/email', methods=['POST'])
def email():

    session['email'] = request.form['email']

    if not Email.validate_email(request.form):
        return redirect('/')
    elif Email.validate_email(request.form):
        new_email = Email.save(request.form)
    return redirect('/success')


    


@app.route('/success')
def success():
    return render_template('success.html', all_emails = Email.get_all())