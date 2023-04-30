from flask import Flask, redirect, render_template, request, url_for
import utils
app=Flask(__name__)

@app.route('/')
def home():
   if request.method == 'POST':
        return redirect(url_for('predict', Open=request.form['Open'], High=request.form['High'], Low=request.form['Low'], Volume=request.form['Volume']))
   return render_template('index.html')

@app.route('/predict/', methods=["GET","POST"])
def predict():
   if request.method == "POST":
      Open = request.form.get("Open")
      High=request.form.get("High")
      Low=request.form.get("Low")
      Volume=request.form.get("Volume")
      prediction=utils.preprocess(Open,High,Low,Volume)
   else:
        prediction = 0.0
   return render_template("pred.html",prediction=prediction)
   
if __name__=="__main__":
   app.run(debug=True)