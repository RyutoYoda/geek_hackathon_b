from flask import Flask
from flask_cors import CORS
import os

app = Flask(__name__, instance_relative_config=True)
CORS(app)
app.json.ensure_ascii = False

app.config.from_mapping(
    SECRET_KEY="dev",
    DATABASE=os.environ["DATABASE_URL"],
)

# from feature import db
# db.init_db()
# from feature import auth
# app.register_blueprint(auth.bp)

from feature import test

from feature import db

@app.route('/')
def hello_world():
    conn=db.get_db()
    cursor=conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS visits (visited_on TIMESTAMP)')
    conn.commit()

    return 'CREATE TABLE!'

@app.route('/visit')
def visit():
    conn=db.get_db()
    cursor=conn.cursor()

    cursor.execute('INSERT INTO visits VALUES (NOW())')
    conn.commit()

    cursor.execute('SELECT * FROM visits')

    row=cursor.fetchall()
    result=','.join([str(r) for r in row])
    
    return 'DataBase content:'+result


app.register_blueprint(test.app)

if __name__ == "__main__":
    app.run()
