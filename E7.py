import numpy as np

# E7.6
a = np.array([
    [0,1,0],
    [0,0,1],
    [1,1,0],
])

b = np.array([
    [0,1,0],
    [0,1,1],
    [0,0,0],
])

c = np.array([
    [0,1,1],
    [1,0,1],
    [1,1,0],
])

print('E7.6a\n', a)
print('E7.6b\n', b)
print('E7.6c\n', c)

# E7.7
a_connectivity_graph = np.add(np.add(np.identity(3), a), np.linalg.matrix_power(a, 2))
b_connectivity_graph = np.add(np.add(np.identity(3), b), np.linalg.matrix_power(b, 2))
c_connectivity_graph = np.add(np.add(np.identity(3), c), np.linalg.matrix_power(c, 2))
print('E7.7a\n', a_connectivity_graph[0, 2])
print('E7.7b\n', b_connectivity_graph[0, 2])
print('E7.7c\n', c_connectivity_graph[0, 2])

