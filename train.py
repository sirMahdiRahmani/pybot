import matplotlib.pyplot as plt


numb = []

for i in range(1, 10):
    if i % 3 == 0 or i % 5 ==0:
        numb.append(i)


sum = 0 
for i in numb:
    sum = sum + i

# print (sum)
# print (numb)
plt.show(block= True)
plt.bar(len(numb), numb)