"""
TODO: Insert what this program does here. Should start with
digits is a FastAPI app that...

This file should be compliant with Pyright.
The tensorflow import is ignored with # type: ignore[import]
because tensorflow doesn't support type hints appropriately.
"""

from tensorflow.keras.saving import load_model  # type: ignore[import]
from PIL import Image
from io import BytesIO
from fastapi import FastAPI
from keras.models import load_model
import numpy as np


model_path: str = "digits.keras"
# TODO: Open saved Keras model as global variable. NO TYPE HINT REQUIRED!
global model
model = load_model("digits.keras")
# TODO: Create FastAPI App as global variable
global app 
app = FastAPI()

def image_to_np(image_bytes: bytes) -> np.ndarray:
    """Convert image to proper numpy array"""
    # First must use pillow to process bytes
    img = Image.open(BytesIO(image_bytes))
    # TODO: convert image to grayscale and resize
    # TODO: convert image to numpy array of shape model expects
    return None


# TODO: Define predict POST function
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """Endpoint to receive image and predict the digit."""
    try:
        # Read image file as bytes
        image_data = await file.read()
        img_array = preprocess_image(image_data)

        # Predict using the global model
        prediction = model.predict(img_array)
        predicted_class = np.argmax(prediction, axis=1)[0]  # Extract predicted class

        return {"predicted_class": int(predicted_class)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
