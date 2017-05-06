#!/usr/bin/env bash
export WORKON_HOME=/home/pi/.virtualenvs
export PROJECT_HOME=$HOME/dev
export VIRTUALENVWRAPPER_SCRIPT=/usr/share/virtualenvwrapper/virtualenvwrapper.sh
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
workon repoduce_pytest_mock_issue_84
rm -rf *.egg-info || true
pip install -r requirements.txt
python setup.py install
printf "\033[1mReady for testing!\n"