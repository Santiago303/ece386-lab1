"""
TODO: Insert what this program does here.
"""
import requests
import sys


def get_img_prediction(
    server_ip: str, server_port: int, api_path: str, image_path: str
) -> str:
    url = "https://0.0.0.0:8000/predict"
    myFiles = {open("/img/10.png","r")}
    x = requests.post(url, json = myFiles)
    print(x.text)
    """Send image to server for prediction."""
    # TODO: Replace with code to send image to server
    return ""


def main(server_ip: str, server_port: int) -> None:
    """Repeatedly prompt the user for a path to an image
    and send it to the server for prediction.
    Then display the result to the user.
    """
    # TODO: Replace with prompt to user and call to get_img_prediction
    print(f"Using server {server_ip}:{server_port}")


if __name__ == "__main__":
    # Ensure user passes required arguments
    if len(sys.argv) != 3:
        print("Usage: python client.py <server IP address> <server port>")
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]))
