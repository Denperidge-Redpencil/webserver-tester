# Webserver Tester

Test the latest versions of your favourite webservers with any and all testing tools with minimal setup.

This project:
- Pulls the latest webserver image (for more information, see [#why docker below](#why-docker))
- Pulls and/or builds multiple testing tools
- Runs every tool and normalises their output


| Webserver name | Status |
| -------------- | ------ |
| Apache         |   ✅   |
| Nginx          |   ✅   |
| Caddy          |   ✅   |


|  Test tool   | Status |
| ------------ | ------ |
| wrk2         |   ✅   |
| slowhttptest |   ❔   |


✅: Integrated
❔: Planned
❌: Not integrated





## How-to
### Basic usage
Ensure that your system has the following installed: `git`, `python3`, `docker` and `docker compose`.

```bash
# Clone the repository
git clone https://github.com/Denperidge-Redpencil/webserver-tester.git
cd webserver-tester

# Start the webservers
docker compose pull  # Ensures that you are running the latest releases
docker compose up -d  # Note: on older installations, you may have to replace docker compose with docker-compose

# Create & activate virtualenv
python -m venv venv
source ./venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Open the help CLI
python -m app --help

# Run the tests
python -m app --all

# Done!
```

### Implementing a new webserver
1. Add it to `docker-compose.yml`
    ```yaml
        # docker-compose.yml
    services:
        # ...
        webserver_example:
            image: example:alpine
            ports:
            - "PORT:80"  # Replace PORT with a port that's currently available
    ```
2. Add it to the server list in [app/__main__.py](app/__main__.py)
    ```python
    # app/__main__.py
    # ...
    if __name__ == "__main__":
        servers = [
            # ...
            Server("example", "http://localhost:PORT"),  # Replace PORT with the same port as in docker-compose.yml
            # ...
        ]
    # ...
    ```

### Implementing a new tester
1. Create a python file
    ```python
    # app/testers/example.py

    # ...
    ```
2. Import the class
    ```python
    # app/testers/example.py
    from ..Tester import DockerTester

    example = DockerTester(
        name="example", 
        docker_image="your/image", 
        default_args="--run --url ")
    ```
3. Import the variable & defined it in the dict in [app/testers/__init__.py](app/testers/__init__.py)
    ```python
    # app/testers/__init__.py
    from .example import example

    testers_dict = {
        # ...
        "example": example,
        # ...
    }
    # ...
    ```
4. That's it! The args will automatically be implemented

## Reference
### Equal playing field
The measures implemented to keep the test as fair as possible:
- Latest **official** alpine Docker images
- Return the same file (TODO)
- Similar docker-compose configuration (TODO) 

## Discussions
### Testing methodology
The tool is designed to be expandable and customisable. This is done through the following methods:

- Docker-compose allows webservers to be added, removed and configured with ease
- The Python class (see [#Testers](#testers)) allows implementing different kinds of 


### Why Docker?
This is done deliberately for a few reasons.
1. Minimise setup time
2. Allows for an equal playing field (due to consistent usage of alpine images)

### Testers
Every tester tool is intigrated using the Tester class (see [app/Tester.py](app/Tester.py))

This allows...
- Drag and drop replacement
- Consistent implementation (e.g. in terms of output)
- Consistency between different tools

### Limitations
- In its current design, this test is incredibly barebones. It will only test how well each webserver can serve the same boilerplate page, which means performance can still vary depending on the size of the project.

