from flask import Flask, request, render_template, make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    name = request.args.get('name', '')
    csp = "default-src 'self'"
    if request.method == 'POST':
        csp = request.form.get('csp', csp)

    response = make_response(render_template('index.html', csp=csp, name=name))
    response.headers['Content-Security-Policy'] = csp
    return response

if __name__ == '__main__':
    app.run(debug=True)
