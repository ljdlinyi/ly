from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    # 这里可以放置一些逻辑，然后重定向到 hacker.html 页面
    return redirect(url_for('hacker'))

@app.route('/hacker')
def hacker():
    return render_template('hacker.html')

if __name__ == '__main__':
    app.run(debug=True)