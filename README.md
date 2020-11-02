# JSON to PPTX examples
This repository contains a set of examples on how to perform requests and structure your data in order to convert json data into pptx presentations.

## Get Started

### Prepare your token
- Navigate to https://api.pptxbuilder.com 
- Create an account or login into your existing account.
- Navigate to the `Company` page, 
     - create a new company and identify the company key provided.
     - upload a 'PPTX Builder' friendly PowerPoint template if you want to use your own PowerPoint, if one is not provided then a default template is used. How to prepare a PowerPoint template: https://wiki.pptxbuilder.com/getting-started-1/preparing-powerpoint-templates
- Open the file `get_token.py` and replace the credentials.

### Create a virtual env
Create a virtual environment in the root of the directory.
``` $ python3 -m venv env ```

### Install dependencies
``` $ pip install -r requirements.txt ```

### Get a valid token
Once you have updated the values in `get_token.py`, you can then run it and get your authentication token.
``` $ python get_token.py ```

### How to try out the examples
In the `example_data` folder you will find various examples on how to structure your data. Change the `example_request.py` accordingly to load the data you want and use the correct token.



