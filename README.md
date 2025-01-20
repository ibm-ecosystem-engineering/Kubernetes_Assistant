## Instructions

### Pre-requisites
    - Deploy Ollama platform
    - Deploy granite3.1-dense:8b and granite3-moe:3b models

Follow instructions at below links to deploy ollama (depending on operating system) and granite models

``https://www.ibm.com/granite/docs/run/granite-on-linux/granite/``

``https://www.ibm.com/granite/docs/run/granite-on-mac/granite/``

``https://www.ibm.com/granite/docs/run/granite-on-windows/granite/``

``https://ollama.com/blog/ibm-granite``


Create a ``.env`` file and copy content from env_sample into it. Update the values of environment variables appropriately.

### Instructions to run on a VM

Use below command to run the program:

  - `python kube-assistant.py`


### Instructions to build and run on docker

  First build the docker image:

  - `docker build -t kube_assistant_agentic:latest -f devops/Dockerfile .`
  
  Run the docker image:
  
  - `docker run -p 8080:80 kube_assistant_agentic:latest`
