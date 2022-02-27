import cv2
import matplotlib.pyplot as plt
import math
import numpy as np
import open3d as o3d

raw_point_cloud = np.load("sdf.npy")
processed_point_cloud_list = []
for i in range(101):
    for j in range(101):
        for k in range(100):
            if raw_point_cloud[i][j][k][3] * raw_point_cloud[i][j][k+1][3] < 0:
                k_inter_up = raw_point_cloud[i][j][k][2]*raw_point_cloud[i][j][k+1][3] - raw_point_cloud[i][j][k+1][2]*raw_point_cloud[i][j][k][3]
                k_inter_down = raw_point_cloud[i][j][k+1][3] - raw_point_cloud[i][j][k][3]
                k_inter = k_inter_up / k_inter_down
                one_point = [raw_point_cloud[i][j][k][0], raw_point_cloud[i][j][k][1], k_inter]
                processed_point_cloud_list.append(one_point)
for i in range(101):
    for k in range(101):
        for j in range(100):
            if raw_point_cloud[i][j][k][3] * raw_point_cloud[i][j+1][k][3] < 0:
                j_inter_up = raw_point_cloud[i][j][k][1]*raw_point_cloud[i][j+1][k][3] - raw_point_cloud[i][j+1][k][1]*raw_point_cloud[i][j][k][3]
                j_inter_down = raw_point_cloud[i][j+1][k][3] - raw_point_cloud[i][j][k][3]
                j_inter = j_inter_up / j_inter_down
                one_point = [raw_point_cloud[i][j][k][0], j_inter, raw_point_cloud[i][j][k][2]]
                processed_point_cloud_list.append(one_point)
for j in range(101):
    for k in range(101):
        for i in range(100):
            if raw_point_cloud[i][j][k][3] * raw_point_cloud[i+1][j][k][3] < 0:
                i_inter_up = raw_point_cloud[i][j][k][0]*raw_point_cloud[i+1][j][k][3] - raw_point_cloud[i+1][j][k][0]*raw_point_cloud[i][j][k][3]
                i_inter_down = raw_point_cloud[i+1][j][k][3] - raw_point_cloud[i][j][k][3]
                i_inter = i_inter_up / i_inter_down
                one_point = [i_inter, raw_point_cloud[i][j][k][1], raw_point_cloud[i][j][k][2]]
                processed_point_cloud_list.append(one_point)
processed_point_cloud = np.array(processed_point_cloud_list)
np.save("processed_sdf.npy", processed_point_cloud)
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(processed_point_cloud)
o3d.io.write_point_cloud("processed_sdf.ply",pcd)