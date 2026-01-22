import matplotlib.pyplot as plt
import math

expanded = [
    (2,45),(2,90),(2,0),(1,45),(3,45),
    (2,135),(1,90),(3,90)
]

r = [p[0] for p in expanded]
theta = [math.radians(p[1]) for p in expanded]

plt.figure(figsize=(6,6))
ax = plt.subplot(111, polar=True)

ax.scatter(theta, r, color='gray', alpha=0.4, label="Expanded States")
ax.set_thetagrids(range(0,360,45))
ax.set_rmax(5)
ax.grid(True)

plt.title("Search Expansion Pattern (BFS)")
plt.legend()
plt.show()
