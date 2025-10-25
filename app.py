from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
