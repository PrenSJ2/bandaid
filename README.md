# Bandaid Base
A simple tool to write patches for the Google Firestore database.

![bandaid](https://github.com/voulezvous-app/Bandaid/assets/70067036/179b46b6-90b5-4191-bc60-6ea7a61a0e7b)


## Setup

- Create a service account key for your Firestore database
- navigate to google cloud console
- select your project
- select IAM & Admin
- select Service Accounts
- create a new service account
- give it the role of Firestore Admin
- create a key for the service account
- download the key and save it as `service-account.json` in the root of the project



- Create a virtual environment and install the dependencies.
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Create a patch
- In the `patch.py` file, create a new function that will be your patch.
- The function needs to be made between the `# Start of patches` and `# End of patches`.
- The function needs to have the `@command` decorator.

## Usage
- To run a patch use the following command:
```bash
python patch.py <patch_name>
```
