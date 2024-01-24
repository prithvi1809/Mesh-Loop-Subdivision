from halfedge_mesh import *
import numpy as np

def midpoint(v1, v2):
    x = (v1.x + v2.x) / 2
    y = (v1.y + v2.y) / 2
    z = (v1.z + v2.z) / 2
    return [x, y, z]

def adjacent_vertices(mesh, vertex):
    adj_vertices = []
    start_halfedge = vertex.halfedge
    traversal_edge = start_halfedge
    
    if(not traversal_edge or not traversal_edge.opposite):
            return adj_vertices
    #traversal_edge = traversal_edge.opposite
    print("start point :", vertex.index)
    len = 0
    while len<30:
        traversal_edge = traversal_edge.opposite
        if(not traversal_edge):
             return adj_vertices
        #print("getting into this loop.........................................")
        v = traversal_edge.vertex
        print("neighbor point :", v.index)
        if(v not in adj_vertices):
            adj_vertices.append(v)
        traversal_edge = traversal_edge.next
        if(traversal_edge==start_halfedge):
             break
        len+=1
        
    return adj_vertices

def update_old_vertices(mesh, vertices):
    new_vertices = []
    for vertex in vertices:
        neighbor_vertices = adjacent_vertices(mesh, vertex)
        n = len(neighbor_vertices)

        if(not vertex.halfedge.opposite or n==0):
            new_pos = 3/4*(np.array(vertex.get_vertex())) + 1/8*(np.array(vertex.halfedge.next.vertex.get_vertex()) + np.array(vertex.halfedge.next.next.vertex.get_vertex()))
            
        else:
            print("N----------------------------------------------------------------------------------------", n)

            if n == 3:
                beta = 3 / 16
            elif n < 3:
                beta = 3 / (8*n)
            else:
                beta = 1/n * (5/8 - (3/8 + 0.5 * np.cos(2 * np.pi / n))**2)
            
            new_pos = (1.0 - n * beta) * np.array(vertex.get_vertex())
            
            for neighbor in neighbor_vertices:
                new_pos += beta * np.array(neighbor.get_vertex())
        
        #vertex.x, vertex.y, vertex.z = new_pos[0], new_pos[1], new_pos[2]
        new_v1 = Vertex(new_pos[0], new_pos[1], new_pos[2], index = vertex.index)
        new_vertices.append(new_v1)
    
    return new_vertices

def update_edge_faces(mesh):
    Edges = {}
    facets = []
    halfedge_count = 0

    vertex_map = {}
    #create vertex map
    for i,v in enumerate(mesh.vertices):
         vertex_map[i] = v


    # For each facet
    for index in range(len(mesh.facets)):
      
        # TODO: make general to support non-triangular meshes
        # Facets vertices are in counter-clockwise order
        facet = mesh.facets[index]
        print("f------------------------------------------------------------")
        facet.index = index
        print(facet.get_face()[0], facet.get_face()[1], facet.get_face()[2], facet.index)

        # create pairing of vertices for example if the vertices are
        # verts = [1,2,3] then zip(verts, verts[1:]) = [(1,2),(2,3)]
        # note: we skip line[0] because it represents the number of vertices
        # in the facet.
        #return a list of index values of 3 vertices in that face [0 1 3] 
        fverts = facet.get_face()
        

        all_facet_edges = list(zip(fverts, fverts[1:]))
        all_facet_edges.append((fverts[2],  fverts[0]))
        
        for i in range(3):
            
            Edges[all_facet_edges[i]] = Halfedge()
            Edges[all_facet_edges[i]].facet = facet
            Edges[all_facet_edges[i]].vertex = vertex_map[
                all_facet_edges[i][0]]
            vertex_map[all_facet_edges[i][0]].halfedge = Edges[all_facet_edges[i]]
            halfedge_count +=1
    
        facet.halfedge = Edges[all_facet_edges[0]]
        print("facet-------------------------------------", facet)

        facets.append(facet)

        for i in range(3):
            Edges[all_facet_edges[i]].next = Edges[
                all_facet_edges[(i + 1) % 3]]
            Edges[all_facet_edges[i]].prev = Edges[
                all_facet_edges[(i - 1) % 3]]

            # reverse edge ordering of vertex, e.g. (1,2)->(2,1)
            if all_facet_edges[i][2::-1] in Edges:
                Edges[all_facet_edges[i]].opposite = \
                    Edges[all_facet_edges[i][2::-1]]

                Edges[all_facet_edges[i][2::-1]].opposite = \
                    Edges[all_facet_edges[i]]
    return Edges, facets

    
def binary_loop_subdivision(mesh):
    #old_vertices = list(mesh.vertices)  # Start with the old vertices
    new_vertices = []
    #new_halfedges = []
    new_facets = []
    new_edges = {}
    
    # Initialize a variable to keep track of the index for new vertices
    new_vertex_index = len(mesh.vertices)
    new_face_index = 0

    for facet in mesh.facets:
        # Get the vertices of the original triangle
        v1 = facet.halfedge
        v2 = facet.halfedge.next
        v3 = facet.halfedge.next.next
        #print("v1 {} {} v2 {} {} v3 {} {}".format(v1.vertex.get_vertex(), v1.vertex.index, v2.vertex.get_vertex(), v2.vertex.index, v3.vertex.get_vertex(), v3.vertex.index))
        print("v1 ", v1.vertex.index, "v1 next ", v1.next.vertex.index)
        print("v2 ", v2.vertex.index, "v2 next ", v2.next.vertex.index)
        print("v3 ", v3.vertex.index, "v3 next ", v3.next.vertex.index)

        
        #Checking boundary condition
        m1 = midpoint(v1.vertex, v2.vertex)
        m2 = midpoint(v2.vertex, v3.vertex)
        m3 = midpoint(v3.vertex, v1.vertex)
        
        # Create new vertices with index values
        new_v1 = Vertex(m1[0], m1[1], m1[2])
        new_v2 = Vertex(m2[0], m2[1], m2[2])
        new_v3 = Vertex(m3[0], m3[1], m3[2])

        # Append only the unique new vertices
        for new_vertex in [new_v1, new_v2, new_v3]:
            is_duplicate = False
            for existing_vertex in new_vertices:
                if new_vertex.get_vertex() == existing_vertex.get_vertex():
                    is_duplicate = True
                    new_vertex.index = existing_vertex.index
                    break
            if not is_duplicate:
                new_vertex.index = new_vertex_index
                new_vertex_index += 1
                new_vertices.append(new_vertex)


        # Create new facets
        new_facet1 = Facet(v1.vertex.index, new_v1.index, new_v3.index)
        new_facet2 = Facet(new_v1.index, v2.vertex.index, new_v2.index)
        new_facet3 = Facet(new_v2.index, v3.vertex.index, new_v3.index)
        new_facet4 = Facet(new_v1.index, new_v2.index, new_v3.index)

        new_facets.extend([new_facet1, new_facet2, new_facet3, new_facet4])
    #Update old vertices
    updated_old_vertices = update_old_vertices(mesh, mesh.vertices)
    
    updated_old_vertices.extend(new_vertices)
    
    new_mesh = HalfedgeMesh(vertices=updated_old_vertices, facets=new_facets, halfedges=new_edges)

    new_mesh.edges, new_mesh.facets = update_edge_faces(new_mesh)
    return new_mesh
