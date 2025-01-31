# Digits Client

The client prompts the user for a path to an image. After hitting “enter” the client makes an HTTP POST request to the server, waits for the response, then displays the prediction integer to the user. 

## Usage

1. Create and activate a virtual environment.
   
2. Install dependencies
```console
usr@ece:~$ pip install -r requirements.txt
```
3. Run the client. (Replace <server_ip> with the server's IP address and <port> with the appropriate port number)
```console
usr@ece:~$ python client.py <server_ip> <port>
```



