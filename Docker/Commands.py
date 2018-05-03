import subprocess
from multiprocessing import Process

from Docker.DockerFactory import DockerFactory


class Commands:
    """
    Used to define basic docker commands.

    Attributes:
        :__docker (docker): Docker client instance.
    """

    def __init__(self):
        self.__docker = DockerFactory().create()

    def start_containers(self, container_ids: list):
        for container_id in container_ids:
            self.__docker.containers.get(container_id).start()

    def stop_containers(self, container_ids: list):
        for container_id in container_ids:
            self.__docker.containers.get(container_id).stop()

    def restart_containers(self, container_ids: list):
        for container_id in container_ids:
            self.__docker.containers.get(container_id).restart()

    def delete_containers(self, containers: list):
        for container_name in containers:
            self.__docker.containers.get(container_name).remove(force=True)

    def delete_images(self, images: list):
        for image_id in images:
            self.__docker.images.remove(image_id, force=True)

    def open_terminal(self, container_ids: list):
        for container_id in container_ids:
            p = Process(target=self.__terminal_session, args=[container_id])
            p.start()

    @staticmethod
    def __terminal_session(container_id: str):
        subprocess.Popen(['x-terminal-emulator', '-e', 'docker', 'exec', '-it', container_id, 'sh'])
