import json
import os
import MySQLdb

from flask import Flask, render_template

app = Flask(__name__, template_folder=os.path.join('static', 'templates'))


def connect_to_db():
    user = 'zhoudada'
    passwd = 'your_database_password'
    db_name = 'invader_detector'
    db = MySQLdb.connect(user=user, passwd=passwd, db=db_name)

    return db


def get_status():
    enabled = False
    try:
        db = connect_to_db()
        enabled = get_status_from_db(db)
    finally:
        db.close()
        return enabled


def get_status_from_db(db):
    c = db.cursor()
    c.execute('select enabled from system_enabled')
    (enabled,) = c.fetchone()

    return enabled == 1


def enable_system():
    enabled = False
    try:
        db = connect_to_db()
        c = db.cursor()
        c.execute('update system_enabled set enabled=true where id=1')
        db.commit()
        c.close()
        enabled = get_status_from_db(db)
    finally:
        db.close()
        return 'Current status: {}'.format(enabled)


def disable_system():
    enabled = False
    try:
        db = connect_to_db()
        c = db.cursor()
        c.execute('update system_enabled set enabled=false where id=1')
        db.commit()
        c.close()
        enabled = get_status_from_db(db)
    finally:
        db.close()
        return 'Current status: {}'.format(enabled)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/get_status', methods=['GET', 'POST'])
def get_status_view():
    system_enabled = get_status()
    return json.dumps(system_enabled)

@app.route('/enable', methods=['GET', 'POST'])
def enable_view():
    return enable_system()

@app.route('/disable', methods=['GET', 'POST'])
def disable_view():
    return disable_system()
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
