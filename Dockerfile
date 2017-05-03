FROM  bossjones/boss-docker-jhbuild-pygobject3:v1.1
MAINTAINER Malcolm Jones <bossjones@theblacktonystark.com>

ENV DEBIAN_FRONTEND noninteractive
ENV PIP_DOWNLOAD_CACHE /home/pi/.pip/cache
ENV GOSS_VERSION v0.2.3
ENV VIRTUALENVWRAPPER_SCRIPT /usr/local/bin/virtualenvwrapper.sh
ENV VIRTUALENV_WRAPPER_SH /usr/local/bin/virtualenvwrapper.sh
ENV GITHUB_REPO_NAME repoduce_pytest_mock_issue_84
ENV MAKEFLAGS -j4
ENV ENABLE_PYTHON3 yes
ENV PYTHONUNBUFFERED 1
ENV OLDPWD /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84/repoduce_pytest_mock_issue_84
ENV LC_ALL en_US.UTF-8
ENV USER pi
ENV SERVER_APP_NAME repoduce_pytest_mock_issue_84
ENV LD_LIBRARY_PATH /home/pi/.virtualenvs/repoduce_pytest_mock_issue_84/lib
ENV LANGUAGE_ID 1473
ENV GITHUB_REPO_ORG bossjones
ENV WORKON_HOME /home/pi/.virtualenvs/repoduce_pytest_mock_issue_84
ENV XDG_CONFIG_DIRS /home/pi/jhbuild/etc/xdg
ENV PYTHON_VERSION 3.5
ENV SCARLETT_LM /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84/tests/fixtures/lm/1473.lm
ENV VIRTUALENVWRAPPER_PYTHON /usr/local/bin/python3
ENV PATH /home/pi/jhbuild/bin:/home/pi/jhbuild/sbin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV JHBUILD /home/pi/gnome
ENV S6_VERSION v1.18.1.5
ENV MAIN_DIR /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84
ENV PWD /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84
ENV USER_HOME /home/pi
ENV LANG C.UTF-8
ENV S6_KILL_GRACETIME 1
ENV PYTHONSTARTUP /home/pi/.pythonrc
ENV PYTHON_VERSION_MAJOR 3
ENV SCARLETT_CONFIG /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84/tests/fixtures/.scarlett
ENV CURRENT_DIR $(pwd)
ENV VIRTUALENVWRAPPER_VIRTUALENV /usr/local/bin/virtualenv
ENV ENABLE_GTK yes
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS 2
ENV PYTHON_PIP_VERSION 9.0.1
ENV SHLVL 1
ENV HOME /home/pi
ENV VIRT_ROOT /home/pi/.virtualenvs/repoduce_pytest_mock_issue_84
ENV GITHUB_BRANCH master
ENV CFLAGS -fPIC -O0 -ggdb -fno-inline -fno-omit-frame-pointer
ENV SERVER_WORKER_PROCESSES 1
ENV S6_KILL_FINISH_MAXTIME 1
ENV GSTREAMER 1.0
ENV SERVER_LOG_MINIMAL 1
ENV PYTHONPATH /home/pi/jhbuild/lib/python3.5/site-packages:/usr/lib/python3.5/site-packages
ENV PREFIX /home/pi/jhbuild
ENV XDG_DATA_DIRS /home/pi/jhbuild/share:/usr/share
ENV GST_PLUGIN_PATH /home/pi/.virtualenvs/repoduce_pytest_mock_issue_84/lib/gstreamer-1.0
ENV DEBIAN_FRONTEND noninteractive
ENV PKG_CONFIG_PATH /home/pi/.virtualenvs/repoduce_pytest_mock_issue_84/lib/pkgconfig
ENV SIGNAL_BUILD_STOP 99
ENV PI_HOME /home/pi
ENV SKIP_ON_TRAVIS yes
ENV CC gcc
ENV SCARLETT_DICT /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84/tests/fixtures/dict/1473.dic
ENV SCARLETT_HMM /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84/.virtualenvs/repoduce_pytest_mock_issue_84/share/pocketsphinx/model/en-us/en-us
ENV PYTHON /usr/local/bin/python3

COPY ./ /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84

WORKDIR /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84

RUN sudo DEBIAN_FRONTEND=noninteractive apt-get update -yqq && \
    sudo DEBIAN_FRONTEND=noninteractive apt-get install dbus dbus-x11 psmisc vim xvfb xclip -yqq && \
    sudo DEBIAN_FRONTEND=noninteractive apt-get clean && \
    sudo DEBIAN_FRONTEND=noninteractive apt-get autoclean -y && \
    sudo DEBIAN_FRONTEND=noninteractive apt-get autoremove -y && \
    sudo rm -rf /var/lib/{cache,log}/ && \
    sudo rm -rf /var/lib/apt/lists/*.lz4 /tmp/* /var/tmp/*

RUN set -x cd /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84 \
    && pwd \
    && pip install --upgrade pip && \
    && pip install --no-cache-dir -r requirements.txt \
    && python3 setup.py install

COPY ./container/root /

RUN sudo mv -f /dotfiles/.pythonrc /home/pi/.pythonrc && \
    sudo chown pi:pi /home/pi/.pythonrc && \
    sudo mv -f /dotfiles/.pdbrc /home/pi/.pdbrc && \
    sudo chown pi:pi /home/pi/.pdbrc && \
    sudo mv -f /dotfiles/.pdbrc.py /home/pi/.pdbrc.py && \
    sudo chown pi:pi /home/pi/.pdbrc.py

ENTRYPOINT ["/docker_entrypoint.sh"]
CMD true