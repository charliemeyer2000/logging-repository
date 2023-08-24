import requests
import datetime
import openai
import base64 
import json
import os

# Configure openAI key (updated 11:02 PM 6/16/23)
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Configure GitHub token
GITHUB_TOKEN =

def lambda_handler(event, context):
    payload = json.loads(event['body'])

    # get git commit message
    commit_message = payload['head_commit']['message']

    # get the commit sha
    commit_sha = payload['head_commit']['id']

    # Get the lines of code that were added or removed
    owner = "charliemeyer2000"
    
    # get the repository that the commit was made to
    repository_committed_to = payload['repository']['name']

    print('the commit sha is: ', commit_sha)

    url = f"https://api.github.com/repos/{owner}/{repository_committed_to}/commits/{commit_sha}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }

    response = requests.get(url=url, headers=headers)
    data = response.json()
    print('data response')
    print(data)

    # get the lines of code that were added or removed
    lines_added = {}
    lines_removed = {}

    for file in data['files']:
        file_name = file['filename']
        added_lines = []
        removed_lines = []

        if 'patch' in file:
            patch = file['patch']
            patch_lines = patch.split('\n')
            for line in patch_lines:
                if line.startswith('+'):
                    added_lines.append(line[1:])
                elif line.startswith('-'):
                    removed_lines.append(line[1:]) 

        lines_added[file_name] = added_lines
        lines_removed[file_name] = removed_lines

    # get the files that were modified in the commit
    files_modified = payload['head_commit']['modified']

    # get the committer 
    committer = payload['head_commit']['committer']['username']

    print("Received a commit to repository " + repository_committed_to + " with commit message: " + commit_message)

    # generate a summary of the commit based on the code 
    commit_summary = generate_summary(code_added=lines_added, code_removed=lines_removed, commit_message=commit_message)

    print("Generated a summary of the commit: " + commit_summary)

    # Add the summary to the markdown file in repository named "logging-repository"
    create_commit(commit_summary=commit_summary, commit_message=commit_message, repository_committed_to=repository_committed_to, files_modified=files_modified, committer=committer)
    create_detailed_commit(code_added=lines_added, code_removed=lines_removed, repository_committed_to=repository_committed_to, commit_message=commit_message, committer=committer)

    # return a 200 response to acknowledge receipt of the payload
    return 'Commit summary added to README.md file in logging-repository'

def generate_summary(code_added: dict, code_removed:dict, commit_message: str) -> str:
    """
    Takes in a string of code and returns a summary of the code

    :param commit_code: string of code
    :return: string of summary
    """

    # Generate summary using OpenAI
    prompt = f"""
    Please generate a summary of the important changes made in this GitHub commit.
     I will present you with the changes below, and I need you to summarize them in a succinct and easy way. 
     The response should be entirely plain text. Here are the changes:

    Code Added:
    """

    for file_name, added_lines in code_added.items():
        prompt += f"    File: {file_name}\n"
        for line in added_lines:
            prompt += f"    + {line}\n"
        prompt += "\n"

    prompt += """
    Code Removed:
    """

    for file_name, removed_lines in code_removed.items():
        prompt += f"    File: {file_name}\n"
        for line in removed_lines:
            prompt += f"    - {line}\n"
        prompt += "\n"

    # if the prompt is over 2k characters, then truncate it
    if len(prompt) > 2000:
        prompt = prompt[:2000]

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=60,
    )

    if(len(prompt) > 2000):
        return response.choices[0].text.strip() + "... Because more than 2000 characters were provided, the summary was truncated. Therefore, the summary may not entirely be accurate to all of the code & changes made in the commit."
    else:
        return response.choices[0].text.strip()

