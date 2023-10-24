from ..Tester import DockerTester

slowhttptest = DockerTester(name="slowhttptest", docker_image="shekyan/slowhttptest", default_args="-u ")
