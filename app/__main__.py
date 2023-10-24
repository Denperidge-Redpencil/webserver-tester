# Local imports
from .args import use_all_testers, show_all_testers, enabled_tester_names
from .testers import testers_dict, testers_list
from .Server import Server

from .runner import run_tests

if __name__ == "__main__":
    servers = [
        Server("Apache", "http://localhost:80"),
        Server("Nginx", "http://localhost:8081"),
        Server("Caddy", "http://localhost:8082"),
    ]
 
    if show_all_testers:
        for tester in testers_list:
            print(tester)

    elif use_all_testers:
        run_tests(servers, testers_list)
        
    else:
        print("Enabled testers: " + str(enabled_tester_names))
        run_tests(servers, enabled_tester_names)

