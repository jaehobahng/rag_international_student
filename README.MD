https://www.uscis.gov/sites/default/files/document/policy-manual-afm/afm34-external.pdf
https://www.uscis.gov/sites/default/files/document/policy-manual-afm/afm31-external.pdf
https://www.uscis.gov/policy-manual/volume-2-part-f


docker build -t int_rag .
docker run -it -v .:/app int_rag

docker rm <CONTAINER ID or NAME>
docker rm -f <CONTAINER ID or NAME>