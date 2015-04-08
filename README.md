[![Build Status](https://travis-ci.org/alekseiko/tow.svg)](https://travis-ci.org/alekseiko/tow)
[![Coverage Status](https://coveralls.io/repos/alekseiko/tow/badge.svg)](https://coveralls.io/r/alekseiko/tow)
[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/alekseiko/tow?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
# tow

[![Join the chat at https://gitter.im/alekseiko/tow](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/alekseiko/tow?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Workflow for docker configuration management 

# Using with docker

```
$ docker run -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd):/workspace tow <parameters>
```
