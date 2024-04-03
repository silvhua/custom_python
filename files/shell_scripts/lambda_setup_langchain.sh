cd ~
mkdir ./python
pip install \
--platform manylinux2014_x86_64 \
--target=./python \
--implementation cp \
--python-version 3.11 \
--only-binary=:all: --upgrade \ langchain
pip install \
--platform manylinux2014_x86_64 \
--target=./python \
--implementation cp \
--python-version 3.11 \
--only-binary=:all: --upgrade \ openai
zip -r langchain_packages.zip python