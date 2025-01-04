from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Define valid username and password combinations with their corresponding URLs
valid_credentials = {
    'user': {'password': 'password', 'redirect_url': 'https://skola-home.vercel.app/'},
    'user1': {'password': 'password1', 'redirect_url': 'https://example-link2.com/'},
    'user2': {'password': 'password2', 'redirect_url': 'https://example-link3.com/'}
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the username exists and the password matches
        if username in valid_credentials and valid_credentials[username]['password'] == password:
            # Redirect to the corresponding URL based on the username
            return redirect(valid_credentials[username]['redirect_url'])
        else:
            # If the credentials are incorrect
            return 'Invalid username or password! Please try again. <a href="/">Go back</a>'

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
