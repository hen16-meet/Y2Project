from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():    
	return render_template("MyHomepage.html")

@app.route('/about')
def about():
	return render_template("Aboutme.html")

@app.route('/contact')
def contact():
	return render_template("ContactMe.html")

if __name__ == '__main__':
	app.run(debug=True)
