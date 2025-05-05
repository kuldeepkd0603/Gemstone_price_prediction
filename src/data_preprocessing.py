import numpy as np
import joblib
import pandas as pd


def preprocess_input(input_dict):
    """
    input_dict: dict with keys ['carat', 'cut', 'color', 'clarity', 'depth', 'table']
    returns: scaled and encoded data ready for prediction
    """
    try:
        
        try:
           scaler = joblib.load('models\standard_scaler.pkl')
        except Exception as e:
           return f"scaler is not found {e}"
        data= pd.DataFrame([input_dict])

        cut_order = {'Fair': 1, 'Good': 2, 'Very Good': 3, 'Premium': 4, 'Ideal': 5}
        color_order = {'J': 1, 'I': 2, 'H': 3, 'G': 4, 'F': 5, 'E': 6, 'D': 7}
        clarity_order = {'I3': 1, 'I2': 2, 'I1': 3, 'SI2': 4, 'SI1': 5,
                 'VS2': 6, 'VS1': 7, 'VVS2': 8, 'VVS1': 9, 'IF': 10, 'FL': 11}
        data['cut'] = data['cut'].map(cut_order)
        data['color'] = data['color'].map(color_order)
        data['clarity'] = data['clarity'].map(clarity_order)
    

        data['log_carat'] = np.log(data['carat'])
        data.drop(['carat'], axis=1, inplace=True)
    
        scaled = scaler.transform(data)
        

        return scaled
    except Exception as e:
        raise ValueError(f"Preprocessing failed: {e}")
