from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")

minutes = list(range(1,10))

dev1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
dev2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
dev3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['Developer 1', 'Developer 2', 'Developer 3']
colors = ['#6d905f', '#fc4f30', '#008fd5']

plt.stackplot(minutes, dev1, dev2, dev3, labels=labels, colors=colors)

plt.legend(loc=(0.07, 0.05))

plt.title("Development Hours by Developer")
plt.tight_layout()
plt.show()