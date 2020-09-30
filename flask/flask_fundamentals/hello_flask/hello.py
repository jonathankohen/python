from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)


@app.route('/play/<num>')
def playRepeat(num):
    return render_template("play.html", times=int(num))


@app.route('/say/<name>')
def show_name(name):
    print(name)
    return f"Hi {name}!"


@app.route('/repeat/<num>/<string>')
def repeatString(num, string):
    output = int(num) * string
    return output


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]
    return render_template("lists.html", random_numbers=[3, 1, 5], students=student_info)


@app.route('/users')
def render_users():
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
    return render_template("users.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)
