from flask import Flask, render_template, url_for, redirect, request
import ibm_db

global conn

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=764264db-9824-4b7c-82df-40d1b13897c2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=32536;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=cgs30384;PWD=pMs2fEZ5sMZzIk6g;",'','')

app = Flask(__name__)

@app.route('/')
def index():
    
    lists = []

    sql = "SELECT * FROM CGS30384.BLOGDB"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.execute(stmt)

    while True:
        row = ibm_db.fetch_assoc(stmt)
        if row is None:
            break
        lists.append(row)

    return render_template('index.html', lists=lists)


@app.route('/create', methods=['POST', 'GET'])
def create():

    if request.method == 'POST':

        postid = request.form['postid']
        title = request.form['title']
        content = request.form['content']
        location = request.form['location']
        iurl = request.form['iurl']

        sql = "INSERT INTO CGS30384.BLOGDB(postid, title, content, location, iurl) VALUES(?, ?, ?, ?, ?)"

        stmt = ibm_db.prepare(conn, sql)

        ibm_db.bind_param(stmt, 1, postid)
        ibm_db.bind_param(stmt, 2, title)
        ibm_db.bind_param(stmt, 3, content)
        ibm_db.bind_param(stmt, 4, location)
        ibm_db.bind_param(stmt, 5, iurl)

        if ibm_db.execute(stmt):
            print("New Post was inserted into the database successfully")
        else:
            print("Failed to insert the new post!")

    else:
        return render_template('create.html')

@app.route('/post/<string:postid>')
def post_view(postid):

    sql = "SELECT * FROM CGS30384.BLOGDB WHERE POSTID = ?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt, 1, postid)
    ibm_db.execute(stmt)
    post = ibm_db.fetch_assoc(stmt)
    if post:
        return render_template('post.html', post=post)
    else:
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=False)