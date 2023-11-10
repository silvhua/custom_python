sudo apt-get update
sudo apt-get upgrade
sudo apt install python3-pip
mkdir ./package
pip install --target ./package langchain
pip install --target ./package openai
cd ./package