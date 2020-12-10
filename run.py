from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    # return "Index Page"
    return render_template("index.html")

@app.route('/MoodboosterMobileApp')
def app1():
    return render_template("app1.html")

@app.route('/DiningPhilosophers')
def app2():
    return render_template("app2.html")

@app.route('/DiningPhilosophers')
def app3():
    return render_template("app3.html")

@app.route('/DiningPhilosophers')
def app4():
    return render_template("app4.html")

@app.route('/DiningPhilosophers')
def app5():
    return render_template("app5.html")

@app.route('/DiningPhilosophers')
def app6():
    return render_template("app6.html")

if __name__=="__main__":
    app.run(debug=True)
