from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gapminder')
def gapminder():
    return render_template('gapminder.html')


@app.route('/election')
def election():
    return render_template('election.html')


if __name__ == '__main__':
    app.run()
