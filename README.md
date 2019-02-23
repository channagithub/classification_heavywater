## heavywater classification algorithm
This is to classify encrypted mortgage data that we get.
This is a supervised model.
On init, classifier will be trained and stored in pickle or json and loaded.
Classifier is built on LinearSVC after comparing the accuracy with multiple other classification models.
When the REST end point is called, it will use the loaded trained model and calculate results.
This container will be hosted on AWS. 

# requirements  
docker installed
> It is required that docker engine is running with at least 6GB of RAM (for Token computation)

# to use
run deploy.sh, like
./deploy.sh

# Use sample api  
curl http://0.0.0.0:8000/isAlive

curl "http://0.0.0.0:8000/get_prediction" -H 'Content-Type: application/json' -d '{
	"sentences":["3486e5fe0d73 1b6d0614f2c7 6bf9c0cb01b4 3486e5fe0d73 c337a85b8ef9 c9a53ea6e219 6dae7d5c1d03 878460b4304e 133d46f7ed38 43af6db29054 7c19789847e6 7e0ebc43dbc1 de9738ee8b24 1015893e384a 586242498a88 e43c4b6f2c61 eeb86a6a04e4 641356219cbc 446c804d79cc f95d0bea231b aa1ef5f5355f"
]
}'