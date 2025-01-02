import numpy as np

def get_angle(x, y, x_center, y_center, radius):
    adjacent = x - x_center
    angle = np.arccos(adjacent / radius)

    print('angle1', angle)
    print('angle1', np.rad2deg(angle))

    # 2pi radians is an entire revolution around the circle
    # I think this flips the angle if the slope is negative?
    if y - y_center < 0:
        angle = 2*np.pi - angle
    print('angle2', angle)
    print('angle2', np.rad2deg(angle))

    print('theta=', angle, ',angle in degree=', np.rad2deg(angle), '\n')
    return angle