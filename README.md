# H.Y.D.R.A - Financial Forecasting in Supermarkets  
**Final Year Project**

H.Y.D.R.A (**Hybrid Yield Data and Revenue Analytics**) is a machine learning-based financial forecasting system designed to predict sales trends and optimize inventory management in supermarkets. The project combines cutting-edge time-series forecasting techniques with deep learning models to deliver accurate and actionable insights.

---

## 🔑 Key Features  
- **Comprehensive Research**: Conducted in-depth analysis of existing time-series forecasting techniques to establish performance benchmarks.
- **Feature Engineering**: Preprocessed datasets to improve accuracy, including handling missing values, creating new features, and normalizing data.
- **Model Training**: Implemented multiple models for comparison, including:
  - **SARIMA**: Traditional statistical forecasting.  
  - **XGBoost**: Gradient-boosted decision tree model.  
  - **LSTM**: Sequential deep learning model for time-series data.  
  - **TFT Transformer**: Advanced temporal pattern recognition model.
  - **DCGAN Benchmark (2025 Research)**: Evaluated a Transformer GAN (DCGAN) approach from a recent 2025 research paper to benchmark generative sequence forecasting performance.  
- **ShadowLearning Technique**: Introduced a novel shadowlearning mechanism — a pattern-filtering technique where repetitive trends already seen in earlier sequences are discarded, allowing the model to focus only on learning new emerging patterns. This not only reduces training time significantly but also preserves predictive performance.
- **Performance Evaluation**: Analyzed and compared model results to identify the optimal approach for large-scale datasets.
---

## 🛠️ Technologies Used  
- **Programming Language**: Python  
- **Development Environment**: Google Colab
- **Dataset**: https://www.kaggle.com/c/favorita-grocery-sales-forecasting/data
- **Libraries**:  
  - Data Manipulation: `Pandas`, `NumPy`  
  - Visualization: `Matplotlib`, `Seaborn`  
  - Machine Learning: `Scikit-learn`, `XGBoost`,`PyTorch`
---
