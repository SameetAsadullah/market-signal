# Market Signal: Financial Time Series Forecasting

This project implements a deep learning pipeline for **multi-horizon prediction of financial time series** using temporal neural architectures. The framework supports multivariate inputs and outputs, enabling robust forecasting of market signals like Open, High, Low, Close, and Volume.

[![Notebook checks](https://github.com/SameetAsadullah/market-signal/actions/workflows/quality.yml/badge.svg)](https://github.com/SameetAsadullah/market-signal/actions/workflows/quality.yml)

---

## 🚀 Key Features

- 📊 **Multivariate Time Series Forecasting** (OHLCV)
- 🔁 **Multi-step Prediction Window**: Past 15 days → Next 3 days
- 🧠 **Models**: RNN, LSTM, GRU (stacked, configurable)
- 🔍 **Hyperparameter Grid Search** over:
  - Learning Rates
  - Batch Sizes
  - Number of Layers
  - Hidden Units
  - Optimizer Selection (Adam, SGD)
- ✅ **Evaluation** via RMSE and visual diagnostics
- 📉 Real-time plots:
  - Training/Validation loss trends
  - Predicted vs Actual market movement
  - Architecture comparisons by RMSE

---

## 🧰 Use Cases

- Financial modeling & algorithmic trading research
- Signal forecasting in time series (economics, IoT, crypto)
- Sequence learning & multivariate regression frameworks

---

## 📊 Benchmark Summary

| Model         | Best RMSE | Optimizer | Learning Rate | Batch Size | Layers | Hidden Units |
|---------------|-----------|-----------|----------------|-------------|--------|---------------|
| **GRU**       | **0.024** | Adam      | 0.001          | 16          | 2      | 100           |
| LSTM          | 0.026     | Adam      | 0.01           | 32          | 2      | 50            |
| RNN           | 0.028     | Adam      | 0.01           | 64          | 2      | 50            |

> ✅ **GRU-based models** achieved the strongest performance in multi-horizon OHLCV forecasting.

---

## 📈 Visualizations

- 🔹 RMSE bar charts by model and configuration
- 🔹 Best predicted vs actual plots (OHLCV)
- 🔹 Loss curves per epoch
- 🔹 Future market trend simulations

## Repository layout

- `notebooks/financial-forecasting.ipynb` — preprocessing, model search, and evaluation
- `data/` — chronological training and test datasets

## Run the analysis

```bash
cd notebooks
jupyter lab financial-forecasting.ipynb
```
