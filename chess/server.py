from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    

@app.route('/')
def play():
    return render_template("index.html", x=8,y=8)


@app.route('/4')
def play2():
    return render_template("index.html",x=8,y=4)

@app.route('/<int:x>')
def play22(x):
    return render_template("index.html",x=x,y=8)
    
    

@app.route('/<int:x>/<int:y>')
def play3(x,y):
    return render_template("index.html",x=x,y=y)

@app.route('/<int:x>/<int:y>/<a>/<b>')
def play4(x,y,a,b):
    return render_template("index.html",x=x,y=y,a=a,b=b)


if __name__=="__main__":
    app.run(debug=True)                   

