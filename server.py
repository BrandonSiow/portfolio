from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')  # decorator
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')  # decorator
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writter = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writter.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. try again.'


# @app.route('/index.html')  # decorator
# def my_home2():
#     return render_template('index.html')
#
#
# @app.route('/works.html')  # decorator
# def works():
#     return render_template('works.html')
#
#
# @app.route('/about.html')  # decorator
# def aboutme():
#     return render_template('about.html')
#
#
# @app.route('/contact.html')  # decorator
# def contact():
#     return render_template('contact.html')


@app.route('/blog')  # decorator
def blog():
    return 'This is my thoughts on blogs'


@app.route('/blog/2020/dogs')  # decorator
def blog2():
    return 'This is my dog'


@app.route('/rendertemplate')  # To do this must import render_template from Flask. Then must put all the html in a templates folder.
def rendertemplate():
    return render_template('index_trial.html')


@app.route('/aboutme')  # To do this must import render_template from Flask. Then must put all the html in a templates folder.
def rendertemplate2():
    return render_template('about_trial.html')


@app.route('/<username>/<int:post_id>')
def rendertemplate3(username=None, post_id=None):
    return render_template('index_trial.html', name=username, post_id=post_id)
