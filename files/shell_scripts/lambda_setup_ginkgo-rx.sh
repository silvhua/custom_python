python3 -m venv .ginkgo-env
source .ginkgo-env/bin/activate
# cd repositories/rx-viewer
# pip install \
# --platform manylinux2014_x86_64 \
# --target=./src \
# --implementation cp \
# --python-version 3.11 \
# --only-binary=:all: -r requirements.txt
pip install ipykernel
ipython kernel install --user --name=ginkgo