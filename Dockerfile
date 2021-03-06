FROM  bossjones/boss-docker-jhbuild-pygobject3:v1.1
MAINTAINER Malcolm Jones <bossjones@theblacktonystark.com>

#######################
# Aufs Fix for docker on mac
# source: https://stackoverflow.com/questions/29245216/write-in-shared-volumes-docker/29251160#29251160
RUN sudo usermod -u 999 pi
RUN sudo usermod -G staff pi

ENV DEBIAN_FRONTEND noninteractive
ENV GOSS_VERSION v0.2.3
ENV GITHUB_REPO_NAME repoduce_pytest_mock_issue_84
ENV MAKEFLAGS -j4
ENV ENABLE_PYTHON3 yes
ENV PYTHONUNBUFFERED 1
ENV LC_ALL en_US.UTF-8
ENV USER pi
ENV SERVER_APP_NAME repoduce_pytest_mock_issue_84
ENV LD_LIBRARY_PATH /home/pi/.virtualenvs/repoduce_pytest_mock_issue_84/lib
ENV GITHUB_REPO_ORG bossjones
ENV WORKON_HOME /home/pi/.virtualenvs
ENV XDG_CONFIG_DIRS /home/pi/jhbuild/etc/xdg
ENV PYTHON_VERSION 3.5
ENV PATH /home/pi/jhbuild/bin:/home/pi/jhbuild/sbin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV JHBUILD /home/pi/gnome
ENV S6_VERSION v1.18.1.5
ENV PROJECT_HOME=/home/pi/dev
ENV MAIN_DIR /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84
ENV USER_HOME /home/pi
ENV LANG C.UTF-8
ENV S6_KILL_GRACETIME 1
ENV PYTHONSTARTUP /home/pi/.pythonrc
ENV PYTHON_VERSION_MAJOR 3
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
ENV PKG_CONFIG_PATH /home/pi/.virtualenvs/repoduce_pytest_mock_issue_84/lib/pkgconfig
ENV SIGNAL_BUILD_STOP 99
ENV PI_HOME /home/pi
ENV SKIP_ON_TRAVIS yes
ENV CC gcc
ENV PYTHON /usr/bin/python3
ENV TERM xterm

COPY ./ /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84

WORKDIR /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84

RUN sudo DEBIAN_FRONTEND=noninteractive apt-get update -yqq && \
    sudo DEBIAN_FRONTEND=noninteractive apt-get install dbus dbus-x11 psmisc vim xvfb xclip -yqq && \
    sudo DEBIAN_FRONTEND=noninteractive xargs apt-get install -y < /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84/packagelist-ubuntu-16.04-apt.txt && \
    sudo DEBIAN_FRONTEND=noninteractive apt-get clean && \
    sudo DEBIAN_FRONTEND=noninteractive apt-get autoclean -y && \
    sudo DEBIAN_FRONTEND=noninteractive apt-get autoremove -y && \
    sudo rm -rf /var/lib/{cache,log}/ && \
    sudo rm -rf /var/lib/apt/lists/*.lz4 /tmp/* /var/tmp/*

COPY ./container/root /

RUN sudo mv -f /dotfiles/.pythonrc /home/pi/.pythonrc && \
    sudo chown pi:pi /home/pi/.pythonrc && \
    sudo mv -f /dotfiles/.pdbrc /home/pi/.pdbrc && \
    sudo chown pi:pi /home/pi/.pdbrc && \
    sudo mv -f /dotfiles/.pdbrc.py /home/pi/.pdbrc.py && \
    sudo chown pi:pi /home/pi/.pdbrc.py && \
    sudo mv -f /dotfiles/.bashrc_orig /home/pi/.bashrc && \
    sudo chown pi:pi /home/pi/.bashrc

# source: https://stackoverflow.com/questions/20635472/using-the-run-instruction-in-a-dockerfile-with-source-does-not-work
RUN set -x cd /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84 \
    && pwd \
    && mkdir -p /home/pi/.virtualenvs \
    && /bin/bash -c "export PATH=\"/usr/local/bin:$PATH\" \
       export WORKON_HOME=/home/pi/.virtualenvs; \
       export PROJECT_HOME=$HOME/dev; \
       export VIRTUALENVWRAPPER_SCRIPT=/usr/share/virtualenvwrapper/virtualenvwrapper.sh; \
       export PYTHONWARNINGS=\"d\"; \
       source /usr/share/virtualenvwrapper/virtualenvwrapper.sh; \
       mkvirtualenv --python=/usr/bin/python3 repoduce_pytest_mock_issue_84; \
       workon repoduce_pytest_mock_issue_84; \
       pip install --no-cache-dir --upgrade --force-reinstall pip setuptools; \
       pip install --no-cache-dir -r requirements.txt; \
       cd /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84; \
       python3 setup.py install"; echo '[venv finished]'

ENTRYPOINT ["/docker_entrypoint.sh"]
CMD true
