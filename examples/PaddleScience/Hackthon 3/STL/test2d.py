import open3d as o3d
import inflation as inf
import numpy as np

mesh = o3d.io.read_triangle_mesh("./example/2d.stl")

pcs = inf.inflation_sample(
    mesh,
    dis=np.linspace(0.1, 0.5, 4),
    density=np.linspace(10, 5, 4),
    mode="uniform",
    dim=2,
)

o3d.visualization.draw_geometries(pcs, mesh_show_wireframe=True)
