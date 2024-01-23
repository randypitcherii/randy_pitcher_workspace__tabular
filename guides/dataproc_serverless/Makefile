all: build

# 👇 make sure you're cool with the values here. Update if you need to
LOCATION = us-east4
REPOSITORY = tabular-serverless-dataproc-artifacts

# you shouldn't have to update these values
PROJECT_ID := $(shell gcloud config get-value project)
IMAGE_NAME = tabular-dataproc-serverless
FULL_IMAGE_NAME = $(LOCATION)-docker.pkg.dev/$(PROJECT_ID)/$(REPOSITORY)/$(IMAGE_NAME)

print:
	@echo '\nCurrent image ID: $(FULL_IMAGE_NAME)'

auth:
	gcloud auth login
	gcloud auth configure-docker $(LOCATION)-docker.pkg.dev --quiet

create_repo:
	-gcloud artifacts repositories create $(REPOSITORY) --repository-format=docker --location=$(LOCATION) --description="Docker repository for Tabular assets used with serverless dataproc"

# Build the Docker image
build:
	@echo 'Building the project...'
	docker build -t $(IMAGE_NAME) .

# Tag the Docker image for GCR
tag:
	docker tag $(IMAGE_NAME) $(FULL_IMAGE_NAME)

# Push the Docker image to GCR
push: build tag auth create_repo
	docker push $(FULL_IMAGE_NAME)
	@echo '\nCurrent image ID: $(FULL_IMAGE_NAME)'

lab:
	pipenv install
	pipenv run jupyter lab
