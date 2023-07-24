# GitHub Bulk Repository Remover

Automate the process of deleting multiple GitHub repositories at once.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [How to Use](#how-to-use)
- [Usage Examples](#usage-examples)
- [License](#license)

## Description

The GitHub Bulk Repository Remover script is a Python tool designed to help you efficiently manage your GitHub repositories. It utilizes the GitHub API to securely access and delete repositories using your GitHub Personal Access Token.

## Features

- Secure and authenticated access to your GitHub account.
- Retrieve a list of your repositories.
- Select and delete multiple repositories at once.
- Streamline your GitHub profile management.
- Easy-to-use interface with clear prompts.

## Requirements

- Python 3.x
- GitHub Personal Access Token (with "delete_repo" scope)

## How to Use

1. Clone or download the repository to your local machine.

2. Install the required Python libraries using pip:

`pip install requests`


3. Set up your GitHub Personal Access Token:

- Go to your GitHub account settings.
- Under "Developer settings," click on "Personal access tokens."
- Generate a new token with the "delete_repo" scope.
- Copy the token and save it securely.

4. Open the `main.py` file and replace `'YOUR_GITHUB_ACCESS_TOKEN'` with your GitHub Personal Access Token.

5. Run the script in your terminal:

`python main.py`


6. The script will fetch your repositories and prompt you to choose which ones to delete.

## Usage Examples

1. To delete a single repository:

`python main.py
Enter the number(s) of the repositories to delete (comma-separated): 2`


2. To delete multiple repositories:

`python main.py
Enter the number(s) of the repositories to delete (comma-separated): 1, 3, 4`


3. To delete all repositories, simply enter all the numbers:

`python main.py
Enter the number(s) of the repositories to delete (comma-separated): 1, 2, 3, 4`

Make sure to replace any placeholders, such as 'YOUR_GITHUB_ACCESS_TOKEN', with the actual values. This README.md file provides detailed instructions on how to use the script, requirements, usage examples, and licensing information, making it informative and user-friendly for potential users of your GitHub Bulk Repository Remover script.