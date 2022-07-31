import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

def GenerateSteps(frames, starting_vector, ending_vector):
    # arg 1 === 3 dimensional
    # add two to each frame to account for starting frame
    line_data = np.empty((len(starting_vector), frames + 1))
    for index, value in enumerate(starting_vector):
        line_data[index] = value

        delta = ending_vector[index] - value
        step = delta / frames
        print(line_data[index])
        for frame in range(frames):
            print(line_data[index, frame])
            line_data[index, frame + 1] = line_data[index, frame] + step

    return line_data


# NOTE: other_updates is a list of tuples, with a function to be called and the frame it should be called in
def update_lines(num, steps, lines, *other_updates):
    print('steps', steps)
    for update in other_updates:
        (func, frame) = update
        if (frame == num):
            func()

    if (num > 29 and num < 61):
        step_index = num - 30
        for line in lines:
            # NOTE: there is no .set_data() for 3 dim data...
            line.set_data([0, steps[0][step_index:step_index+1]], [0, steps[1][step_index:step_index+1]])
            line.set_3d_properties([0, steps[2][step_index:step_index+1]])
    return lines

# Attaching 3D axis to the figure
fig = plt.figure()
ax = p3.Axes3D(fig)

v = np.array([
    [1],
    [1],
    [1]
])


A = np.array([
    [4, 1, 0],
    [4, 3, 0],
    [1, 2, 0],
])

w = np.matmul(A, v)

# output = Generatestarting_vector(number_of_frames, v, w)
starting_coordinates = [v[0][0], v[1][0]]

# NOTE: Can't pass empty arrays into 3d version of plot()
lines = ax.plot([0, starting_coordinates[0]], [0, starting_coordinates[0]], [0, starting_coordinates[0]])

steps = GenerateSteps(30, v, w)

# Setting the axes properties
ax.set_xlim3d([0.0, 8.0])
ax.set_xlabel('X')

ax.set_ylim3d([0.0, 8.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 8.0])
ax.set_zlabel('Z')

ax.set_title('3D Test')

def show_exerted_forces():
    x1 = [0, A[0,0]]
    y1 = [0, A[1,0]]
    z1 = [0, A[2,0]]
    x2 = [0, A[0,1]]
    y2 = [0, A[1,1]]
    z2 = [0, A[2,1]]
    # x3 = [0, A[0,2]]
    # y3 = [0, A[1,2]]
    # z3 = [0, A[2,2]]

    ax.plot(x1, y1, z1)
    ax.plot(x2, y2, z2)
    # ax.plot(x3, y3, z3)



# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_lines, 90, fargs=(steps, lines, (show_exerted_forces, 30)),
                                   interval=100, blit=False)

line_ani.save('Fundamental Spaces/matrix-vector2.gif', writer='imagemagick', fps=30)

# plt.show()
