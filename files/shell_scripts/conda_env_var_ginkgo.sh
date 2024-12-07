
conda activate ginkgo
conda env config vars set TABLE_NAME=GinkgoData
conda env config vars set S3_BUCKET_ARN=arn:aws:iam::339712780591:role/GinkgoIntelligencePlatformRoleBeta
conda env config vars set S3_BUCKET_NAME=listparquet-prescription-generator
conda env config vars set AWS_PROFILE=GinkgoBeta
conda env config vars set AWS_DEFAULT_REGION=us-west-2
conda env config vars set REGION_NAME=us-west-2

conda env config vars list