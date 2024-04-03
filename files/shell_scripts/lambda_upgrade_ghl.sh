source activate-ghl.sh   
pip install --upgrade \
--platform manylinux2014_x86_64 \
--target=./src \
--implementation cp \
--python-version 3.11 \
--only-binary=:all: -r requirements.txt
cp -r src ../../
cd ~
mv src python
rm -r python/app
rm python/ghl_reply_lambda.py
rm python/ghl_chat_history_lambda.py
rm python/.env
zip -r langchain_packages_2024-01-13.zip python