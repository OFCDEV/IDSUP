from matplotlib import pyplot as plt
from collections import Counter
grades = [83,95,87,70,0,85,82,100,67,73,77,0]
lst=[min(grade//10*10,90)for grade in grades]
print(lst)
histogram = Counter(lst)
print(histogram)