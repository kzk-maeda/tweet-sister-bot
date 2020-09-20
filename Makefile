ENV := aws
PROFILE := default
WORKDIR := $(PWD)

# install libs
.PHONY: install
install:
	cd ./src \
	&& pip3 install -r requirements.txt -t ./lib \
	&& cd $(WORKDIR) \
	&& pip3 install -r ./src/requirements.txt \
	&& npm install

# deploy codes
.PHONY: deploy
deploy: 
	serverless deploy --stage production --aws-profile $(PROFILE) --verbose

# test
.PHONY: test
test: 
	cd ./test/ \
	&& pytest \
	&& cd $(WORKDIR)