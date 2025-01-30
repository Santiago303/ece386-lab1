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
from typing import Annotated
from fastapi import FastAPI, File, UploadFile
import pillow


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
    img = Image.ImageOps.grayscale(img)
    # TODO: convert image to numpy array of shape model expects
    return np.array(img)


# TODO: Define predict POST function
@app.post("/predict")
def predict(file: Annotated[bytes, File()]):
    processed_image = image_to_np(file)
    return {"file_size": len(file)}
