import numpy as np
import matplotlib.pyplot as plt

labels = ["Optimality","Speed","Memory","Completeness"]
angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)

bfs = [4,2,1,5]
dfs = [1,3,5,2]
bestf = [2,4,3,3]
astar = [5,4,4,5]

def plot(values, label):
    values += values[:1]
    plt.plot(np.append(angles, angles[0]), values, label=label)
    plt.fill(np.append(angles, angles[0]), values, alpha=0.1)

plt.figure(figsize=(6,6))
plt.subplot(polar=True)

plot(bfs,"BFS")
plot(dfs,"DFS")
plot(bestf,"BestF")
plot(astar,"A*")

plt.xticks(angles, labels)
plt.title("Algorithm Comparison Radar")
plt.legend(loc="upper right")

plt.savefig("visuals/algorithm_radar.png", dpi=300)
plt.show()
