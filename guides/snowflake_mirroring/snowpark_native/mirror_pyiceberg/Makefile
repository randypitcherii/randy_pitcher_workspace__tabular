all: execute

clean:
	rm -rf ./.packages
	rm ./app.zip

build:
	pipenv run snow --config-file ./config.toml snowpark build --pypi-download yes --package-native-libraries ask --no-check-anaconda-for-pypi-deps

deploy: build
	pipenv run snow --config-file ./config.toml snowpark deploy --replace

execute: deploy
	pipenv run snow --config-file ./config.toml snowpark execute procedure "mirror_pyiceberg()" --debug