from flask import Flask
app = Flask(__name__)


@app.route('/my_app')
def hello_world:
	return render_template("my_app.html")

if __name__ == '__main__':
    app.run(debug=True)

