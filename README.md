## heavywater classification algorithm
This is to classify encrypted mortgage data that we get.
This is a supervised model.
On init, classifier will be trained and stored in pickle or json.
As of now, classifier is planned to be built on Keras.
When the REST end point is called, it will load the trained model and calculate results.
This container will be hosted on AWS. 

# requirements  
docker installed

# to use
run deploy.sh, like
./deploy.sh

# Use sample api  
curl http://0.0.0.0:8000/isAlive

curl "http://0.0.0.0:8000/get_prediction" -H 'Content-Type: application/json' -d '{"sentences":["love it"]}'