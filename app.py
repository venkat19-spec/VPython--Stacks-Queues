from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('welcome.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('index.html')


@app.route('/stack', methods=['GET', 'POST'])
def stack():
    return render_template("website_stack.html")


@app.route('/stack/queue', methods=['GET', 'POST'])
def queue():
    return render_template("website_queue.html")


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
