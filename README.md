# 🚗 Maybe Obstacle: Uncertainty-Aware Road Obstacle Identification

## 📝 Project Overview
Reliable road obstacle identification is essential for the safe operation of autonomous driving systems. Traditional object detection methods often struggle to recognize unexpected or unknown obstacles, as they are typically limited to predefined categories. In dynamic and complex environments, this limitation poses a significant risk. Recent advancements in semantic segmentation, anomaly detection, and uncertainty quantification have enabled the development of uncertainty-aware methods that improve detection accuracy and reliability. These methods offer formal statistical guarantees on the reliability of predictions, crucial for safe and robust decision-making in real-world driving conditions.

### 🎯 Project Goal
The aim of this project is to develop a general, model-agnostic framework for road obstacle identification based on semantic segmentation outputs. The system will focus on anomaly-aware semantic segmentation to detect obstacles outside predefined classes. Additionally, the framework will integrate uncertainty quantification using Conformal Prediction methods, providing formal statistical guarantees regarding detection reliability.

## 🎡 Main Objectives
1. Anomaly-Aware Obstacle Segmentation: Integrate techniques within a semantic segmentation model to detect obstacles that fall outside known classes.
2. Statistical Uncertainty Quantification: Use conformal prediction methods to ensure reliable detection metrics.
3. Comprehensive Evaluation: Benchmark the system using both detection performance and uncertainty metrics.

## 🛠️ Proposed Structure
- Introduction
- Problem Statement
- Methodology
- Implementation
- Evaluation
- Results and Discussion
- Conclusions

## 🚀 How to Run
- Clone the repository.
- Follow the installation guide to set up the environment.
- Run the provided notebook for training and evaluation.

## 📚 References
1. Noguchi, C., Ohgushi, T., & Yamanaka, M. (2024). Road Obstacle Detection based on Unknown Objectness Scores. arXiv [Cs.CV].
2. Mossina, L., Dalmau, J., & Andéol, L. (2024). Conformal Semantic Image Segmentation: Post-hoc Quantification of Predictive Uncertainty. arXiv [Cs.CV].
3. Angelopoulos, A. N., & Bates, S. (2022). A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification. arXiv [Cs.LG].
