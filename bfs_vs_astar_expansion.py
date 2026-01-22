import matplotlib.pyplot as plt
import math

# ===== Replace with your Java expanded states =====
bfs_expanded = [
    (2,45),(2,90),(2,0),(1,45),(3,45),
    (2,135),(1,90),(3,90),(2,315)
]

astar_expanded = [
    (2,45),(2,90),(2,135),(2,180),(2,225),(3,225)
]

def plot(ax, data, title, color):
    r = [p[0] for p in data]
    theta = [math.radians(p[1]) for p in data]
    ax.scatter(theta, r, color=color, alpha=0.6)
    ax.set_thetagrids(range(0,360,45))
    ax.set_rmax(5)
    ax.set_title(title)
    ax.grid(True)

fig, axs = plt.subplots(1,2, subplot_kw={'polar':True}, figsize=(10,5))

plot(axs[0], bfs_expanded, "BFS Expansion", "gray")
plot(axs[1], astar_expanded, "A* Expansion", "green")

plt.tight_layout()
plt.savefig("visuals/bfs_vs_astar_expansion.png", dpi=300)
plt.show()
