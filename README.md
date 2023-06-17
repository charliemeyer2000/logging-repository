# Logging Repository

This repository contains logs and detailed logs of any commits I make that are set up to my webhook endpoint. Any time I commit or perform any action on a repository that has this webhook configured, it edits this `logs.md` file and adds a new `h3` to the file with the commit name, repository committed to, and the date. Below the header, a summary of the code (up to 2000 characters) is generated using GPT 3.5 to summarize the changes. Also, it adds to `detailed-logs.md` all of the adds/removals for that commit. This is useful for me to keep track of what I've done and to see how my code has changed over time.

## How it works

I currently just have a small flask app that runs on port 9000, and am using `ngrok` to forward a public facing endpoint to that localhost. Right now it is just running forever on my Raspberry Pi, but in the future I might make this run on a sub-domain of my [personal website 👋](https://charliemeyer.xyz), if i can figure out how to do that! 

Using the GitHub API, I get information about the commit that was made, look up and do some parsing of the adds/removals of the commit, and then use the GPT 3.5 API to generate a summary of the commit. I then use the GitHub API to edit the `logs.md` file and add the new commit to the top of the file. I also add the detailed logs to the `detailed-logs.md` file.

## Do it yourself 

The code for the actual flask api is not on this repository since it has my GitHub and OpenAI keys on the script too (and is on my Raspberry Pi🥧 , and i'm too lazy to add it 🤷), but if you want me to share you the code, just email me at [charlie@charliemeyer.xyz](mailto:charlie@charliemeyer.xyz) and I can hit you up. 




