from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.form
    num_items = int(data['strawberry']) + \
        int(data['raspberry']) + int(data['apple'])
    now = datetime.datetime.now()
    day = now.strftime("%x")
    time = now.strftime("%X")
    print(f"Charging {data['first_name']} for {num_items} fruits")
    return render_template("checkout.html", data=data, num_items=num_items, day=day, time=time)


@app.route('/fruits')
def fruits():
    return render_template("fruits.html")


if __name__ == "__main__":
    app.run(debug=True)
