from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/python")
def python_notes():
    return render_template("python.html")

@app.route("/java")
def java_notes():
    return render_template("java.html")

@app.route("/dbms")
def dbms_notes():
    return render_template("dbms.html")

@app.route("/javascript")
def javascript_notes():
    return render_template("javascript.html")

@app.route("/books")
def books():
    return render_template("books.html")

@app.route("/python/introduction")
def introduction():
    return render_template("introduction.html")

@app.route("/python/variables")
def variables():
    return render_template("variables.html")

@app.route("/python/datatypes")
def datatypes():
    return render_template("datatypes.html")

@app.route("/python/operators")
def operators():
    return render_template("operators.html")

@app.route("/python/ifelse")
def ifelse():
    return render_template("ifelse.html")

@app.route("/python/loops")
def loops():
    return render_template("loops.html")

@app.route("/java/introduction")
def java_intro():
    return render_template("java_introduction.html")

@app.route("/java/variables")
def java_variables():
    return render_template("java_variables.html")

@app.route("/java/datatypes")
def java_datatypes():
    return render_template("java_datatypes.html")

@app.route("/java/operators")
def java_operators():
    return render_template("java_operators.html")

@app.route("/java/ifelse")
def java_ifelse():
    return render_template("java_ifelse.html")

@app.route("/java/loops")
def java_loops():
    return render_template("java_loops.html")

@app.route("/dbms/introduction")
def dbms_intro():
    return render_template("dbms_introduction.html")

@app.route("/dbms/architecture")
def dbms_architecture():
    return render_template("dbms_architecture.html")

@app.route("/dbms/keys")
def dbms_keys():
    return render_template("dbms_keys.html")

@app.route("/dbms/sql")
def dbms_sql():
    return render_template("dbms_sql.html")

@app.route("/dbms/normalization")
def dbms_normalization():
    return render_template("dbms_normalization.html")

@app.route("/dbms/transactions")
def dbms_transactions():
    return render_template("dbms_transactions.html")

@app.route("/javascript/introduction")
def javascript_intro():
    return render_template("javascript_introduction.html")

@app.route("/javascript/variables")
def javascript_variables():
    return render_template("javascript_variables.html")

@app.route("/javascript/datatypes")
def javascript_datatypes():
    return render_template("javascript_datatypes.html")

@app.route("/javascript/operators")
def javascript_operators():
    return render_template("javascript_operators.html")

@app.route("/javascript/ifelse")
def javascript_ifelse():
    return render_template("javascript_ifelse.html")

@app.route("/javascript/loops")
def javascript_loops():
    return render_template("javascript_loops.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)