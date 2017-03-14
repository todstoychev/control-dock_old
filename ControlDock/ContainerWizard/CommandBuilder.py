class CommandBuilder:
    """Used to build docker container command.

    Attributes:
        __command (str): Command string.
        __entrypoint (str): Entrypoint commands."""

    __command = ''
    __entrypoint = ''

    def __init__(self, base_command):
        """
        Parameters:
        -----------
        :param base_command: Base docker command.
         :Example: docker run"""

        self.__command = base_command

    def container_name(self, name=None):
        """Sets container name.

        Keyword arguments:
            :param name: Container name."""

        if name is not None and name.__len__() > 0:
            self.__command += '--name ' + name + ' '

    def entrypoint(self, entrypoint=None):
        """Sets the entrypoint directives.

        Keyword arguments:
            :param entrypoint: Entrypoint commands."""

        self.__entrypoint = entrypoint

    def build_command(self, image_id='', repository='', tag='', entrypoint=''):
        """Build command.

        Keyword arguments:
        :arg image_id: Image id.
        :arg repository: Image repository.
        :arg tag: Image tag / version.
        :arg entrypoint: Entrypoint command."""

        if len(image_id) == 0:
            image_id = repository

            if len(tag) > 0:
                image_id += ':' + tag

        self.__command += image_id + ' ' + entrypoint

        return self.__command

    def host_name(self, value):
        """Sets host name.

        Parameters:
        -----------
        :param value: Host name."""

        if value.__len__() > 0:
            self.__command += '--hostname ' + value + ' '

    def ports(self, value):
        """Sets ports.

        Parameters:
        -----------
        :param value: Ports string."""

        if value.__len__() > 0:
            ports = value.splitlines()

            for pair in ports:
                self.__command += '-p ' + pair + ' '

    def filesystem(self, value):
        """Sets filesystem mounts.

        Parameters:
        -----------
        :param value: Directory string."""

        if value.__len__() > 0:
            ports = value.splitlines()

            for pair in ports:
                self.__command += '-v ' + pair + ' '

    @property
    def command(self):
        return self.__command
