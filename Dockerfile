FROM  bossjones/boss-docker-jhbuild-pygobject3:v1.1
MAINTAINER Malcolm Jones <bossjones@theblacktonystark.com>

ENV DEBIAN_FRONTEND noninteractive

COPY ./ /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84

WORKDIR /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84

RUN sudo DEBIAN_FRONTEND=noninteractive apt-get update -yqq && \
    sudo DEBIAN_FRONTEND=noninteractive apt-get install dbus dbus-x11 psmisc vim xvfb xclip -yqq && \
    sudo DEBIAN_FRONTEND=noninteractive apt-get clean && \
    sudo DEBIAN_FRONTEND=noninteractive apt-get autoclean -y && \
    sudo DEBIAN_FRONTEND=noninteractive apt-get autoremove -y && \
    sudo rm -rf /var/lib/{cache,log}/ && \
    sudo rm -rf /var/lib/apt/lists/*.lz4 /tmp/* /var/tmp/*

# RUN set -x cd /home/pi/dev/bossjones-github/repoduce_pytest_mock_issue_84 \
#     && pwd \
#     && pip install --upgrade pip && \
#     && pip install --no-cache-dir -r requirements.txt \
#     && python3 setup.py install

COPY ./container/root /

RUN sudo mv -f /dotfiles/.pythonrc /home/pi/.pythonrc && \
    sudo chown pi:pi /home/pi/.pythonrc && \
    sudo mv -f /dotfiles/.pdbrc /home/pi/.pdbrc && \
    sudo chown pi:pi /home/pi/.pdbrc && \
    sudo mv -f /dotfiles/.pdbrc.py /home/pi/.pdbrc.py && \
    sudo chown pi:pi /home/pi/.pdbrc.py

ENTRYPOINT ["/docker_entrypoint.sh"]
CMD true