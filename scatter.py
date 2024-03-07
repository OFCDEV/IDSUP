from matplotlib import pyplot as plt

user = [70,65,72,63,71,64,69,64,67]
minutes = [175,170,205,120,220,130,105,145,190]
website = ['a','b','c','d','e','f','g','h','i']
plt.scatter(user, minutes)
for label,friend_count,minute_count in zip(website,user,minutes):
    plt.annotate(label,xy=(friend_count,minute_count),xytext=(5,-5),textcords='offset point')
