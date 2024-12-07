# # set up
cd ~/OneDrive/datajam
# python3.12 -m venv create_openai_layer
# source create_openai_layer/bin/activate
# # Create openai layer
# pip install openai --platform=manylinux2014_x86_64 --only-binary=:all: --target ./create_openai_layer/lib/python3.12/site-packages
# mkdir python
# cp -r create_openai_layer/lib python/
# zip -r openai_layer.zip python
# rm -r python
# Create Google layer
python3.12 -m venv create_google_documentai_layer
source create_google_documentai_layer/bin/activate
pip install -r expense-classifier-backend/src/requirements.txt --platform=manylinux2014_x86_64 --only-binary=:all: --target ./create_google_documentai_layer/lib/python3.12/site-packages
pip uninstall pandas
pip uninstall numpy
mkdir python
cp -r create_google_documentai_layer/lib python/
zip -r google_documentai_layer.zip python