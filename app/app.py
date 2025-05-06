from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    try:
        return render_template('index.html', name='World'),200
    except Exception as e:
        return f"error occured in app {e}",500
if __name__ == '__main__':
    app.run(debug=True)
