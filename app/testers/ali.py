from docker import DockerClient

def ali(client: DockerClient, url: str, command="ali"):
    meow = client.containers.run("nakabonne/ali", f"{command} {url}")
    print(meow)