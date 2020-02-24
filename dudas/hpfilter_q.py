import tkinter
import matplotlib
import matplotlib.pyplot as plt


fechas=['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08']
temperaturas=[20,25,30,25,40,30,20,15]

matplotlib.use('TkAgg')
plt.plot(fechas,temperaturas)
plt.show()
