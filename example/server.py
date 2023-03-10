import socketsc


server = socketsc.SocketServer(("localhost", 8080), address_family=socketsc.AF_INET, sock_type=socketsc.SOCK_TCP)

print("Server listening on port 8080")


def on_question(socket: socketsc.ServerSocketWrapper, data):
    socket.emit("answer", input("Insert answer: "))
    server.emit("broadcast", "Hello")


server.on("question", on_question)
server.serve()
