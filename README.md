# Logging Repository

This repository contains logs and detailed logs of any commits I make that are set up to my webhook endpoint. Any time I commit or perform any action on a repository that has this webhook configured, it edits this `logs.md` file and adds a new `h3` to the file with the commit name, repository committed to, and the date. Below the header, a summary of the code (up to 2000 characters) is generated using GPT 3.5 to summarize the changes.

## How it works

Using AWS API Gateway and AWS Lambda, I have a webhook endpoint at `api.charliemeyer.xyz` that is triggered by a GitHub webhook. This endpoint then triggers a lambda function (see `code/lamnda-function.py`) that then edits the `logs.md` and `detailed-logs.md` files on this repository.

## Do it yourself 

The code for the lambda function is in the folder `code.` All you need to do is create a `.zip` file according to [these instructions](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html), but a summary is:

1. Create a new folder called "package." in your working directory.
1. For this use-case, i just had to install the `openai` package, so I ran did `pip install --target ./package openai`. If you have a `requirements.txt` file from a venv or want to do something different, install the packages you need into the `package` folder from requirements.txt with `pip install -r requirements.txt --target ./package`. 
1. `cd package`
1. `zip -r ../my_deployment_package.zip .`
1. `cd ..`
1. `zip -g my_deployment_package.zip lambda_function.py`

Then, upload the `.zip` file to AWS Lambda and configure the webhook endpoint to point to the API Gateway endpoint.

Make sure you have created a lambda function and integrated it into a `POST` request to API gateway, and have properly configured the DNS settings and certificates. There's some other configuration necessary with DNS stuff, certificates and others that you can figure out. I used [this tutorial](https://www.youtube.com/watch?v=ESei6XQ7dMg) to get started and figured out the rest myself.

Additionally, make sure to add the proper GitHub/OpenAI tokens accordingly through Lambda -> Configuration -> Environment Variables and reference them in your code like I did. 






