import socket

host = ''           # Bind to all interfaces
port = 51423

# Step 1 (Create the socket object)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2 (Set the socket options)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Step 3 (Bind to a port and interface)
s.bind((host, port))

# Step 4 (Listen for connections)
s.listen(5)
