# conda env config vars set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\silvh\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\Roaming\gcloud\application_default_credentials.json
conda activate gcp
conda env config vars set GOOGLE_APPLICATION_CREDENTIALS=`pwd`/src/application_default_credentials.json
conda env config vars set GOOGLE_APPLICATION_CREDENTIALS_PATH=`pwd`/src/application_default_credentials.json
conda env config vars set AWS_PROFILE=silvhua2-admin