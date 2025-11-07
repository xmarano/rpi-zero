
# rpi-zero

Ce dépôt sert à tester et configurer de nouveaux Raspberry Pi Zero 2 W pour valider rapidement le réseau, les services de base et les réglages spécifiques au matériel.

## Init (désordre)
```sh
sudo apt update
sudo apt install git
sudo apt install btop
mv btop.conf ~/.config/btop/

# rpi-connect
sudo apt install rpi-connect-lite
sudo loginctl enable-linger
loginctl show-user $USER | grep Linger
rpi-connect on
rpi-connect signin

# Docker
sudo apt install docker.io docker-compose
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
newgrp docker

# zsh
sudo apt install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
chsh -s $(which zsh)
# theme "arrow"
nano ~/.zshrc
source ~/.zshrc

git clone https://github.com/xmarano/rpi-zero.git
```
