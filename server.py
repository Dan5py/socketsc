from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from socketsc import ServerSocketWrapper

import socketsc

server = socketsc.SocketServer(("localhost", 8080), socketsc.SOCK_TCP)

print("Server listening on port 8080")


def on_question(socket: ServerSocketWrapper, data):
    # print(f"Received {data} from {socket.client_address}")
    # socket.emit("answer", "1")
    socket.emit("answer", input("Insert answer: "))
    # socket.connection.close()
    # socket.connection.shutdown(socketsc.SHUT_WR)


server.on("question", on_question)
server.serve()
