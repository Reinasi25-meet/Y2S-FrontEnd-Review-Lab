from Flask import Flask, render_template, request , redirect, url_for
from Flask import session as login_session
import pyrebase 


app=Flask(__name__)
app.config["SECRET KEY"]="123456"

firebase= pyrebase.initialize_app(config)
auth=firebase.auth()


const firebaseConfig = {
  apiKey: "AIzaSyD4Y25q0Pa_ChBBK26h4_bI6p_vTfvibrc",
  authDomain: "auth-lab-178d1.firebaseapp.com",
  projectId: "auth-lab-178d1",
  storageBucket: "auth-lab-178d1.appspot.com",
  messagingSenderId: "171677911133",
  appId: "1:171677911133:web:8ac94dd84aa247a0a3e5b4"}

  @app.rout("/", methods=["GET,POST"]
    def login()

    if request.method == 'GET':
        return render_template("login.html") 
    else: #if the method is post
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Womp it failed sad"
            return render_template("login.html", error=error)

  @app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'GET':
        return render_template("signup.html") 
    else: #if the method is post
        email = request.form['email']
        password = request.form['password']
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            print(login_session['user'])
            print(login_session['user']['localId'])
            return redirect(url_for('home'))
        except:
            error = "Womp it failed. Try again"
            return render_template("signup.html",error=error)
        
    
@app.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        login_session['user'] = None
        auth.current_user = None
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
