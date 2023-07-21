from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/products.html')
def products():
    return render_template('products.html')

@app.route('/store.html')
def store():
    return render_template('store.html')


@app.route('/css/<path:filename>')
def serve_css(filename):
    return send_from_directory('static/css', filename)

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('static/js', filename)

@app.route('/assets/<path:filename>')
def serve_assets(filename):
    return send_from_directory('static/assets', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
