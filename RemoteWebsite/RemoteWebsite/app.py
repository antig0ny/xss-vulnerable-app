from flask import Flask, render_template, request

app = Flask(__name__)
recorded_cookies = []

@app.route('/')
def index():
    # Cookie is delivered to the site by setting the url parameter 'cookie'
    cookie = request.args.get('cookie')
    # If the cookie exists, it is added to storage
    if cookie:
        recorded_cookies.append(cookie)
    return render_template('index.html', recorded_cookies=recorded_cookies)

if __name__ == '__main__':
    app.run('localhost', 5000)
