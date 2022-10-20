from flask import Flask,render_template,request,abort,redirect
import csv

app = Flask(__name__)

@app.errorhandler(500)
def server_error(error):

    return render_template('500.html')

@app.errorhandler(404)
def page_not_found(error):

    return render_template('404.html/error_handling.html')



@app.route("/")
def home():
    abort(500)
    return render_template('index.html')



@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_csv_files(data)
        return redirect('thankyou.html')
    else:
        return 'something went wrong'

def write_csv_files(data):
    with open('server/database.csv', newline='', mode='a') as csv_file:
        email= data['email']
        name=data['name']
        message=data['message']
        csv_file_writer=csv.writer(csv_file, delimiter = ",", quotechar=" ", quoting=csv.QUOTE_MINIMAL)
        csv_file_writer.writerow([email,name,message])




