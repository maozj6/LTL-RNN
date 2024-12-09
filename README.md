# LTL-RNN  
**Predict trajectory with LTL-constrained RNN**

This repository contains scripts for preprocessing datasets, training models, and visualizing results, designed to integrate Linear Temporal Logic (LTL) constraints into a Recurrent Neural Network (RNN) for trajectory prediction tasks.


## **Installation**

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```
---


## **Datasets**

Download the required datasets from the following sources:

- [ETH BIWI Walking Pedestrians Dataset](https://icu.ee.ethz.ch/research/datsets.html)  
  This dataset contains short-term pedestrian trajectories and is used for initial experiments.

- [NCLT Dataset](https://robots.engin.umich.edu/nclt/)  
  This dataset provides long-term pedestrian trajectories and is used for extended predictions and evaluations.

Make sure to place the downloaded datasets in the appropriate directories as specified in the scripts or preprocessing instructions.


## **Code Overview**

### **Preprocessing and Utilities**
- **`maxmin.py`**  
  Calculates the maximum and minimum values of the speed across the dataset. Useful for setting normalization or constraint thresholds.

- **`maxspeed.py`**  
  Computes the long-term maximum speed, aiding in defining velocity constraints.

- **`nclt_loader.py`**  
  Loads and processes the NCLT dataset for training and evaluation. Ensures the data is prepared in a format suitable for RNN models.

- **`newdata.py`**  
  Creates a smaller version of the dataset, intended for quick testing and debugging.

- **`newloader.py`**  
  Loads the smaller dataset generated by `newdata.py`, enabling faster iterations during testing.

---

### **Visualization**
- **`normal.py`**  
  Plots data points from the dataset for a quick overview of its structure and distribution.

- **`plot_loss.py`**  
  Generates plots for training and testing loss over epochs, helping to visualize model performance and convergence.

- **`visualizeNew.py`**  
  Visualizes the preprocessed dataset, providing insights into how the data is segmented and structured.

---

### **Training and Model Development**
- **`ran.py`**  
  Generates random splits of the dataset into training, validation, and test sets. Ensures reproducibility and balanced subsets.

- **`train.py`**  
  Trains a standard RNN without LTL constraints on the trajectory dataset.

- **`train2.py`**  
  Trains an RNN with LTL constraints applied to enforce logical and physical rules on the model's outputs.

---

## **How to Run**
To train the models and visualize results, execute the following commands:

```bash
# Train a standard RNN
python train.py

# Train an LTL-constrained RNN
python train2.py
