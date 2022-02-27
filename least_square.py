import numpy as np

if __name__ == '__main__':
    point_cloud = np.load("processed_sdf.npy")
    print(point_cloud)
    big_y_list = []
    phi_mat = []
    for point in point_cloud:
        x, y, z = point[0], point[1], point[2]
        phi1, phi2 = x**2*z**3, y**2*z**3
        phi12 = [phi1, phi2]
        big_y = -(2*x**2+y**2+z**2-1)**3
        phi_mat.append(phi12)
        big_y_list.append(big_y)
    X, Y = np.array(phi_mat), np.array(big_y_list)
    a_b_list = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T)
    a_b_list = np.dot(a_b_list, Y)
    print(a_b_list)