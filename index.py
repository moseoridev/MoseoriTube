from flask import Flask, render_template, request

import parse_url

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def receive():
    url = request.form['yturl']
    p = parse_url.main(url)
    isVLC = any(word in request.headers.get('User-Agent')
                for word in ['iPhone', 'iPad'])

    for f in p['formats']:
        if str(type(f['filesize'])) != '<class \'NoneType\'>':
            f['filesize'] = int(f['filesize'])
        else:
            f['filesize'] = None
        if isVLC:
            f['url'] = 'vlc://' + f['url']

    return render_template('result.html', s=p)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
