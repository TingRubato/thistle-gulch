from . import base_server as base_server, exceptions as exceptions, packet as packet, socket as socket
from _typeshed import Incomplete

default_logger: Incomplete

class Server(base_server.BaseServer):
    def send(self, sid, data) -> None: ...
    def send_packet(self, sid, pkt) -> None: ...
    def get_session(self, sid): ...
    def save_session(self, sid, session) -> None: ...
    server: Incomplete
    sid: Incomplete
    def session(self, sid): ...
    sockets: Incomplete
    def disconnect(self, sid: Incomplete | None = None) -> None: ...
    def handle_request(self, environ, start_response): ...
    service_task_handle: Incomplete
    def shutdown(self) -> None: ...
    def start_background_task(self, target, *args, **kwargs): ...
    def sleep(self, seconds: int = 0): ...