cd repositories
python3 -m venv ghl-env
source ghl-env/bin/activate
cp -r /mnt/c/users/silvh/OneDrive/lighthouse/portfolio-projects/GHL-chat ./
cp -r GHL-chat ./ghl-env
rm -r GHL-chat
pip install -r ghl-env/GHL-chat/requirements.txt

cd repositories/ghl-env/GHL-chat
pip install -r requirements.txt --target=./src
# Deleted modules using windows file explorer
pip install \
--platform manylinux2014_x86_64 \
--target=./src \
--implementation cp \
--python-version 3.11 \
--only-binary=:all: --upgrade -r requirements.txt


pip install \
--platform manylinux2014_x86_64 \
--target=./src \
--implementation cp \
--python-version 3.11 \
--only-binary=:all: --upgrade langchain

# pip install ipykernel
# ipython kernel install --user --name=ghl