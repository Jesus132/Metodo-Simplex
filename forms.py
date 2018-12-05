from wtforms import Form, TextField, FloatField, IntegerField

class CommentForm1(Form):
	Z= TextField('Digite Z:')
	ecuacion1= TextField('Digite la ecuacion1:')
	ecuacion2= TextField('Digite la ecuacion2:')
	
	
class CommentForm2(Form):
	Z= TextField('Digite Z:')
	ecuacion1 = TextField('Digite la ecuacion1:')
	ecuacion2 = TextField('Digite la ecuacion2:')
	ecuacion3 = TextField('Digite la ecuacion3:')
	