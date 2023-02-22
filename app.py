from flask import Flask, send_from_directory, render_template



app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello():
    return render_template('index.html')
    
@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)


if __name__ == "__main__":
    app.run()