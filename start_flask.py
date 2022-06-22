from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    hello = 'mama miya'
    return render_template('url_1.html', text=hello)


@app.route('/users/')
def main2():
    users = ['ann', 'olga', 'mark']
    return render_template('url_2.html', users=users)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)





