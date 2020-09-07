ENV := aws
PROFILE := kzk-serverless
WORKDIR := $(PWD)

# install libs
.PHONY: install
install:
	cd ./src \
	&& pip3 install -r requirements.txt -t ./lib \
	&& pip3 install -r requirements.txt \
	&& cd $(WORKDIR) \
	&& npm install

# deploy codes
.PHONY: deploy
deploy: 
	serverless deploy --aws-profile $(PROFILE) --verbose

# test
.PHONY: test
test: 
	cd ./test/ \
	&& pytest \
	&& cd $(WORKDIR)