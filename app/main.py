from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    returnData = {}
    returnData['Title'] = "Grogan's Café and Ice Cream Parlour"
    return render_template('index.html', **returnData)

if __name__ == "__main__":
    app.run(debug=True)