import re


class Command:
    _commands = ['!GET', '!SEND', '!HELP', '!EXIT', '!CLOSE']
    end_of_output = '!END_OF_OUTPUT\r\n'
    usage = 'Commands Usage: \n     !GET - filepath > destination #(filepath is in the server, destination is in ' \
            'the client)\n     !SEND - filepath > destination #(filepath is in the client, destination is in the ' \
            'server)\n     !HELP - Display this help message\n     !EXIT - Exit from this client\n     ' \
            '!CLOSE - Close client and remote server\n'

    def __init__(self, command):

        self.command = command
        self.type = self._assign_type()

    def _valid_get_command(self):
        return re.match("!GET (.+)>(.+)", self.command)

    def _valid_send_command(self):
        return re.match("!SEND (.+)>(.+)", self.command)

    def _strip_command(self):
        self.command = self.command.strip()

    def _remove_type(self):
        return self.command.replace(self.type, '')

    def _assign_type(self):
        self._strip_command()
        test = self.command.split(' ')[0]  # get first word in command.

        if test not in Command._commands:
            return 'default'

        if test == '!GET':
            if self._valid_get_command():
                return test
            return 'INVALID'

        if test == '!SEND':
            if self._valid_send_command():
                return test
            return 'INVALID'
        return test  # can return '!HELP', '!CLOSE' or '!EXIT'

    def get_filename(self):
        """Get Filename folder from a \'!GET\' or \'!SEND\' command."""

        command = self._remove_type()
        tmp = command.split('>')
        filename = re.split(r"\\|/", tmp[0])[-1]
        return filename

    def get_destination(self):
        """Get Destination folder from a \'!GET\' or \'!SEND\' command."""

        command = self._remove_type()
        tmp = command.split('>')
        dst = tmp[1].strip()
        return dst

    def get_path(self):
        """Get file path from a \'!GET\' or \'!SEND\' command."""

        command = self._remove_type()
        tmp = command.split('>')
        path = tmp[0].strip()
        return path

    def __str__(self):
        return 'Command: %s\nType: %s' % (str(self.command), str(self.type))
