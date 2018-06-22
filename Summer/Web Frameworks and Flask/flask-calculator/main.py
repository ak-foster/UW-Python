import os

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = b'|\xea\xa6!\xb6EL\xc0\x06\xe9,\x94\xbc,\xbf\xc0\x7f!<!\xb7\xe9/\x12'

@app.route('/add', methods=['GET', 'POST'])
def add():
    # session ['total']

    if 'total' not in session:
        session['total'] = 0

    if request.method == 'POST':
        number = int(request.form['number'])
        session['total'] += number

    return render_template('add.jinja2', session=session)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
