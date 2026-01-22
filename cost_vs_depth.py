import matplotlib.pyplot as plt

algorithms = ["BFS","DFS","BestF","A*"]
depth = [5, 18, 7, 5]
cost = [7.28, 145, 40, 7.28]

plt.figure(figsize=(6,5))
plt.scatter(depth, cost, s=100)

for i, alg in enumerate(algorithms):
    plt.text(depth[i]+0.2, cost[i], alg)

plt.xlabel("Solution Depth")
plt.ylabel("Path Cost")
plt.title("Path Cost vs Depth")
plt.grid(True)

plt.savefig("visuals/cost_vs_depth.png", dpi=300)
plt.show()
