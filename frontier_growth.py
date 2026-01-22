import matplotlib.pyplot as plt

iterations = list(range(1,11))

# Example values (replace with Java logs if available)
bfs_frontier = [4,6,8,10,12,14,16,18,20,22]
dfs_frontier = [1,1,2,2,3,3,4,4,5,5]
astar_frontier = [3,4,4,5,5,6,6,6,6,6]

plt.figure(figsize=(7,4))
plt.plot(iterations, bfs_frontier, label="BFS", linewidth=2)
plt.plot(iterations, dfs_frontier, label="DFS", linewidth=2)
plt.plot(iterations, astar_frontier, label="A*", linewidth=2)

plt.xlabel("Iteration")
plt.ylabel("Frontier Size")
plt.title("Frontier Growth Over Time")
plt.legend()
plt.grid(True)

plt.savefig("visuals/frontier_growth.png", dpi=300)
plt.show()
