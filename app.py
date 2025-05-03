
from flask import Flask, render_template, request, redirect, url_for
from database.db import Base, engine, SessionLocal
from models.contact import Contact

app = Flask(__name__)
Base.metadata.create_all(bind=engine)

@app.route('/')
def index():
    session = SessionLocal()
    contacts = session.query(Contact).all()
    session.close()
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    session = SessionLocal()
    new_contact = Contact(name=name, phone=phone, email=email)
    session.add(new_contact)
    session.commit()
    session.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_contact(id):
    session = SessionLocal()
    contact = session.query(Contact).get(id)
    if contact:
        session.delete(contact)
        session.commit()
    session.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
