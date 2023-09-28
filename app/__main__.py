# Package imports
import docker

# Local imports
from .args import use_all_testers, show_all_testers
from .testers import testers_dict, all_testers

# Funcs
def run_tests(urls, testers):
   for url in urls:
        for tester in testers:
            tester.run(url)


if __name__ == "__main__":
    client = docker.from_env()
    #urls = ["localhost:8080", "localhost:8081", "localhost:8082"]
    urls = ["http://localhost:80"]

 
    if use_all_testers:
        run_tests(urls, all_testers)
    elif show_all_testers:
        for tester in all_testers:
            print(tester)

    else:
        pass

