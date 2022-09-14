from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    # Displayed message relies on url parameter 'name', set by form submission
    if request.args.get('name'):
        message = 'There we go! Nice to meet you, ' + request.args['name'] + '.'
    else:
        message = 'Still waiting...'
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run('localhost', 4449)
