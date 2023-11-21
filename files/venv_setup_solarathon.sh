cd ~
python3 -m venv solarathon
source solarathon/bin/activate
pip install farm-haystack -f https://download.pytorch.org/whl/torch_stable.html
pip install ipykernel
ipython kernel install --user --name=solarathon