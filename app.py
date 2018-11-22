from flask import Flask
app = Flask(__name__)

background-color: "blue"

@app.route('/')
def zimbabwi():
    return 'welcome to Zimbabwi'




if __name__ == '__main__':
    app.run(debug=True)

