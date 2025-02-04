# ece386-lab01

Serving handwritten digit inference with FastAPI.

See [USAFA ECE 386: AI Hardware Applications - Lab 1](https://usafa-ece.github.io/ece386-book/b1-prediction/lab-digits-api.html)

**GitHub Actions are enabled in this repository!** The workflow currently:

- Runs [Black](https://black.readthedocs.io/en/stable/index.html) format checker against client and server
- Runs [Pyright](https://microsoft.github.io/pyright/#/) type checker against client and server

## Writeup

*Answer the following questions. Strive to be articulate.*

### What strategies did you use to ensure that your client and server where communicating with the same schema?
To ensure that our client and server were communicating with the same schema we used strategies such as standardizing API endpoints and its parameters. The client would always send POST requests so that it can reach the endpoint on the server which would be shown as the /predict portion of the code. This means that the API path is consistent as it ends up at the endpoint which is the server. Another strategy is using pillow. Using pillow allows the server to process the PNG image that we are sending. This allows both sides to know that we are trying to achieve the same goal of receiving and sending an image with the same format.

### In regard to preprocessing your digit images, how well do you think your server would scale to *any* picture of a digit?
We first decided to grayscale the image so that it doesn’t get in the way of recognizing the digit. Then we fixed the pixels of the image to 28x28 so that all the pictures that we put in were in the same format. This allowed the model to recognize what we were trying to get at as it was in the format that it was expecting. I do think that there are some improvements that we need to make as our model did not correctly identify any numbers. It could be from not writing the digits clearly or straight so there is a high chance that it got moved and weirdly positioned when we were resizing. 

### Does the client/server architecture make sense for this problem? Why or why not?
It depends, assuming we are getting multiple clients/users then it makes sense to have the server with the model to simplify the client side. On the other hand, if it was just for a single user and a time or just a local program it would not need a server it would just be overkill.   
## Documentation

*Documentation statement. We used Capt Yarbrough's video to structure our server code. C1C Quinn Flachman then told us how to set up our server with the post function to receive the POST request. He also showed us how to send files he directed us to the fast API documentation. He also helped us debug various errors.  
