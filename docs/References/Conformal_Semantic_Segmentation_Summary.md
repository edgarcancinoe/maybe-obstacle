
# Conformal Semantic Image Segmentation: Post-hoc Quantification of Predictive Uncertainty

## Authors
- Luca Mossina, Joseba Dalmau, Léo Andéol  
- IRT Saint Exupéry, Institut de Mathématiques de Toulouse, SNCF

## Abstract
This paper introduces a computationally efficient method to quantify predictive uncertainty in semantic image segmentation. 
The approach leverages **Conformal Prediction (CP)** to create statistically valid prediction sets that guarantee the inclusion 
of the ground-truth segmentation mask at a predefined confidence level. The method is model-agnostic and can be applied 
post-hoc to any segmentation model.

## Key Points

### 1. Problem Statement
- Predictive uncertainty in semantic image segmentation (SIS) is critical, especially in safety-critical applications.
- Softmax scores from deep models are typically overconfident and poorly calibrated.
- There is a need for reliable uncertainty quantification (UQ) that can work post-hoc without requiring model retraining.

### 2. Proposed Method: Conformal Prediction (CP)
- Uses **Conformal Prediction (CP)** to assess uncertainty in segmentation masks.
- Generates **multi-labeled masks** where each pixel can belong to multiple classes if uncertainty is high.
- A **risk level α** is set to control the confidence of predictions.
- Uses **Conformal Risk Control (CRC)** to guarantee that the empirical risk remains below a user-defined threshold.

### 3. Loss Functions
- **Binary Loss**: Strict criterion where the prediction set must cover all pixels.
- **Binary Loss with Threshold**: Controls the coverage ratio (e.g., 90% of pixels must be correctly labeled).
- **Miscovrage Loss**: Directly controls coverage by minimizing the proportion of pixels not covered.

### 4. Visualization: Varisco Heatmaps
- Heatmaps represent uncertainty by showing the number of classes associated with each pixel.
- Warm colors indicate high uncertainty.
- Provides a visual assessment of the risk control, showing areas where the model is less confident.

### 5. Experiments
- Datasets: Cityscapes, ADE20K, LoveDA
- Models: PSPNet, SegFormer
- Metrics: **Empirical Risk**, **Activation Ratio (AR)**

| Dataset     | α    | Empirical Risk | Activation Ratio |
|------------|------|----------------|------------------|
| Cityscapes | 0.1  | 0.106 ± 0.019   | 1.028            |
| ADE20K     | 0.2  | 0.179 ± 0.005   | 1.000            |
| LoveDA     | 0.1  | 0.097 ± 0.018   | 1.231            |

### 6. Strengths and Limitations

**Strengths:**  
- Model-agnostic and computationally efficient.  
- Provides post-hoc uncertainty quantification without retraining.  
- Can be applied to pre-trained models accessed via APIs.  

**Limitations:**  
- Limited interpretability when used with poor-quality segmentation models.  
- Calibration data quality impacts prediction accuracy.  

## Suggested Sections to Read
1. **Introduction** (Section I) - Overview of the problem and motivation.  
2. **Proposed Method** (Section IV) - Detailed methodology including CP and CRC.  
3. **Experiments** (Section VI) - Datasets and experimental evaluation.  
4. **Results and Analysis** (Section VII) - Detailed comparison and performance metrics.  
5. **Conclusion** (Section VIII) - Summary and future directions.  

## Conclusion
The method effectively quantifies uncertainty in SIS using CP, offering reliable and interpretable uncertainty metrics. 
Further research should explore its integration with Bayesian methods and adaptation to panoptic segmentation.
