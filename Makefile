project := repoduce_pytest_mock_issue_84
projects := repoduce_pytest_mock_issue_84
flake8 := flake8
COV_DIRS := $(projects:%=--cov %)
# [-s] per-test capturing method: one of fd|sys|no. shortcut for --capture=no.
# [--tb short] traceback print mode (auto/long/short/line/native/no).
# [--cov-config=path]     config file for coverage, default: .coveragerc
# [--cov=[path]] coverage reporting with distributed testing support. measure coverage for filesystem path (multi-allowed)
pytest_args := -s --tb short --cov-config .coveragerc $(COV_DIRS) tests
pytest := py.test $(pytest_args)
sources := $(shell find $(projects) tests -name '*.py' | grep -v version.py | grep -v thrift_gen)

test_args_no_xml := --cov-report=
test_args := --cov-report term-missing --cov-report xml --junitxml junit.xml
cover_args := --cov-report html

.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"


define ASCILOGO
              _            _                             _      _                       ___  _  _   
  _ __  _   _| |_ ___  ___| |_      _ __ ___   ___   ___| | __ (_)___ ___ _   _  ___   ( _ )| || |  
 | '_ \| | | | __/ _ \/ __| __|____| '_ ` _ \ / _ \ / __| |/ / | / __/ __| | | |/ _ \  / _ \| || |_ 
 | |_) | |_| | ||  __/\__ \ ||_____| | | | | | (_) | (__|   <  | \__ \__ \ |_| |  __/ | (_) |__   _|
 | .__/ \__, |\__\___||___/\__|    |_| |_| |_|\___/ \___|_|\_\ |_|___/___/\__,_|\___|  \___/   |_|  
 |_|    |___/   
                                                                                    
=======================================
endef

export ASCILOGO

# http://misc.flogisoft.com/bash/tip_colors_and_formatting

RED=\033[0;31m
GREEN=\033[0;32m
ORNG=\033[38;5;214m
BLUE=\033[38;5;81m
NC=\033[0m

export RED
export GREEN
export NC
export ORNG
export BLUE

help:
	@printf "\033[1m$$ASCILOGO $$NC\n"
	@printf "\033[21m\n"
	@printf "\n"
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

list:
	@$(MAKE) -qp | awk -F':' '/^[a-zA-Z0-9][^$#\/\t=]*:([^=]|$$)/ {split($$1,A,/ /);for(i in A)print A[i]}' | sort

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

.PHONY: bootstrap
bootstrap:
	@workon repoduce_pytest_mock_issue_84
	@rm -rf *.egg-info || true
	@pip install -r requirements.txt
	@python setup.py install
	@printf "\033[1mReady for testing! $$NC\n"

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

test:
	py.test --pdb --showlocals -v -R : -k test_subprocess.py

test-with-pdb:
	pytest -p no:timeout -k test_subprocess.py
