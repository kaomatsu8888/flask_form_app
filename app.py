from flask import Flask, render_template, request  # fappでフォームが出てきます

app = Flask(__name__)


# GETメソッド、POSTメソッドの追記 デフォルトはget
@app.route("/", methods=["GET", "POST"])
def index():
    # もしGETリクエストだった場合はindex.htmlを表示
    if request.method == "GET":
        return render_template("index.html")
    else:
        message = request.form['message']
        return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
