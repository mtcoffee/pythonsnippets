# PythonSnippets
A repo to hold some Python and Selenium Scripts

A linked github package/docker image is available to simplify requirements like Selenium. Just run the container with the script name and parameters for the script.

```
docker run -i --rm --name pythoncontainer \
-v "$PWD":/usr/src/myapp \
-w /usr/src/myapp \
ghcr.io/meatsac/alpine-python-selenium-chromium \
python scriptname.py
```
