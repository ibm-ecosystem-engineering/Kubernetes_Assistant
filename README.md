## Instructions

Create a ``.env`` file and copy content from env_sample into it. Update the values of environment variables appropriately.

### Instructions to run on a VM

Use below command to run the program:

  - `python kube-assistant.py`


### Instructions to build and run on docker

  First build the docker image:

  - `docker build -t kube_assistant_agentic:latest -f devops/Dockerfile .`
  
  Run the docker image:
  
  - `docker run -p 8080:80 kube_assistant_agentic:latest`
