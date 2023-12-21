#Health Check Program
This program performs health checks based on the provided input file.

##Getting Started
To run this program, follow these steps:

##Prerequisites
Python: Ensure Python is installed on your system. 
Virtualenv: Install the virtualenv package to create a virtual environment for this project.
```
pip install virtualenv
```
###1.Setup
Create a Python Virtual Environment:
Replace <virtual-environment-name> with your preferred name.

python<version> -m venv <virtual-environment-name>
Example:
```
python -m venv health_check_env
```

###2.Activate the Virtual Environment:

On Unix or MacOS:

source health_check_env/bin/activate
On Windows Command Prompt:

```
#cmd
health_check_env\Scripts\activate.bat
```

On Windows PowerShell:
```
#powershell
health_check_env\Scripts\Activate.ps1
```
###3.Upgrade Pip:
Ensure pip is up to date inside the virtual environment.
```
python -m pip install --upgrade pip
```
###4.Install Required Packages:
Use the provided requirements.txt file to install necessary dependencies.
```
pip install -r requirements.txt
```
Running the Code
Run the main script health_check.py and provide the input file name (e.g., input.yaml).
```
python health_check.py
```
Follow the prompts to input the necessary information when prompted.

Example
An example of running the program:
```
python health_check.py
#Please enter file name or absolute path name: 
#input.yaml
```

##Tesing:

The test.py includes tests for send_request function with scenarios where the request is successful (200 OK) and when it fails (404 Not Found), as well as a test for calculate_availability.


Screenshot attached for executing the program and the result, result.png.
