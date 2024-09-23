include <view_config.scad>
use <obiscad/vector.scad>

*frame();

// Vértices de la pirámide (x, y, z)
vertices = [
    [0, 0, 0],   // Vértice 0 - Esquina de la base
    [10, 0, 0],  // Vértice 1 - Esquina de la base
    [10, 10, 0], // Vértice 2 - Esquina de la base
    [0, 10, 0],  // Vértice 3 - Esquina de la base
    [5, 5, 10]   // Vértice 4 - Cúspide (centro superior)
];

// Caras de la pirámide (definidas por los índices de los vértices)
faces = [
    [0, 1, 4], // Cara lateral 1
    [1, 2, 4], // Cara lateral 2
    [2, 3, 4], // Cara lateral 3
    [3, 0, 4], // Cara lateral 4
    [0, 1, 2, 3] // Base cuadrada
];

// Crear la pirámide
polyhedron(points = vertices, faces = faces);