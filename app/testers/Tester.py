from os import system, makedirs
from os.path import exists
from pathlib import Path
from subprocess import run

testers_dir = Path(__file__).parent
binary_dir = testers_dir.parent.joinpath("bin")

makedirs(str(binary_dir), exist_ok=True)


class Tester():
    """The base Tester class"""
    def __init__(self) -> None:
        pass

    def run(url: str):
        pass


class BinaryTester(Tester):
    """A Tester run using an executable file"""

    def __init__(self, binary:str, build_commands:list, default_args: str=None) -> None:
        """
        params:
        - binary: path towards the binary, relative to app/bin/
        
        """
        super().__init__()

        self.binary = str(binary_dir.joinpath(binary))
        self.default_args = default_args

        if not exists(self.binary):
            run("; ".join(build_commands), cwd=str(binary_dir), shell=True)
    
    def run(self, url: str, args: str=None):
        """
        Runs the binary against the provided url in the following format: `BINARY ARGS URL`

        If no args are passed but default_args is defined, those args will be used
        
        """
        if args is None and self.default_args is not None:
            args = self.default_args

        system(f"{self.binary} {args} {url}")
