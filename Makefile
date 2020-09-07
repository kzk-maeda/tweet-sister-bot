ENV := aws
PROFILE := kzk-serverless
WORKDIR := $(PWD)

# install libs
.PHONY: install
install:
	cd ./src \
	&& pip3 install -r requirements.txt -t ./lib \
	&& cd $(WORKDIR) \
	&& npm install

# deploy codes
.PHONY: deploy
deploy: install
	serverless deploy --aws-profile $(PROFILE) --verbose

# test
.PHONY: test
test: install
	cd ./test/ \
	&& pytest \
	&& cd $(WORKDIR)