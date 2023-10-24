from os import  makedirs
from os.path import exists, join
from pathlib import Path
from subprocess import run, PIPE
from json import loads

from re import compile

from docker import DockerClient, from_env as docker_from_env
from docker.types import LogConfig


testers_dir = Path(__file__).parent
binary_dir = testers_dir.parent.joinpath("bin")

makedirs(str(binary_dir), exist_ok=True)


re_ansi_escape = compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
def escape_ansi(text):
    """From https://stackoverflow.com/a/14693789"""
    return re_ansi_escape.sub('', text)



class Tester():
    """The base Tester class"""
    def __init__(self, name:str) -> None:
        self.name = name

    def run(url: str):
        pass

class BinaryTester(Tester):
    """A Tester run using an executable file"""

    def __init__(self, name:str, binary:str|Path, build_command:str, default_command: str=None) -> None:
        """
        params:
        - binary: path towards the binary, relative to app/bin/
        
        """
        super().__init__(name)

        self.binary_path = join(binary_dir, binary)
        self.build_command = build_command
        self.default_command = default_command
    
    def run(self, url: str, command: str=None):
        """
        Runs the binary against the provided url in the following format: `BINARY ARGS URL`

        If no args are passed but default_args is defined, those args will be used
        
        """
        if not exists(self.binary_path):
            run(self.build_command, cwd=str(binary_dir), shell=True)

        if command is None and self.default_command is not None:
            command = self.default_command
        return run([self.binary_path, loads(command.replace("<URL>", url))], stdout=PIPE, encoding="UTF-8", shell=True).stdout

    def __repr__(self) -> str:
        return f"BinaryTester: {self.binary_path}"


class DockerTester(Tester):
    """A Testser run using Docker"""
    def __init__(self, name:str, docker_image:str, default_command:str=None):
        super().__init__(name)
        self.docker_image = docker_image
        self.default_command = default_command
    
    def run(self, url: str, command: str=None):
        if command is None and self.default_command is not None:
            command = self.default_command
        
        client = docker_from_env()
        return escape_ansi(client.containers.run(image=self.docker_image, network="host", command=command.replace("<URL>", url)).decode("utf-8"))
