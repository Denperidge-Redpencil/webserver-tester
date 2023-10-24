from .Server import Server
from .Tester import Tester

from .testers import testers_dict

from os.path import join, abspath, dirname 

def run_tests(servers: [Server], testers: [Tester|str]):
    output = "<h1>Output</h1>"
    # Create table

    output += "<table>"
    output += "<tr><th></th>"
    for server in servers:
        output += f"<th>{server.name}</th>"

    for tester in testers:
        if type(tester) == str:
            tester = testers_dict[tester]

        output += f"<tr><th>{tester.name}</th>"

        for server in servers:
            result = tester.run(server.url)            
            output += f"<td>{result}</td>"

    output += "</table>"


    with open(join(dirname(__file__), "template/index.html"), "r", encoding="UTF-8") as template_file:
        template = template_file.read()

    with open("output.html", "w", encoding="UTF-8") as output_file:
        output_file.write(template.replace("<REPLACE/>", output.replace("\n", "<br>")))

