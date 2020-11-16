
from flask import Flask
import math
app = Flask(__name__)    

           
@app.route('/sqrt/<input_1>')
def sqr_root(input_1):
    return str( math.sqrt(int(input_1)))
    

@app.route('/user/<username>')
def user(username):
    return username


if __name__ == '__main__':    
    app.run(debug = True, port = 5001)    