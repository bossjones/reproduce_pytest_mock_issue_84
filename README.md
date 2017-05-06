# reproduce_pytest_mock_issue_84
reproduce_pytest_mock_issue_84

## Disclaimer

I put this repo together pretty quickly, in between the work week in an effort to repoduce the issues I saw while working w/ `pytest` and `pytest-mock` for my personal project, `scarlett_os`. I left a lot of the modules that I originally used in this repo, along w/ some other things that might be a bit unecessary. The purpose of that was to create an environment that was as close as possible to what I'm actually using ... just minus some of the complexity.

# Requirements
- Docker For Mac ( That's what I tested on! If it needs testing on linux, I can do that as well )

Specifically i'm using:

```
$ docker --version
Docker version 1.12.5, build 7392c3b

$ docker-compose --version
docker-compose version 1.9.0, build 2585387

 |2.2.3|   Malcolms-MBP-3 in ~/dev
○ →
```

# Setup

### 1. Start docker container via docker-compose

`make docker-compose`

### 2. Exec into the container using bash

`make docker-exec`

### 3. Once in the container, run bootstrap command to install dependencies

```
# from inside container
make bootstrap
```

### 4. Enable virtualenv and run tests

#### A. How to repoduce error

```
# from inside container
workon repoduce_pytest_mock_issue_84
make test
```

#### B. Run tests w/ mocker.stopall() to fix "leak"

When you set this environment variable, mocker.stopall() runs at the beginning and end of each test case.

```
# from inside container

workon repoduce_pytest_mock_issue_84
ENABLE_STOPALL=1 make test
``` 