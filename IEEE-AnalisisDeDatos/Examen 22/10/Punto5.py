import matplotlib.pyplot as plt 

notas = [1,2,3,4,5,6,7,8,9,10,4,5,6,7,8,4,5,6,7,4,5,6,7,8,9,7,8,6,7,8,6,7,8,7,6,7,8]

plt.subplot(2,2,1)
plt.hist(notas, range(12), align='mid', rwidth=0.75)
plt.subplot(2,2,2)
plt.title('right')
plt.hist(notas, align='right', rwidth=0.5)
plt.subplot(2,2,3)
plt.title('left')
plt.hist(notas, align='left', rwidth=0.5)
plt.subplot(2,2,4)
plt.title('mid')
plt.hist(notas, align='mid', rwidth=0.5)



plt.show()