import numpy as np
def rotation2point(view_x,view_y):
    #obtiene la rotacion adecuada para que el preview tenga como ejes locales view_x y view_y

    pass


def normalize(v):
    """Normaliza un vector para que tenga longitud 1."""
    norm = np.linalg.norm(v)
    return v / norm

def projection(a, b):
    """
    Calcula la proyección del vector a sobre el vector b.
    
    :param a: Vector a (numpy array)
    :param b: Vector b (numpy array)
    :return: Proyección del vector a sobre el vector b (numpy array)
    """
    # Producto escalar de a y b
    dot_product = np.dot(a, b)
    
    # Magnitud de b al cuadrado (b · b)
    b_magnitude_squared = np.dot(b, b)
    
    # Proyección de a sobre b
    projection_ab = (dot_product / b_magnitude_squared) * b
    
    return projection_ab

def generate_coordinate_system(p, segment_x_prime, invert=None):

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


out=(generate_coordinate_system([0,1,0],[[0,0,1],[1,0,0]],invert=True))
#out=(generate_coordinate_system([1,1,0],[[0,0,0],[0,1,0]]))

print("out=",out)

# Ejemplo de uso
original_axes = np.array([[1, 0, 0],  # Eje x original
                          [0, 1, 0],  # Eje y original
                          [0, 0, 1]]) # Eje z original


rotated_axes = np.array([[0, -1, 0],  # Eje x rotado
                         [1,  0, 0],  # Eje y rotado
                         [0,  0, 1]]) # Eje z rotado

rotated_axes = out[1]

rotation_matrix = calculate_rotation_matrix(original_axes, rotated_axes)

print("Matriz de rotación:")
print(rotation_matrix)

from scipy.spatial.transform import Rotation as R

def rotation_matrix_to_euler_angles(rotation_matrix):
    """
    Convierte una matriz de rotación en ángulos de Euler (rotaciones sobre los ejes x, y, z).
    
    :param rotation_matrix: Matriz de rotación 3x3.
    :return: Ángulos de Euler en radianes (rotaciones alrededor de x, y, z).
    """
    r = R.from_matrix(rotation_matrix)
    return r.as_euler('xyz', degrees=True)  # En grados

# Convertir la matriz de rotación a ángulos de Euler
euler_angles = rotation_matrix_to_euler_angles(rotation_matrix)

print("Ángulos de Euler (en grados):", euler_angles)




