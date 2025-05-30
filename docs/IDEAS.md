# Ideas de qué hacer

## ¿Qué dice la descripción del proyecto?
- Desarrollar un framework general, independiente del modelo, para identificar obstáculos en calles, partiendo desde el output de cualquier red de segmentación semántica.
- Enfocarse en segmentación semántica consciente de anomalías para detectar obstáculos fuera de las clases predefinidas, permitiendo identificar obstáculos desconocidos como parte del output.
- Implementar Conformal Prediction para tener garantías estadísticas de la confiabilidad de las predicciones.

### Objetivos principales:
- **Segmentación de obstáculos con detección de anomalías:** Integrar en un modelo de segmentación semántica técnicas que permitan detectar obstáculos que no pertenezcan a las clases conocidas.
- **Cuantificación estadística de la incertidumbre:** Obtener salidas de segmentación semántica y propuestas de obstáculos con garantías sobre la fiabilidad de la detección.
- **Evaluación integral:** Evaluar el sistema utilizando tanto métricas de rendimiento en detección como métricas de incertidumbre.

Entonces, en corto:

1. Aplicar algún método o combinación de métodos de **anomaly detection** sobre los outputs softmax de cualquier modelo de segmentación. Así, generaremos en el output una predicción de objetos desconocidos más la predicción por clases. *(No podemos aplicar directamente el Unknown Object Score del paper 1 porque está basado en una red modificada con cabeza sigmoide y entrenada con una función de pérdida especial. Si hacemos esto, perdemos el requerimiento de ser model-agnostic.)*

2. Aplicar **Conformal Risk Control** del segundo paper directamente. Hay que ver cómo incluir la predicción de objetos desconocidos.  
   Aquí las implementaciones:  
   - https://github.com/aangelopoulos/conformal-prediction  
   - https://github.com/deel-ai-papers/conformal-segmentation

3. Hacer benchmark, validar, etc.

---

### Propuesta

0. Revisar este paper: [Segment Every Out-of-Distribution Object](https://arxiv.org/pdf/2311.16516)  
   Lo que hace es:
   - Utiliza cualquier método de anomaly detection (MSP, Softmax Entropy, Energy-based Score, etc.) para generar un mapa de anomalías (una medida de anómalo por cada píxel).
   - Le pasa ese mapa a una red que detecta el objeto y le dibuja una cajita alrededor (nosotros tendríamos que entrenar esta red).
   - Le pasa esa cajita como prompt a una SAM (modelo de segmentación universal de Meta AI).
   - SAM escupe un objeto perfectamente segmentado.

Entonces, la propuesta ahora sí es:

1. Usamos **Conformal Risk Control** como método de anomaly detection. La cantidad de clases por píxel sería nuestra medida de anomalía.
2. Usamos el pipeline del paper *Segment Every Out-of-Distribution Object* para obtener una segmentación precisa del objeto.
3. Ahora que tenemos los píxeles exactos del objeto, recuperamos desde el mapa de anomalías las medidas del Conformal Risk Control para agruparlas y generar una medida general de confianza de que nos encontramos frente a un objeto desconocido.
4. El único detalle es que aún no estamos considerando si este objeto es un obstáculo; es decir, estamos segmentando cualquier objeto no identificado en la imagen. Pero creo que con un filtro geométrico al inicio o final del pipeline, o alguna estrategia simple, se puede sobrellevar. Igual, siempre es interesante identificar objetos raros.





