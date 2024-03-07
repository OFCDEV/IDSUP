'''Line chart'''
from matplotlib import pyplot
years=[1950,1960,1980,1990,2000,2010]
gdp=[300.2,543.3,1075.9,2062.5,5979.6,10289.7]
pyplot.plot(years, gdp,color='red',marker='o',linestyle='--')
plt.title("Years and GDP")
plt.xlabel('Years')
plt.ylabel('GDP')
plt.show()

movies=['RRR','BAHUBALI','3 IDIOTS','12th FAIL','DRISHYAM']
num_awards=[4,3,15,3,5]
plt.bar(movies,num_awards,color='black')
plt.title("Movies and Awards")
plt.yticks(range(20))
