import statsmodels.api as sm
import pandas as pd
import tkinter
import matplotlib
import matplotlib.pyplot as plt


matplotlib.use('TkAgg')

fechas=['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05', '2020-01-06', '2020-01-07', '2020-01-08']
temperaturas={'temperatura':[20,25,30,25,40,30,20,15]}
dta = pd.DataFrame(temperaturas)
print(dta)

index = pd.DatetimeIndex(fechas, freq ='D',tz ='America/Costa_Rica') 
dta.set_index(index, inplace=True)
cycle, trend = sm.tsa.filters.hpfilter(dta.temperatura, 1600)
gdp_decomp = dta[['temperatura']]
gdp_decomp["cycle"] = cycle
gdp_decomp["trend"] = trend

fig, ax = plt.subplots()
gdp_decomp[["temperatura", "trend"]]["2020-01-01":].plot(ax=ax,fontsize=16)
plt.show()
