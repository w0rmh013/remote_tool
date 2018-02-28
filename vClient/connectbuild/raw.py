import socket
import os.path


class Client:

    def __init__(self, server_ip, server_port):
        """Class constructor."""

        self.address = str(server_ip), int(server_port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, data):
        self.socket.send(str(data))

    def recv(self, buffersize):
        return self.socket.recv(buffersize)

    def recvall(self, size):

        buf = ''
        while size:
            data = self.recv(4096)
            buf += data
            size -= len(data)
        return buf

    def close(self):

        self.socket.close()


class SpecialClient(Client):

    def __init__(self, server_ip):
        """Class constructor."""

        Client.__init__(self, server_ip, 55867)

    @staticmethod
    def check_send(sendc):
        """validate the file that is being sent."""

        path = sendc.get_path()

        if os.path.exists(path):
            if os.path.isfile(path):
                return '0'
            else:
                return '1'
        return '2'

    @staticmethod
    def write_to_file(content, dst, filename):
        """Write content to dst\\filename."""

        with open(dst + '\\' + filename, 'wb') as f:
            f.write(content)

    @staticmethod
    def read_from_file(path):
        """Read content of path."""

        with open(path, 'rb') as f:
            return f.read()

    def get_cmd(self, c):
        """Handle '!GET' command."""

        self.send(c.command)
        rcode = self.recv(4096)

        if rcode == '1':
            return '[-] "%s" is not a file type.' % (c.get_filename())
        elif rcode == '2':
            return '[-] "%s" does not exist.' % (c.get_filename())
        elif rcode == '0':

            if os.path.exists(c.get_destination()):
                size = int(self.recv(4096))
                self.write_to_file(self.recvall(size), c.get_destination(), c.get_filename())
                return '[+] "%s" was downloaded.' % (c.get_filename())

            return '[-] Destination does not exist.'

        return '[-] Unknown error occurred.'

    def send_cmd(self, c):
        """Handle '!SEND' command."""

        rcode = self.check_send(c)
        if rcode == '1':
            return '[-] "%s" is not a file type.' % (c.get_path())
        elif rcode == '2':
            return '[-] "%s" does not exist.' % (c.get_path())
        elif rcode == '0':

            self.send(c.command)

            server_rcode = self.recv(4096)
            if server_rcode == '1':
                return '[-] Destination "%s" does not exist.' % (c.get_destination())
            elif server_rcode == '0':
                file_to_send = self.read_from_file(c.get_path())
                self.send(len(file_to_send))
                self.send(file_to_send)
                if self.recv(4096) == '0':
                    return '[+] "%s" was sent.' % (c.get_path())

        return '[-] Unknown error occurred.'

    def default_cmd(self, c):
        """Handle 'default' commands."""

        self.send(c.command)
        size = int(self.recv(4096))
        return self.recvall(size)

    def exit_close_cmd(self, c):
        """Handle '!CLOSE' and '!EXIT' commands."""

        self.send(c.type)
        self.close()
