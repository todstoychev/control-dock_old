from Docker.DockerFactory import DockerFactory


class Commands:
    """
    Used to define basic docker commands.

    Attributes:
        :__docker (docker): Docker client instance.
    """

    def __init__(self):
        self.__docker = DockerFactory().create()

    def start_containers(self, containers: list):
        for container_name in containers:
            self.__docker.start(container_name)

    def stop_containers(self, containers: list):
        for container_name in containers:
            self.__docker.stop(container_name)

    def restart_containers(self, containers: list):
        for container_name in containers:
            self.__docker.restart(container_name)

    def delete_containers(self, containers: list):
        for container_name in containers:
            self.__docker.remove_container(container_name, force=True)
