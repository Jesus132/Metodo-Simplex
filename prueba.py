import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as animation
import mpld3
from metodos import Newton
tabla, men, df, ani = Newton().resultado()
print("\nf'(x)=",df)
print(tabla,men)
mpld3.show()