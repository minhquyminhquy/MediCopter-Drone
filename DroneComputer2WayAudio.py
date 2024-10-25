import socket
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

def audio_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen(1)

    print("Waiting for connection...")
    connection, address = server_socket.accept()
    print("Connected!")

    p = pyaudio.PyAudio()
    output_device_index = 0
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, output_device_index=output_device_index)

    try:
        while True:
            data = connection.recv(CHUNK)
            if not data:
                break
            stream.write(data)
    except KeyboardInterrupt:
        pass

    print("Closing connection...")
    connection.close()
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    audio_server()
