FROM python:3.8

RUN apt-add-repository ppa:fish-shell/release-3 \
    && apt update \
    && apt upgrade -y \
    && apt install -y npm nodejs lsb-release expect fish \
    && pip3 install online-judge-tools\
    && npm install -g atcoder-cli \
    && pip3 install flake8 \
    && pip3 install autopep8 \
    && acc config default-task-choice all \
    # && ./login.sh \
    # && fish \
    # && curl -sL https://git.io/fisher | source && fisher install jorgebucaran/fisher \
    # && apt install fonts-powerline -y \
    # && fisher install oh-my-fish/theme-bobthefish \
    # && fisher install jethrokuan/z \
    # && fisher install oh-my-fish/plugin-peco

    # host machine側から
    # d cp ~/.config/fish/config.fish {container_id}:/root/.config/fish/config.fish  