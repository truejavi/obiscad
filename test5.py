import pyvista as pv
from stl import mesh
import numpy as np

# Cargar el archivo STL
your_mesh = mesh.Mesh.from_file('output.stl')

# Convertir la malla a formato adecuado para PyVista
points = your_mesh.points.reshape(-1, 3)
faces = np.hstack([np.full((len(points) // 3, 1), 3), np.arange(len(points)).reshape(-1, 3)]).astype(np.int64)

# Crear la malla para PyVista
pv_mesh = pv.PolyData(points, faces)

# Crear el plotter y añadir la malla en modo wireframe
plotter = pv.Plotter()
plotter.add_mesh(pv_mesh, style='wireframe', color='blue', line_width=0.5)

# Función de callback para mostrar coordenadas
def callback(point, picker):
    """ Función que se llama cuando seleccionas un punto en la malla """
    print(f'Punto seleccionado: {point}')

# Activar la opción de seleccionar puntos
plotter.enable_point_picking(callback=callback, show_message=True, use_picker=True)

# Configurar la cámara de manera paramétrica
def set_camera(azimuth=0, elevation=30, distance=5, focal_point=(0, 0, 0)):
    """Controlar el ángulo y la distancia de la cámara"""
    plotter.camera_position = [(distance * np.cos(np.radians(azimuth)), distance * np.sin(np.radians(azimuth)), elevation), 
                               focal_point, 
                               (0, 0, 1)]  # Último vector es 'up', hacia arriba en la escena
    plotter.camera.focal_point = focal_point
    plotter.camera.zoom(1.0)  # Puedes modificar el zoom si es necesario

# Aplicar una configuración inicial de la cámara
set_camera(azimuth=45, elevation=30, distance=10)


# Mostrar la visualización interactiva
plotter.show()
