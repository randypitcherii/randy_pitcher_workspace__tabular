all: build

# Get the current Google Cloud project ID
PROJECT_ID := $(shell gcloud config get-value project)
IMAGE_NAME = tabular-dataproc-serverless
FULL_IMAGE_NAME = gcr.io/$(PROJECT_ID)/$(IMAGE_NAME)

# Build the Docker image
build:
	@echo 'Building the project...'
	docker build -t $(IMAGE_NAME) .

# Tag the Docker image for GCR
tag:
	docker tag $(IMAGE_NAME) $(FULL_IMAGE_NAME)

# enable the gcp container registry
enable-container-registry: 
	gcloud services enable containerregistry.googleapis.com

# Push the Docker image to GCR
push: build tag
	docker push $(FULL_IMAGE_NAME)

lab:
	pipenv install
	pipenv run jupyter lab
