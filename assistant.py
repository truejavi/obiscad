import numpy as np
from scipy.spatial.transform import Rotation as R



def normalize(v):
    """Normaliza un vector para que tenga longitud 1."""
    norm = np.linalg.norm(v)
    return v / norm

def generate_coordinate_system(segment_x_prime, p, invert):

    origin=np.array(segment_x_prime[0])
    end=np.array(segment_x_prime[1])
    p=np.array(p)
    
    # Normalizar el vector del eje x'
    x_prime = normalize(end-origin)
    
    # Calcular el eje z' como el producto vectorial entre x' y el vector origen->p
    z_prime = normalize(np.cross(x_prime, (p-origin)))  
    if invert: z_prime=-z_prime

    # Calcular el eje y' como el producto vectorial entre z' y x'
    y_prime = normalize(np.cross(z_prime, x_prime))

    return origin,  np.array([x_prime, y_prime, z_prime])

def calculate_rotation_matrix(original_axes, rotated_axes):
    """
    Calcula la matriz de rotación entre dos sistemas de coordenadas 3D.
    
    :param original_axes: Matriz 3x3 de los ejes originales (columnas: x, y, z)
    :param rotated_axes: Matriz 3x3 de los ejes rotados (columnas: x, y, z)
    :return: Matriz de rotación que transforma los ejes originales en los ejes rotados.
    """
    # Invertir la matriz de los ejes originales para obtener la transformación inversa
    original_axes_inv = np.linalg.inv(original_axes)
    
    # Multiplicar la matriz de los ejes rotados por la inversa de la original
    rotation_matrix = np.dot(rotated_axes, original_axes_inv)
    
    return rotation_matrix

def rotation_matrix_to_euler_angles(rotation_matrix):
    """
    Convierte una matriz de rotación en ángulos de Euler (rotaciones sobre los ejes x, y, z).
    
    :param rotation_matrix: Matriz de rotación 3x3.
    :return: Ángulos de Euler en radianes (rotaciones alrededor de x, y, z).
    """
    r = R.from_matrix(rotation_matrix)
    return r.as_euler('xyz', degrees=True)  # En grados

def get_transform_x_axis_point_XY(x_axis_segment,point_xy,invert):
    
        
    original_axes = np.array([[1, 0, 0], # Eje x original
                             [0, 1, 0],  # Eje y original
                             [0, 0, 1]]) # Eje z original

    origin,rotated_axes=(generate_coordinate_system(x_axis_segment,point_xy,invert))



    rotation_matrix = calculate_rotation_matrix(rotated_axes,original_axes)



    # Convertir la matriz de rotación a ángulos de Euler
    euler_angles = rotation_matrix_to_euler_angles(rotation_matrix)

    return origin , euler_angles

def set_config_view(traslation=None,rotation=None,perspective=None,distance=None,file_path="view_config.scad"):

    if (rotation is None) and (traslation is None) and (perspective is None) and (distance is None):
        #default
        traslation=[0,0,0]
        rotation=[55,0,25]
        perspective=22.5
        distance=140

    with open(file_path, 'r') as f:
        lineas = f.readlines()


    if (rotation     is  not None): lineas[1]=f'rotation={rotation};\n'
    if (traslation   is  not None): lineas[2]=f'traslation={traslation};\n'
    if (perspective  is  not None): lineas[3]=f'perspective={perspective};\n'
    if (distance     is  not None): lineas[4]=f'distance={distance};\n'


    # Escribir las líneas modificadas de nuevo en el archivo
    with open(file_path, 'w') as f:
        f.writelines(lineas)



#TEST
origin,rot=get_transform_x_axis_point_XY([[0,0,0],[5,5,10]],[10,0,0],invert=True)
origin,rot=get_transform_x_axis_point_XY([[5,5,10],[0,0,0]],[10,0,0],invert=False)
set_config_view(traslation=origin.tolist(), rotation=rot.tolist())
#set_config_view()


