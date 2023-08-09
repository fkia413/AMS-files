from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Homepage"

# @app.route("/square/<int:num>", methods=["GET"])
# def square(num):
#     return str(num ** 2)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

@app.route('/ben')
def ben():
    return render_template('ben.html')

@app.route('/harry')
def harry():
    return render_template('harry.html')

@app.route('/namelist')
def namelist():
    return render_template('namelist.html', names=["ben", "harry", "bob", "jay", "matt", "bill"])

