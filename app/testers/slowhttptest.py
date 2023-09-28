from docker import DockerClient

def slowhttptest(client: DockerClient, url: str, command=""):
    meow = client.containers.run("shekyan/slowhttptest", f"{url}")
    print("@@")
    print(meow)