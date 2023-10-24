from .Server import Server
from .Tester import Tester

from .testers import testers_dict
        


def run_tests(servers: [Server], testers: [Tester|str]):
    output = "# Output\n"
    # Create table
    """
    |     | SERVERNAME | SERVERNAME | SERVERNAME |
    |     | ---------- | ---------- | ---------- |
    """
    output += "|    |"
    for server in servers:
        output += f" {server.name} |"
    
    output += "\n|    |"
    output += " ------- |" * len(servers)


    for tester in testers:
        if type(tester) == str:
            tester = testers_dict[tester]

        output += f"\n| {tester.name} |"

        for server in servers:
            result = tester.run(server.url)            
            output += f" {result} |"


            

    with open("output.md", "w", encoding="UTF-8") as output_file:
        output_file.write(output)

