from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Define valid username and password combinations
valid_credentials = {
    'user': 'password',
    'thirulingeshwar': 'thirulingeshwar sci'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the username exists and the password matches
        if username in valid_credentials and valid_credentials[username] == password:
            # Redirect to Skola Tech Academy home page
            return redirect("https://skola-home.vercel.app/")
        else:
            # If the credentials are incorrect
            return 'Invalid username or password! Please try again. <a href="/">Go back</a>'

    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
