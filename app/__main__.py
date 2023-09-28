
# Package imports
import docker

from .args import use_all_testers
from .testers import all_testers

if use_all_testers:
    testers = all_testers
else:
    testers = []


if __name__ == "__main__":
    client = docker.from_env()
    #urls = ["localhost:8080", "localhost:8081", "localhost:8082"]
    urls = ["http://localhost:80"]
    
    for url in urls:
        for tester in testers:
            tester.run(url)
