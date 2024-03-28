cd ~
python3 -m venv notion
source notion/bin/activate
pip install ipykernel
ipython kernel install --user --name=notion