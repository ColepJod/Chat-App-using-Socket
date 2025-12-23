import socket
import threading
import sys

HOST = "0.0.0.0"
PORT = 5000


def receive_messages(conn):
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                print("\nClient disconnected.")
                break
            print("\nClient:", data.decode("utf-8"))
            print("You: ", end="", flush=True)
        except Exception:
            break


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Listening on {HOST}:{PORT} ...")

    conn, addr = s.accept()
    print(f"Connected with {addr}")

    t = threading.Thread(target=receive_messages, args=(conn,), daemon=True)
    t.start()

    try:
        while True:
            msg = input("You: ")
            if msg.strip().lower() == "/quit":
                break
            if not msg:
                continue
            conn.sendall(msg.encode("utf-8"))
    except KeyboardInterrupt:
        pass
    finally:
        conn.close()
        s.close()
        print("\nConnection closed.")


if __name__ == "__main__":
    main()
