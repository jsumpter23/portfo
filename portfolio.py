from flask import Flask, render_template, request, url_for, redirect
import csv
app = Flask(__name__)


@app.route('/')
def portfolio_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as db2:
        email = str(data['email'])
        subject = str(data['subject'])
        message = str(data['message'])
        csv_writer = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        db2.close()


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'error'
