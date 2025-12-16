
import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.sin(x)
df = lambda x: np.cos(x)

x = np.linspace(-0.5, 2*np.pi, 400)
y = f(x)

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(x, y, color='dimgray', linewidth=3, label='f(x) = sin(x)')

x0s = [0, np.pi/4, np.pi/2, np.pi, 3*np.pi/2]
colors = ['red', 'green', 'blue', 'magenta', 'cyan']
labels = [
    'Tangente en x=0',
    'Tangente en x=π/4',
    'Tangente en x=π/2',
    'Tangente en x=π',
    'Tangente en x=3π/2'
]

segments = [
    (-0.5, 1.0),
    (0.0, 1.7),
    (0.5, 2.5),
    (2.1, 4.1),
    (3.7, 6.2)
]

for x0, color, label, (xa, xb) in zip(x0s, colors, labels, segments):
    m = df(x0)
    b = f(x0) - m*x0
    xt = np.linspace(xa, xb, 200)
    yt = m*xt + b
    ax.plot(xt, yt, color=color, linewidth=3, label=label)
    ax.scatter([x0], [f(x0)], color=color, s=70, zorder=3)

ax.set_title('Rectas tangentes a f(x) = sin(x)', fontsize=16, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_xlim(-0.5, 2*np.pi)
ax.set_ylim(-1.1, 1.5)
ax.set_xticks(np.arange(0, 7, 1))
ax.set_yticks(np.arange(-1.0, 1.6, 0.5))
ax.grid(True, color='lightgray', alpha=0.7)
ax.legend(loc='upper right', frameon=True)

plt.tight_layout()
plt.show()
