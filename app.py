'''

flask

sqlite3

python

1. python -m venv venv
virtual environment

2. source venv/bin/activate

3. pip install flask

4. sqlite3 db.sqlite3

5. create table tablename(
    id integer primary key,
    name text,
    field text
);

6. insert into tablename(name, field) values ("joe", "sights");

'''

from flask import Flask, request, jsonify
import sqlite3


app = Flask(__name__)

@app.route('/gid_joe')
def ads():
    conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
    cur = conn.cursor()
    query = 'SELECT * FROM tablename'
    cur.execute(query)
    result = cur.fetchall()

   
    


    return_var = []
    for d in result:
        return_var.append(
            {
                'name': d[1],
            }
        )
    

    return return_var


app.run(debug=True, port=5002)