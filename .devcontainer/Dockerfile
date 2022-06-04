FROM python:3.8-slim-buster

RUN apt update \
    && apt upgrade -y \
    && apt install -y npm nodejs lsb-release expect git fish vim peco curl fonts-powerline \
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
    # && fisher install oh-my-fish/theme-bobthefish \
    # && fisher install jethrokuan/z \
    # && fisher install oh-my-fish/plugin-peco

    # ------- starship setup ------
    # curl -sS https://starship.rs/install.sh | sh

    # && ./login.sh \

    # ------ host machine側から ------
    # docker cp ~/.config/fish/config.fish {container_id}:/root/.config/fish/config.fish
    # docker cp ~/tools/dotfiles/fish/abbreviations.fish {container_id}:/root/.config/fish/abbreviations.fish
    # docker exec {container_id} fish /root/.config/fish/abbrievations.fish
    # docker cp ~/.ssh {container_id}:/root/.ssh
    # docker cp ~/.commit_template {container_id}:/root/.commit_template