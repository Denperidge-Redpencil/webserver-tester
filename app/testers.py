from configparser import ConfigParser

from .Tester import BinaryTester, DockerTester

testers_dict = dict()

config = ConfigParser()
config.read("testers.conf")

for tester_name in config.sections():
    conf_section = config[tester_name]

    if "build_command" in conf_section.keys():
        testers_dict[tester_name] = BinaryTester(
            name=tester_name,
            binary=conf_section.get("binary"),
            build_command=conf_section.get("build_command"),
            default_command=conf_section.get("default_command")
        )
    elif "docker_image" in conf_section.keys():
        testers_dict[tester_name] = DockerTester(
            name=tester_name,
            docker_image=conf_section.get("docker_image"),
            default_command=conf_section.get("default_command")
        )
    else:
        print(f"""The tester type couldn't be determined for {tester_name}.
There should be a build_command or a docker_image defined. You can check README.md if need be")
""")

testers_list = list(testers_dict.values())
