cd ~
source .venv/bin/activate
pip install \
--platform manylinux2014_x86_64 \
--target=.venv/lib/python3.10/site-packages \
--implementation cp \
--python-version 3.11 \
--only-binary=:all: urllib3
mkdir ./urllib3
mkdir ./urllib3/python
cp -r ./.venv/lib/python3.10/site-packages/urllib3 ./urllib3/python
zip -r urllib_packages.zip urllib3