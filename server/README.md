# Digits Server

The server opens up the previously saved keras model. It accepts a POST request to /predict and then conducts inference on the image. It returns and integer of the predicted class.

## Usage

*Replace this line with some steps of how to setup and run the server*
1. Create and activate a virtual enviorment.

2. Install server packages

```console
usr@ece:~$ pip install -r requirements.txt
```
3. Run the server while serving the model.

```console
usr@ece:~$ fastapi run digits.py
```
