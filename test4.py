import sys
import numpy as np
from PyQt5 import QtWidgets
from pyvistaqt import QtInteractor
import pyvista as pv
from stl import mesh

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        # Crear el widget central
        self.frame = QtWidgets.QFrame()
        self.layout = QtWidgets.QVBoxLayout()
        
        # Crear el widget de PyVista dentro de la ventana Qt
        self.plotter = QtInteractor(self.frame)
        self.layout.addWidget(self.plotter.interactor)

        # Añadir un botón
        self.button = QtWidgets.QPushButton("Vista predeterminada")
        self.button.clicked.connect(self.set_camera_view)
        self.layout.addWidget(self.button)

        self.frame.setLayout(self.layout)
        self.setCentralWidget(self.frame)

        # Inicializar lista de puntos resaltados
        self.highlighted_points = []

        # Configuración de la malla STL
        self.setup_scene()

    def setup_scene(self):
        # Cargar el archivo STL
        your_mesh = mesh.Mesh.from_file('archivo.stl')

        # Convertir la malla a formato adecuado para PyVista
        points = your_mesh.points.reshape(-1, 3)
        faces = np.hstack([np.full((len(points) // 3, 1), 3), np.arange(len(points)).reshape(-1, 3)]).astype(np.int64)

        # Crear la malla para PyVista
        self.pv_mesh = pv.PolyData(points, faces)

        # Añadir la malla al widget de PyVista
        self.plotter.add_mesh(self.pv_mesh, style='wireframe', color='blue', line_width=0.5)

        # Configurar la cámara inicial
        self.plotter.camera_position = 'xy'  # Vista desde el eje xy
        self.plotter.show()

        # Activar la opción de seleccionar puntos
        self.plotter.enable_point_picking(callback=self.callback, show_message=True, use_picker=True)

    def set_camera_view(self):
        """Función que ajusta la cámara a una vista predeterminada"""
        self.plotter.camera_position = [(10, 10, 10), (0, 0, 0), (0, 0, 1)]
        self.plotter.render()  # Actualizar la visualización

    def callback(self, point, picker):
        """Función que se llama cuando seleccionas un punto en la malla"""
        print(f'Punto seleccionado: {point}')
        self.highlight_point(point)

    def highlight_point(self, point):
        """Resaltar el punto seleccionado"""
        # Añadir el punto a la lista de puntos resaltados
        self.highlighted_points.append(point)

        # Crear un objeto de puntos resaltados
        highlighted_points = pv.PolyData(np.array(self.highlighted_points))

        # Añadir los puntos resaltados a la visualización
        self.plotter.add_mesh(highlighted_points, color='red', point_size=10, render_points_as_spheres=True)

        # Actualizar la visualización
        self.plotter.render()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
