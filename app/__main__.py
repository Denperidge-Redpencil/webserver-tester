# Package imports
import docker

from .testers.wrk2 import wrk2

if __name__ == "__main__":
    client = docker.from_env()
    #urls = ["localhost:8080", "localhost:8081", "localhost:8082"]
    urls = ["http://localhost:80"]
    
    for url in urls:
        wrk2.run(url)
        #slowhttptest(client, url)