
# Road Obstacle Detection based on Unknown Objectness Scores

## Authors
- Chihiro Noguchi, Toshiaki Ohgushi, Masao Yamanaka  
- Toyota Motor Corporation, Tokyo, Japan

## Abstract
The paper introduces a novel approach to detecting road obstacles, specifically targeting the challenge of unknown object detection in autonomous driving. The standard object detection methods fail to recognize unknown objects since they are not part of predefined categories, often labeling them as background. To address this limitation, the authors propose combining pixel-wise anomaly detection with object detection to achieve stable performance.

## Key Points

### 1. Problem Statement
- Autonomous vehicles must detect various road obstacles to ensure safety.  
- Traditional object detection methods, such as Faster R-CNN and YOLOv3, fail to detect unknown objects.  
- Pixel-wise anomaly detection methods are unstable, especially in complex driving scenarios.  

### 2. Proposed Method
- A semantic segmentation network with a **sigmoid head** is used, allowing the assignment of multiple classes to each pixel.  
- The model combines **unknown scores** (from anomaly detection) and **objectness scores** (from object detection) to form an **unknown objectness score**.  
- This score helps to detect road obstacles by identifying areas that are neither background nor predefined objects but still resemble objects.

### 3. Loss Function
- The model incorporates a **Boundary-aware Binary Cross-entropy Loss** to minimize false positives near object boundaries.  
- This loss assigns additional weights to boundary regions, reducing the model's tendency to mistake boundary areas for obstacles.

## Experimental Results
- Datasets used: Cityscapes, LostAndFound, Fishyscapes, Road Anomaly  
- The proposed method consistently outperformed state-of-the-art approaches, especially when integrated with OoD data.  
- Notable improvements in False Positive Rate at 95% True Positive Rate (FPR95) and AUROC metrics.

### Results Summary
| Method              | LostAndFound FPR95 | Fishyscapes AUROC | Road Anomaly AP |
|---------------------|--------------------|-------------------|-----------------|
| Softmax Entropy     | 19.45              | 91.38             | 17.06           |
| Max Logit           | 16.44              | 93.89             | 18.64           |
| Proposed (w/o OoD)  | **3.92**           | **93.81**         | **48.41**       |
| Proposed (w/ OoD)   | **1.17**           | **95.10**         | **49.07**       |

## Strengths and Limitations

### Strengths
- Reduces false positives in background regions.  
- Fast computation, outperforming other methods in speed (around 15 ms per image).  
- Effective use of objectness scores stabilizes detection.  

### Limitations
- Relies on accurate objectness scoring; if obstacles are not recognized as objects, detection fails.  
- Limited by the quality of available road obstacle data.  

## Suggested Sections to Read
1. **Introduction** (Section I) - Overview of problem and motivation.  
2. **Proposed Method** (Section III) - Detailed methodology and loss function.  
3. **Experiments** (Section IV) - Experimental setup, datasets used, and evaluation metrics.  
4. **Results and Analysis** (Section IV-B to IV-F) - Quantitative and qualitative evaluations.  
5. **Conclusions** (Section VI) - Summary and future directions.  

## Conclusion
The study demonstrates the efficacy of combining objectness and anomaly scores for road obstacle detection. The proposed method outperforms existing techniques, both in accuracy and computational efficiency. Future work should focus on generalizing objectness scoring to accommodate a wider range of unknown objects.

