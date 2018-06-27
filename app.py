#flask app
#implement a FLASK SESSION
#creating a basic login page

from flask import Flask, render_template, request, session, url_for, g, redirect
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods= ['GET','POST'])
def index():
    if request.method=='POST':  #if the method is POST then first drop the current ongoing session
        session.pop('user', None)

        if request.form['password']== 'password': #check if password==password
            session['user']= request.form['username'] #take name from the form
            return redirect(url_for('protect')) #if all the conditions are true then go to the protected page else go to the index page
    return render_template('index.html')
    #return render_template('index.html')

@app.route('/protect')
def protect():
    if g.user:
        return render_template('protect.html')
    return redirect(url_for("index"))

""" to make the 'protect' page a password protect use """
#note-> user shuould have an active session before getting to this page
# g is a global variable used
@app.before_request
def before_request():
    g.user=None
     #if session exists then set g.user to the user
    if 'user' in session:
        g.user = session['user']

@app.route('/getsession')
def getsession():
     if 'user' in session:
         return session['user']
     return "Not Logged in"
@app.route('/dropsession')
def dropsession():
    session.pop('user', None)
    return 'Dropped'

if __name__== '__main__':
    app.run(debug=True)
