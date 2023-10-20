# InterSP
Interactive Signal Processing

# Some Cool Links: 

## Unit and Integration tests: 
[Unit and Integration tests with Dash](https://dash.plotly.com/testing)

## CI/CD
[Cool Youtube Playlist about Automated CI/CD with GitHub actions](https://www.youtube.com/playlist?list=PLArH6NjfKsUhvGHrpag7SuPumMzQRhUKY) - Videos are very long but content is really complete with many practical examples. 

## Code Formatting and Prettifyers
[PyLint](https://pypi.org/project/pylint/) - Lint is a tool that checks code Styling such as Identation, Line length, File Length and so on.

## HSMW 
If we decide to use Mittweida servers instead of our own computers, we can use those tutorials to set them up. I never used it so I am not sure about capabilities and Limitations
[Website SetUp](https://wiki.hs-mittweida.de/de/Eigene_Webseite)
[Data Base SetUp](https://wiki.hs-mittweida.de/de/Eigene_Datenbank)

# Discussion

## Architecture
If we are going to make this app scalable, we need to decide on one architecture to use: Here is a small Medium article on Architecture with dash.I would recomend MVC for the UI since it is quite simple.
[https://towardsdatascience.com/clean-architecture-for-ai-ml-applications-using-dash-and-plotly-with-docker-42a3eeba6233]

## Docker
Maybe it would make sense to put all code inside a Docker Container, since we are planning to move the code to University Servers at some point. Docker Compose makes the migration almost effortless. 

## Branches
- We are only two persons, but maybe it would still make sense to setup review process in GitHub, so we must review code from each other before merging. We could learn a lot from each other this way :).
- We need to define some general rules for our branches. It is usually bad practice to have huge branches because it is a pain in the ass to solve merge conflicts.
- We should also block main branch, to avoid bad code there. The process should be always working on a feature branch and let the pipeline do it's magic and see if it is possible to merge it in main.

# I love you, Dear <3
