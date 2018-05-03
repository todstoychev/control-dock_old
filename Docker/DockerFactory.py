import docker


class DockerFactory:
    """
    Attributes:
        :__docker docker: Docker client instance.
    """
    __docker = None

    def create(self):
        """
        Creates docker client instance

        :return docker:
        """
        self.__docker = docker.from_env()

        return self.__docker
