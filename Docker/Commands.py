from Docker.DockerFactory import DockerFactory


class Commands:
    __docker = DockerFactory().create()

    def start_containers(self, containers: list):
        for container_name in containers:
            self.__docker.start(container_name)
