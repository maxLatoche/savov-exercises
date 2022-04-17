import numpy as np

# P2.2
print("P2.2\n", np.add([1, 0, 1], [0, 2, 2]))

# P2.4
i = [1, 0, 0]
j = [0, 1, 0]
k = [0, 0, 1]

# P2.4a
print("P2.4a\n", np.cross(i, i))

# P2.4b
print("P2.4b\n", np.cross(i, j))

# P2.4c
print("P2.4c\n", np.add(np.cross(np.multiply(-1, i), k), np.cross(j, i)))

# P2.4d
print(
    "P2.4d\n",
    np.add(np.add((np.cross(k, j), np.cross(i, i)), np.cross(j, k)), np.cross(j, i)),
)

# P2.5
v = [2, -1, 3]
w = [1, 0, 1]

# P2.5a
print("P2.5a")
print(np.dot(v, w))
print("the dot product is greater than 0, so the angle is acute (𝚹<pi/2)\n")
# P2.5a
print("P2.5b\n", np.cross(v, w))
# P2.5a
print("P2.5c\n", np.cross(v, v))
# P2.5a
print("P2.5d\n", np.cross(w, w))


# P2.8
u = [1, 0, 1]
v = [1, 2, 0]

print("P2.8\n", np.cross(u, v) / np.linalg.norm(np.cross(u, v)))
print("cross product divided by the length of the cross product (normalized), gives a unit-length vector. -- To find a unit vector with the same direction as a given vector, we divide the vector by its magnitude.\n")
