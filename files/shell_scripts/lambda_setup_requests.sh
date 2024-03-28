cd ~
sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate
mkdir ./python
pip install \
--platform manylinux2014_x86_64 \
--target=./python \
--implementation cp \
--python-version 3.11 \
--only-binary=:all: requests
zip -r requests_packages.zip python