import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/mahmoud/Desktop/CTP-BUE/Waleed-Amr/class/output/MG1_background.dat', '/Users/mahmoud/Desktop/CTP-BUE/Waleed-Amr/class/output/MG0_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['MG1_background', 'MG0_background']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'rho_lambda']
tex_names = [u'(8\\pi G/3)rho_lambda']
x_axis = 'z'
ylim = []
xlim = [[0.0, 100.0]]
ax.semilogx(curve[:, 0], curve[:, 11]/curve[:,15])
#ax.semilogx(curve[:, 0], curve[:, 10]/curve[:,15])

index, curve = 1, data[1]
y_axis = [u'rho_lambda']
tex_names = [u'(8\\pi G/3)rho_lambda']
x_axis = 'z'
ylim = []
xlim = [[0.0, 100.0]]
ax.semilogx(curve[:, 0], curve[:, 11]/curve[:,15])
#ax.semilogx(curve[:, 0], curve[:, 10]/curve[:,15])

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('z', fontsize=16)
plt.show()
