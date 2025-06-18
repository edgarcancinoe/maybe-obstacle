# Uncertainty-Aware Road Obstacle Identification

### Project Task

The aim of this project is to develop a general, model-agnostic framework for road obstacle identification based on semantic segmentation outputs. The system will focus on anomaly-aware semantic segmentation to detect obstacles outside predefined classes. Additionally, the framework will integrate uncertainty quantification using Conformal Prediction methods, providing formal statistical guarantees regarding detection reliability.

## Main Objectives

1. **Anomaly-Aware Obstacle Segmentation**: Integrate techniques within a semantic segmentation model to detect obstacles that fall outside known classes.
2. **Statistical Uncertainty Quantification**: Use conformal prediction methods to ensure reliable detection metrics.
3. **Comprehensive Evaluation**: Benchmark the system using both detection performance and uncertainty metrics.

## Pipeline (TOVERIFY)

In this prohject we did 3 main tasks:

- **Train a model to recognize road objects**: Fine tune an existing object recognition model to perform on vehicle POV, capturing surrounding data. We now can identify up to 32 objects (Cityscapes label map).
  - **Unknown Score**: For each pixel, if it’s low probability for all known classes, it’s likely unknown.
  - **Objectness Score**: For each pixel, probability of being an object (merging all known object classes into one “object” class).
  - **Unknown Objectness Score (UOS)**: Multiply unknown and objectness scores for each pixel.
    - **High UOS** = probably an unknown obstacle.
- **Focus on object-like pixels**: Group the object labels into a _smaller label map_, grouping objects and filtrating background elements. We now can predict if a pixel belongs to an object-like class or background class.

  - Boundarys were misunderstood and recognized as unknown, getting higher unknown score, even though they’re not objects.
  - We re-trained the model to be more careful on predicted object borders, resulting in a reduction in unknowness score on boundaries.
  - We rose the threshold of what to be considered an object based on UOS score, to minimize false positives.

- **Evaluate with Conformal Risk Control**: To further improve reliability, we implemented Conformal Risk Prediction, based on the papers Conformal Semantic Image Segmentation: Post-hoc Quantification of Predictive Uncertainty. and A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification.

  - Combined with the the _UOS_, conformal prediction allows to put a statistically valid confidence interval on unknown obstacle detection, or mark pixels/objects as “uncertain” with rigorous coverage guarantees.

## What we accomplished (TOVERIFY)

Applying a threshold to the _UOS_ enables detection of unknown obstacles while minimizing false positives from the background, calibrating the detection threshold to ensure the false negative rate stays below the desired level. The end results demonstrate that CRC reduces missed detections of small and rare obstacles while maintaining robust performance. This pipeline enables statistically valid, uncertainty-aware road obstacle detection and sets a new standard for safe deployment in real-world environments.

### Results

- Object detection on vehicles dataset
- Object detection using **_UOS_** with a threshold > 0.5
- Minimization of False Negatives using CRC

## How to Run (TODO)

This project consists of 2 main Jupyter Notebooks

- **UAROI_Conformal_Risk_Control_Evaluation**
  - asd
- UAROI_Training

## References

### Academic Papers

1. Noguchi, C., Ohgushi, T., & Yamanaka, M. (2024). Road Obstacle Detection based on Unknown Objectness Scores. arXiv [Cs.CV].
2. Mossina, L., Dalmau, J., & Andéol, L. (2024). Conformal Semantic Image Segmentation: Post-hoc Quantification of Predictive Uncertainty. arXiv [Cs.CV].
3. Angelopoulos, A. N., & Bates, S. (2022). A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification. arXiv [Cs.LG].

### Datasets

1. Alok, S. (n.d.). _Cityscapes dataset_. Kaggle. [View](https://www.kaggle.com/datasets/shuvoalok/cityscapes)
2. Gehrig, S. (n.d.). _Lost and Found dataset_. DHBW Stuttgart. [View](https://wwwlehre.dhbw-stuttgart.de/~sgehrig/lostAndFoundDataset/index.html)
3. Fishyscapes. (n.d.). _Fishyscapes benchmark suite_. [View](https://fishyscapes.com/)
