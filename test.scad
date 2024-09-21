//control de la camara
$vpr = [55.0, 0, 25.0];   // Rotación de la cámara
$vpt = [70, 0, 0];   // Traslación de la cámara
$vpf = 22.5;           // Factor de perspectiva
$vpd = 300;           // Distancia de la cámara

// Ejemplo de objeto
//cube([20, 10, 10]);




      //example polygon with multiple holes
a0 = [[0,0],[100,0],[130,50],[30,50]];     // main
b0 = [1,0,3,2];
a1 = [[20,20],[40,20],[30,30]];            // hole 1
b1 = [4,5,6];
a2 = [[50,20],[60,20],[40,30]];            // hole 2
b2 = [7,8,9];
a3 = [[65,10],[80,10],[80,40],[65,40]];    // hole 3
b3 = [10,11,12,13];
a4 = [[98,10],[115,40],[85,40],[85,10]];   // hole 4
b4 = [14,15,16,17];
a  = concat (a0,a1,a2,a3,a4);
b  = [b0,b1,b2,b3,b4];
//polygon(a,b);
      //alternate 
linear_extrude(height=10)
rotate([0,0,0]){
   polygon(a,[b0,b1,b2,b3,b4]);
   }

