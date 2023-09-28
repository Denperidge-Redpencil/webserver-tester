# Webserver Tester

Test the latest versions of your favourite webservers with any and all testing tools with minimal setup.

This project:
- Pulls the latest webserver image (for more information, see [#why docker below](#why-docker))
- Pulls and/or builds multiple testing tools
- Runs every tool and normalises their output


| Webserver name | Status |
| -------------- | ------ |
| Apache         |   ❔   |
| Nginx          |   ❔   |
| Caddy          |   ❔   |


| Test tool | Status |
| --------- | ------ |
| wrk2      |   ❔   |


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

# Run the tests
python3 -m app

# Done!
```


## Discussions
### Testing methodology
The tool is designed to be expandable and customisable. This is done through the following methods:

- Docker-compose allows webservers to be 
- The python 


### Why Docker?
This is done deliberately for a few reasons.
1. Minimise setup time
2. Allows for an equal playing field (due to consistent usage of alpine images)

### Testers
Every tester tool is intigrated using the Tester class (see [app/testers/Tester.py](app/testers/Tester.py))

This allows...
- Drag and drop replacement
- Consistent implementation (e.g. in terms of logging)
- Consistency between different tools

### Limitations
- This test is incredibly barebones. It will only test how well each webserver can serve the same boilerplate page, which means performance can still vary depending on the size of the project.




