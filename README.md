# Webserver Tester

Test the latest versions of your favourite webservers with any and all testing tools with minimal setup.

This project:
- Pulls the latest webserver image (for more information, see [#why docker below](#why-docker))
- Automatically pulls and/or builds multiple testing tools
- Runs every tool and collects their output


| Webserver name | Status |
| -------------- | ------ |
| Apache         |   ✅   |
| Nginx          |   ✅   |
| Caddy          |   ✅   |


|  Test tool   | Status |
| ------------ | ------ |
| wrk2         |   ✅   |
| slowhttptest |   ❔   |
| vegeta       |   ❔ <sup>1</sup> |

Notes:
1. Requires go & easyjson to be installed



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
In [testers.conf](testers.conf), add the following
- `[name]`: replacing name with the name of the tester
- `default_command`: the default command that should be run when nothing else is specified. Make sure to add `<URL>` where the URL will have to go

Afterwards, depending on how the tool is installed/built, add the following

#### The tool uses a binary
In [testers.conf](testers.conf), add the following:
- `binary`: path relative to ./bin/ after the build is complete
- `build_command`: which command to run to build the binary. Multiple commands can be inserted using `echo "this"; echo "notation"`

#### The tool uses a Docker image
In [testers.conf](testers.conf), add the following:
- `docker_image`: the Docker image name. If you would normally run `docker run example/example`, the image name would be `example/example`


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

