# PythonSnippets and Selenium Snippets
A repo to hold some Python and Selenium Scripts

A linked github package/docker image is available to simplify requirements like Selenium. Just run the container with the script name and parameters for the script.

## To run the built in scripts
To run your own scripts run the docker container and call the scripts directory in the container
```
docker run -i --rm --name pythoncontainer \
-v "$PWD":/usr/src/myapp \
-w /usr/src/myapp \
ghcr.io/mtcoffee/pythonsnippets \
python /scripts/CreateServiceNowIncidentSelenium.py
```

## To run your own scripts
To run your own scripts run the docker container with your script in the current path
```
docker run -i --rm --name pythoncontainer \
-v "$PWD":/usr/src/myapp \
-w /usr/src/myapp \
ghcr.io/mtcoffee/pythonsnippets \
python scriptname.py
```
