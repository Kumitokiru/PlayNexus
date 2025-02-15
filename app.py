from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Adjusted to use a template file

if __name__ == '__main__':
    app.run(debug=True)
