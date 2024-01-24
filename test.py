from subdivision import *
from halfedge_mesh import * 

data_path = 'tests/data/bunny.off'

# HalfedgeMesh
mesh = HalfedgeMesh(data_path)

for vertex in mesh.vertices:
    print(vertex.get_vertex())

def save_halfmesh_as_obj(mesh, file_name):
    with open(file_name, 'w') as open_file:
        for vertex in mesh.vertices:
            lv = vertex.get_vertex()
            open_file.write("v {} {} {} \n".format(lv[0], lv[1], lv[2]))

        for face in mesh.facets:
            open_file.write("f {} {} {}\n".format(face.a+1, face.b+1, face.c+1))

save_halfmesh_as_obj(mesh, 'bunny.obj')

#First Iteration
new_mesh = binary_loop_subdivision(mesh)
save_halfmesh_as_obj(new_mesh, 'bunny1.obj')

#Second Iteration
new_mesh2 = binary_loop_subdivision(new_mesh)
save_halfmesh_as_obj(new_mesh2, 'bunny2.obj')