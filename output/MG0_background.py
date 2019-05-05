import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/mahmoud/Desktop/CTP-BUE/Waleed-Amr/class/output/MG0_background.dat', '/Users/mahmoud/Desktop/CTP-BUE/Waleed-Amr/class/output/MG2_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['MG0_background', 'MG2_background']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'H[1/Mpc]']
tex_names = ['H [1/Mpc]']
x_axis = 'z'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 3]))

index, curve = 1, data[1]
y_axis = [u'H[1/Mpc]']
tex_names = ['H [1/Mpc]']
x_axis = 'z'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 3]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('z', fontsize=16)
plt.show()