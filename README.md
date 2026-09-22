# House Price Prediction

A Streamlit web app that predicts house prices based on a few key property inputs such as area, bedrooms, and number of floors.

## Overview

This project uses a trained machine learning model to estimate the price of a house in lakhs. The app accepts user inputs and returns a price prediction in a simple, interactive interface.

## Features

- Simple and responsive Streamlit UI
- Input validation for realistic property values
- House price prediction using a saved machine learning model
- Clean and quick setup for local development

## Tech Stack

- Python
- Streamlit
- pandas
- scikit-learn
- joblib

## Project Structure

- `app.py` – Streamlit app entry point
- `log_reg_house_model.pkl` – trained model file
- `requirements.txt` – project dependencies

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   cd House_Price_Prediction
   ```

2. Create and activate a virtual environment:

   On Windows:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   On macOS/Linux:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

5. Open the local URL shown in the terminal in your browser.

## Input Rules

The app accepts the following input ranges:

- Area: 600 to 3000 sq ft
- Bedrooms: 1 to 4
- Floors: 0 to 10

If values fall outside these ranges, the app displays an error and does not predict a price.

## Example

The app will predict a price like:

```text
Predicted House Price: ₹35,00,000.00
```

## Notes

This project is intended as a lightweight machine learning demo and can be expanded with a larger dataset, additional features, or a more advanced model.