def create_commit(commit_summary: str, commit_message: str, repository_committed_to: str, files_modified: any, committer:str) -> None:
    """
    Takes in a summary of the commit and adds it to the logs.md file in the logging-repository in my github account.

    :param commit_summary: summary of the commit
    :return: None
    """

    # Get the current logs.md file from the logging-repository
    url = "https://api.github.com/repos/charliemeyer2000/logging-repository/contents/logs.md"
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}'
    }

    # Get the current logs.md file
    response = requests.get(url=url, headers=headers)
    current_content = response.json()['content']
    current_content = base64.b64decode(current_content).decode('ascii', 'ignore')

    # Gets the current date and time
    current_date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    # Create a new addition to the logs.md file
    title = f"### {committer}: '{commit_message}' @ {current_date} to {repository_committed_to}\n"
    summary= ''
    if len(files_modified) > 0: # files_modified is an array of strings
        # add to summary the files that were modified using a for loop
        summary = "The following files were modified: \n"
        for file in files_modified:
            summary += f"- {file}\n"
    else:
        summary = "No files were modified in this commit."
    
    # Add the GPT summary to the summary, make the summary a block quote of code block
    summary += f'\nGPT Summary: \n > {commit_summary}' + '\n' 
        

    # Add a h3 header to the TOP logs.md file with the commit message and the commit summary
    new_content = title + summary + '\n\n' + current_content

    # Encode the new content to base64 and avoiding emojis
    new_content = new_content.encode('ascii', 'ignore')
    new_content = base64.b64encode(new_content)

    # Update the logs.md file to be the old content + the new content
    data = {
        "message": f"Update logs.md with commit summary for commit {commit_message}",
        "content": new_content.decode('ascii'),
        "sha": response.json()['sha']
    }

    # Update the logs.md file
    response = requests.put(url=url, headers=headers, data=json.dumps(data))


## TODO: make a method called "create detailed logs" where rather than doing a GPT summary you just directly add the added/removed code to the file. Add it to a separate file called "detailed-logs.md"
def create_detailed_commit(code_added: dict, code_removed: dict, repository_committed_to:str, commit_message: str, committer: str) -> None:
    """
    This generates a detailed log of the commit made and adds it to the `detailed-logs.md` file in the logging-repository
    This contains the code that was added and removed in the commit, as well as the commit message, the committer, and the date/time of the commit. 
    It does not contain the GPT summary.

    :param code_added: dictionary of code added
    :param code_removed: dictionary of code removed
    :param repository_committed_to: string of the repository committed to
    :param commit_message: string of the commit message
    :param committer: string of the committer

    :return: None
    
    """
    # Get the current logs.md file from the logging-repository
    url = "https://api.github.com/repos/charliemeyer2000/logging-repository/contents/detailed-logs.md"
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}'
    }

    # gets the current detailed-logs.md file
    response = requests.get(url=url, headers=headers)
    current_content = response.json()['content']
    current_content = base64.b64decode(current_content).decode('ascii', 'ignore')

    # Gets the current date and time
    current_date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

    # Create a new addition to the logs.md file
    title = f"### {committer}: '{commit_message}' @ {current_date} to {repository_committed_to}\n"

    # Add the code added and removed to the summary
    summary = f"""
    Code Added:
    """

    for file_name, added_lines in code_added.items():
        summary += f"    File: {file_name}\n"
        for line in added_lines:
            summary += f"    + {line}\n"
        summary += "\n"

    
    summary += """
    Code Removed:
    """

    for file_name, removed_lines in code_removed.items():
        summary += f"    File: {file_name}\n"
        for line in removed_lines:
            summary += f"    - {line}\n"
        summary += "\n"
    
    
    # Add new content to the detailed-logs.md file
    new_content = title + summary + '\n\n' + current_content

        # Encode the new content to base64
    new_content = new_content.encode('ascii', 'ignore')
    new_content = base64.b64encode(new_content)

    # Update the detailed-logs.md file to be the old content + the new content
    data = {
        "message": f"Update detailed-logs.md with commit summary for commit {commit_message}",
        "content": new_content.decode('ascii'),
        "sha": response.json()['sha']
    }

    # Update the detailed-logs.md file
    response = requests.put(url=url, headers=headers, data=json.dumps(data))