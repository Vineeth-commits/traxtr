import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('data_chart_1.csv','r') as csvfile:
    lines = csv.reader(data_chart.csv, delimiter=',')
    for row in lines:
        y.append(row[0])
        x.append(row[1])
  
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Price Tracker")
  
plt.xticks(rotation = 25)
plt.xlabel('Dates')
plt.ylabel('Price(Inr)')
plt.title('Price Tracker', fontsize = 20)
plt.grid()
plt.legend()
plt.show()
