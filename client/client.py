"""
TODO: Insert what this program does here.
"""

import requests
import sys
from pathlib import Path


def get_img_prediction(
    server_ip: str, server_port: int, api_path: str, image_path: str
) -> str:

    image_path = Path(image_path)
    url = f"http://{server_ip}:{server_port}/{api_path}"
    with image_path.open("rb") as img_file:
        files = {
            "file": (image_path.name, img_file, "image/png")
        }  # Assuming PNG, change MIME type as needed
        response = requests.post(url, files=files)
    return response.text


def main(server_ip: str, server_port: int) -> None:
    """Repeatedly prompt the user for a path to an image
    and send it to the server for prediction.
    Then display the result to the user.
    """
    while True:
        image_path = input("Enter the path to the image or 'exit' to quit: ")
        if image_path.lower() == "exit":
            break
        if not Path(image_path).is_file():
            print("File does not exist, please try again.")
            continue

        response = get_img_prediction(
            server_ip, server_port, "predict", Path(image_path)
        )
        print("Prediction from server:", response)

    print(f"Using server {server_ip}:{server_port}")


if __name__ == "__main__":
    # Ensure user passes required arguments
    if len(sys.argv) != 3:
        print("Usage: python client.py <server IP address> <server port>")
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]))
