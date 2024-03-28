python3 -m venv .ghl-env
source .ghl-env/bin/activate
cp -r /mnt/c/users/silvh/OneDrive/lighthouse/portfolio-projects/GHL-chat ./repositories
cd repositories/GHL-chat
pip install \
--platform manylinux2014_x86_64 \
--target=./src \
--implementation cp \
--python-version 3.11 \
--only-binary=:all: -r requirements.txt
pip install ipykernel
ipython kernel install --user --name=ghl