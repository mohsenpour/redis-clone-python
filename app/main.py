import socket
import time


def main():
    # Implement your server here
    print("hey")

    s = socket.create_server(("localhost", 6379))
    s.accept()  # Wait for a new connection


if __name__ == "__main__":
    main()
