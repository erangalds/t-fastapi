# Learning **FastAPI**

## Setting up the *FastAPI* Dev environment

```bash
# Listing the current conda python environments
conda env list
# Creating a new environment named l-fastapi
conda create --name l-fastapi
# activating the new environment
conda activate l-fastapi
# Checking for the python version, new environment should be empty
python --version
# Instaling the python 3.12 version
conda install python=3.12
# Checking the python version
python --version
```

### Installing the FastAPI packate

```bash
conda activate l-fastapi

pip install "fastapi[all]"
```

Let's break down this command:

+ pip install: This is the standard Python package installer.
+ fastapi: This installs the FastAPI framework.
+ "uvicorn[standard]": This installs Uvicorn, the ASGI (Asynchronous Server Gateway Interface) web server. The [standard] part is important because it includes recommended additional dependencies for Uvicorn (like python-dotenv and watchfiles for development features like hot-reloading). The quotes around "uvicorn[standard]" are important on some shells (like zsh) to prevent the square brackets from being interpreted as special characters.

Let's checkout the installation

```python
import fastapi
import uvicorn

print(fastapi.__version__)
print(uvicorn.__version__)
```

## Setting up the SQLAlchemy

Instaling SQLAlchemy

```bash
pip install sqlalchemy
```
