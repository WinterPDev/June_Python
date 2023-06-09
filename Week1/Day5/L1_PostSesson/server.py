from flask import Flask, render_template, redirect, session, request

# import request, session and redirect from flask
# session stores a global variable onto our server in the form of a dictionary

app = Flask(__name__)
app.secret_key = 'baylife'


# Show Route
@app.route('/')
def Home():
    return render_template('index.html')


# Objective 1: Use session to pass a username from a simulated login page to a welcome page.

# Action Route
@app.route('/login', methods = ['POST'])
def login_action():
    # We extract form data from a dictionary that is returned by 'request.form'
    
    # print(request.form)
    session['username'] = request.form['username']
    
    '''
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    DO NOT RENDER ON A POST ROUTE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    '''
    return redirect('/dashboard')



# Objective 2: Using the form on the dashboard, build a POST route to submit the form data into session.
# Show route for the form on dashboard
@app.route('/dashboard')
def dashboard():

    return render_template('dashboard.html')


#action route for form

@app.route('/submit_form', methods=['POST'])
def submit_form():
    session['name'] = request.form['name']
    session['genre'] = request.form['genre']
    session['release'] = request.form['release']

    print(request.form)
    return redirect('/form_results')


# Objective 3: Retrieve the session data and show it on the page via Jinja.

@app.route('/form_results')
def show_results():
    return render_template('results.html')

# Objective 4: Create a logout route to clear session and redirect to the original login page.

@app.route('/logout')
def logout():
    # session.pop('username') # remove a specific key
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run( debug=True, port=5001 )

