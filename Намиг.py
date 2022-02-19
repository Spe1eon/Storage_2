from matplotlib import pyplot as plt

fig, ax=plt.subplots()
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
ax.imshow(plt.imread(r'D:\`\Kartino4ki\Namig.png'))
plt.show()