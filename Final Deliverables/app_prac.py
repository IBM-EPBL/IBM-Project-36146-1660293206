from flask import Flask, render_template, request

app = Flask(__name__)

import pickle
model = pickle.load(open('model.pkl','rb'))


@app.route('/')
def index():
    return render_template("inputpage.html")

@app.route('/index', methods = ['GET','POST'])
def page():
    a = request.form["temp"]
    b = request.form["DO"]
    c = request.form["PH"]
    d = request.form["conductivity"]
    e = request.form["BOD"]
    f = request.form["NI"]
    g = request.form["Fec_col"]
    h = request.form["Tot_col"]
    i = request.form["year"]
    ip = [[float(a),float(b),float(c),float(d),float(e),float(f),float(g),float(h),int(i)]]
    p = model.predict(ip)
    p=p[0]
    if(p==0):
        output = "The water quality is Very Poor"
    if(p==1):
        output="The water quality is Bad "
    if(p==2):
        output="The water quality is Medium "
    if(p==3):
        output="The water quality is Good"
    if(p==4):
        output="The water quality is Excellent"

    return render_template("inputpage.html", output_text = " Quality of water is {}".format(output))

if __name__ == '__main__' :
    app.run(debug=False)