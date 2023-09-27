One lovely day, I was working on getting a project up and running on a company server. I got to talking with my lovely coworker about the web server we were using, and my personal preference towards the Caddy webserver. Talks about how every webserver compared came into play, and then I decided to dig a little. After finding a few unclear or old articles and one website where the first comment I saw was an accusation of guerilla advertising, I decided to create a solution. Ish.




So, to get started, I used the [awesome-http-benchmark by GitHub user denji](https://github.com/denji/awesome-http-benchmark) to find some tools for a first draft. I cut the list down to those with > 1K stars (as to make sure its somewhat industry-vetted), non-archived and those that linked towards a focused GitHub repository.

- https://github.com/shekyan/slowhttptest
- https://github.com/six-ddc/plow
- https://github.com/hatoo/oha
- https://github.com/hallatore/Netling
- https://github.com/PragmaticFlow/NBomber
- https://github.com/grafana/k6
- https://github.com/rakyll/hey
- https://github.com/fortio/fortio
- https://github.com/giltene/wrk2
- https://github.com/wg/wrk
- https://github.com/tsenart/vegeta 
- https://github.com/fcsonline/drill
- https://github.com/ddosify/ddosify
- https://github.com/codesenberg/bombardier
- https://github.com/mcollina/autocannon
- https://github.com/nakabonne/ali

So that list has been made. That's a lot. I'm cutting down. The important factors now are those with an existing Docker image, non overlapping usecases as well as being logable cli tools (for example, tools including a dashboard are too out of scope)

This left:
- https://github.com/shekyan/slowhttptest
- https://github.com/grafana/k6
- https://github.com/fortio/fortio
- https://github.com/rakyll/hey
- https://github.com/tsenart/vegeta


- https://github.com/nakabonne/ali

