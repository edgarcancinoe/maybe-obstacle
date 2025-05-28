Ya entonces lo que hicieron fue:

1. Poner un **sigmoide** al final de la red, porque así todas las clases son independientes, es como tener puros **binary classifiers** uno encima del otro.
---
2. El **sigmoide** sirve porque ellos añaden una nueva clase llamada **objectness**, ojo que esta clase no considera todos los objetos de la escena, solamente los que son **obstáculos en la carretera**. Entonces ahora si vemos un auto en la foto, vamos a tener un output alto en la clase **auto**, y también un output alto en la clase **objeto**, lo que viene al pelo porqueeee...
---
3. Se maquinearon una **Score de no identificado**, que es bien fácil: a cada salida del sigmoide, le restas 1 y las multiplicas. Si tienes una clase que es relativamente certera, tipo 0.9 para el auto, el score cae bastante, pero si tienes varias clases ahí medias culeras que la red no tiene claro qué verga, tipo **car 0.5, tree 0.6, box 0.6**, el score va a ser alto.
---
4. Finalmente, combinan estas dos últimas ideas para tener el **score de objeto no identificado**, que es multiplicar el score anterior por la **probabilidad de objeto**, o sea, lo que escupe el sigmoide en la clase **objectness**.
---
5. También pasa que en los **bordes** la red se pone weona porque los objetos están cortados y así, entonces es normal que la red se equivoque y tire probabilidades no tan certeras, esto va a contaminar el **score de objeto no identificado**, lo que causaría que todos los objetos en el borde fueran identificados como un **obstáculo**. Para contrarrestar esto, durante el entrenamiento le pusieron a la función de pérdida **Binary Cross Entropy loss** un **peso extra** para todos los objetos del borde, o sea que si te equivocas en el borde, te castigo más aún. Así la red le pone más atención al borde y no se equivoca tanto, lo que evita la contaminación de la performance del **Score**.