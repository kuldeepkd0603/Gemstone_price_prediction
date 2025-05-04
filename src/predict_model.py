import joblib
from src.data_preprocessing import preprocess_input
import numpy as np




def predict(input_dict):
    """
    these is prediction function of gemstone price
    input_dict: dict with feature values
    returns: predicted price
    """
    try:
        try:
            model = joblib.load('models\SVR_model.pkl')
        except Exception as e:
            return f"model not found {e}"
        processed_data = preprocess_input(input_dict)
        prediction = model.predict(processed_data)
        print(prediction)
        return np.exp(float(prediction[0]))
    except Exception as e:
        raise ValueError(f"prediction failed: {e}")
