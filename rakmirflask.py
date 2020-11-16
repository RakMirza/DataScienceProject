from flask import Flask
app = Flask(__name__)

@app.route('/sqrt/<input>') 
def sqrt():
    print("Inside Flask route")
    return '<PRE> Flask app is returning<PRE>'

if __name__ == '__main__':
    app.run(debug = True, port = 5000)    