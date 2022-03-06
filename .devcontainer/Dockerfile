FROM python:3.8

RUN apt update \
    && apt upgrade -y \
    && apt install -y npm nodejs lsb-release expect fish vim \
    && pip3 install --upgrade pip \
    && pip3 install online-judge-tools\
    && npm install -g atcoder-cli \
    && pip3 install selenium \
    && pip3 install flake8 \
    && pip3 install autopep8 \
    && acc config default-task-choice all \
    && chsh -s /usr/bin/fish

    # ------- fish setup ------
    # && curl -sL https://git.io/fisher | source && fisher install jorgebucaran/fisher \
    # && apt install fonts-powerline -y \
    # && fisher install oh-my-fish/theme-bobthefish \
    # && fisher install jethrokuan/z \
    # && fisher install oh-my-fish/plugin-peco

    # && ./login.sh \

    # ------ host machine側から ------
    # d cp ~/.config/fish/config.fish {container_id}:/root/.config/fish/config.fish
    # d cp ~/.ssh {container_id}:/root/