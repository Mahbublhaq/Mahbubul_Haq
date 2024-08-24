from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configuration for Gmail
GMAIL_USER = 'gourob.haq@gmail.com'
GMAIL_PASSWORD = 'owtc hcch zufy cgey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def index2():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/skill')
def skill():
    return render_template('skill.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    email = request.form['email']
    subject = request.form['subject']
    description = request.form['description']

    try:
        # Set up the MIME
        message = MIMEMultipart()
        message['From'] = GMAIL_USER
        message['To'] = GMAIL_USER
        message['Subject'] = f'Email from: {email} - {subject}'

        # Attach the description to the email
        message.attach(MIMEText(description, 'plain'))

        # Connect to the server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(GMAIL_USER, GMAIL_PASSWORD)
            server.sendmail(GMAIL_USER, GMAIL_USER, message.as_string())

        flash('Email sent successfully!', 'success')
    except Exception as e:
        flash(f'Error: {e}', 'danger')

    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)
