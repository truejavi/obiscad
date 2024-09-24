import pyvista as pv
from pyvista.plotting.opts import ElementType

# Crear una malla
mesh = pv.Wavelet()

# Crear el visualizador
pl = pv.Plotter()
pl.add_mesh(mesh, show_edges=True, pickable=True)


# Asegurarse de que no hay selección habilitada antes de activar la selección de caras
pl.disable_picking()

face=True

# Función para obtener y mostrar características de la cara seleccionada
def on_pick_face(picked_element):
    if picked_element != -1:
        # Pasar el índice de la celda seleccionada como una lista
        print(picked_element.points)

        # Pasar el índice de la celda seleccionada como una lista
        #selected_cells = [picked_cell_id]
        
        # Obtener la celda seleccionada
        #selected_cell = mesh.extract_cells(selected_cells)
        #print(selected_cell)
        
        if len(picked_element.points)==4:    
            pl.disable_picking()
            pl.enable_element_picking(mode=ElementType.EDGE, callback=on_pick_face)
            face=False
        else:   
            pl.disable_picking()
            pl.enable_element_picking(mode=ElementType.FACE, callback=on_pick_face)
            face=True

# Habilitar la interacción de selección de caras
pl.enable_element_picking(mode=ElementType.FACE, callback=on_pick_face)



# Mostrar la ventana interactiva
pl.show(auto_close=False)

