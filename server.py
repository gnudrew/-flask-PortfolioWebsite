from flask import Flask, render_template
import os

app=Flask(__name__)

@app.route('/')
def home():
    # return "Index Page"
    return render_template("index.html")

# Routing for App 1

@app.route('/app1')
def app1():
    return render_template("app1.html")

@app.route('/app1/run')
def app1_run():
    # launch the Kivy app.
    print(os.getcwd())
    os.chdir('apps/app1')
    print(os.getcwd())
    import apps.app1.main
    return 'Click!'

# Routing for App 2

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
