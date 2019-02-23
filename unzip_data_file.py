import zipfile
with zipfile.ZipFile("./data/shuffled-full-set-hashed.csv.zip","r") as zip_ref:
    zip_ref.extractall("/usr/intermediate/")

