import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

number_of_frames = 25

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



def update_lines(num, steps, lines):
    for line in lines:
        print('steps', steps[0][num:num+1], steps[1][num:num+1], steps[2][num:num+1])
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data([0, steps[0][num:num+1]], [0, steps[1][num:num+1]])
        line.set_3d_properties([0, steps[2][num:num+1]])
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
    [4, 1, 2],
    [4, 3, 0],
    [1, 2, 4],
])

w = np.matmul(A, v)

# output = Generatestarting_vector(number_of_frames, v, w)
starting_coordinates = [v[0][0], v[1][0], v[2][0]]

# NOTE: Can't pass empty arrays into 3d version of plot()
lines = ax.plot([0, starting_coordinates[0]], [0, starting_coordinates[0]], [0, starting_coordinates[0]])

steps = GenerateSteps(number_of_frames, v, w)

# Setting the axes properties
ax.set_xlim3d([0.0, 8.0])
ax.set_xlabel('X')

ax.set_ylim3d([0.0, 8.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 8.0])
ax.set_zlabel('Z')

ax.set_title('3D Test')

# Creating the Animation object
line_ani = animation.FuncAnimation(fig, update_lines, number_of_frames, fargs=(steps, lines),
                                   interval=100, blit=False)

plt.show()
