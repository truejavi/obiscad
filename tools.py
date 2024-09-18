from stl import mesh

# Cargar el archivo STL
def obtener_vertices_stl(archivo_stl):
    # Cargar la malla desde el archivo STL
    modelo = mesh.Mesh.from_file(archivo_stl)

    # Crear una lista para almacenar los vértices únicos
    vertices = set()

    # Recorrer todos los vectores en la malla
    for i in range(len(modelo.vectors)):
        # Cada triángulo tiene 3 vértices
        for vertice in modelo.vectors[i]:
            # Añadir cada vértice a la lista de vértices únicos (usamos tupla para que sea hashable)
            vertices.add(tuple(vertice))

    # Convertir el conjunto de vértices únicos en una lista
    return list(vertices)

# Ejemplo de uso
archivo_stl = 'output.stl'  # Ruta al archivo STL
vertices = obtener_vertices_stl(archivo_stl)

# Mostrar la lista de vértices
for vertice in vertices:
    print(vertice)

import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

# Función para visualizar el archivo STL
def visualizar_maya_stl(archivo_stl):
    # Cargar la malla desde el archivo STL
    modelo = mesh.Mesh.from_file(archivo_stl)

    # Configurar el gráfico 3D
    figura = plt.figure()
    grafico_3d = figura.add_subplot(111, projection='3d')

    # Recorrer los triángulos de la malla y agregarlos a la gráfica
    for tri in modelo.vectors:
        triangulo = [[tri[0, 0], tri[0, 1], tri[0, 2]],
                     [tri[1, 0], tri[1, 1], tri[1, 2]],
                     [tri[2, 0], tri[2, 1], tri[2, 2]]]
        triangulo = np.array(triangulo)

        # Crear el triángulo en el gráfico
        grafico_3d.add_collection3d(mplot3d.art3d.Poly3DCollection([triangulo]))

    # Ajustar los límites del gráfico según los límites de la malla
    grafico_3d.auto_scale_xyz(modelo.x.flatten(), modelo.y.flatten(), modelo.z.flatten())

    # Mostrar la visualización
    plt.show()

# Ejemplo de uso
archivo_stl = 'output.stl'  # Ruta al archivo STL
#visualizar_maya_stl(archivo_stl)

import pyvista as pv
from stl import mesh

# Función para visualizar la malla en modo wireframe usando PyVista
def visualizar_malla_stl_pyvista(archivo_stl):
    # Cargar la malla desde el archivo STL
    modelo = mesh.Mesh.from_file(archivo_stl)

    # Crear un objeto PolyData con los puntos y triángulos
    puntos = modelo.points
    caras = np.arange(len(modelo.vectors) * 3).reshape(-1, 3)

    # Crear la malla PyVista
    malla_pv = pv.PolyData(puntos, faces=caras)

    # Crear la ventana de visualización
    plotter = pv.Plotter()
    plotter.add_mesh(malla_pv, style='wireframe', color='black')

    # Mostrar la visualización
    plotter.show()

# Ejemplo de uso
archivo_stl = 'output.stl'  # Ruta al archivo STL
visualizar_malla_stl_pyvista(archivo_stl)

