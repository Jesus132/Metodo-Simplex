from flask import Flask, render_template, request
from metodos import Simplex, Simplex1

import forms
app= Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/Simplex2x2.html', methods = ['GET', 'POST'])
def Simpx(t = "", m = "", df = "", grf = ""):
	comment_form = forms.CommentForm1(request.form)
	if request.method =='POST':
		t= Simplex(comment_form.Z.data, comment_form.ecuacion1.data,comment_form.ecuacion2.data).resultado()
	return render_template('Simplex2x2.html', form=comment_form, matriz = t)

@app.route('/Simplex2x3.html', methods = ['GET', 'POST'])
def Simpx2(t = "", m = "", df = "", grf = ""):
	comment_form = forms.CommentForm2(request.form)
	if request.method =='POST':
		t= Simplex1(comment_form.Z.data,comment_form.ecuacion1.data,comment_form.ecuacion2.data,comment_form.ecuacion3.data).resultado1()
	return render_template('Simplex2x3.html', form=comment_form, matriz = t)


if __name__== '__main__':
    app.run(debug = True)
