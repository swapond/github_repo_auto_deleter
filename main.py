import requests

def get_user_repos(token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    url = 'https://api.github.com/user/repos'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repos = response.json()
        return repos
    else:
        raise Exception(f"Failed to retrieve repositories: {response.status_code} - {response.text}")

def delete_repository(repo_name, token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    url = f'https://api.github.com/repos/swapond/{repo_name}'  # Replace 'your_username' with your GitHub username
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f'Repository "{repo_name}" deleted successfully.')
    else:
        print(f'Error deleting repository "{repo_name}": {response.status_code} - {response.text}')

def prompt_for_removal(repos):
    print("Your repositories:")
    for idx, repo in enumerate(repos, 1):
        print(f"{idx}. {repo['name']}")

    while True:
        selected = input("Enter the number(s) of the repositories to delete (comma-separated): ").strip()
        selected_indices = [int(idx.strip()) - 1 for idx in selected.split(",") if idx.strip().isnumeric()]

        if not selected_indices:
            print("Please enter at least one valid number.")
        elif all(idx in range(len(repos)) for idx in selected_indices):
            return [repos[idx]['name'] for idx in selected_indices]
        else:
            print("Invalid number(s) entered. Please try again.")

if __name__ == "__main__":
    token = "<GITHUB_ACCESS_TOKEN>"  # Replace this with your actual GitHub access token

    try:
        repositories = get_user_repos(token)
        repos_to_delete = prompt_for_removal(repositories)

        for repo in repos_to_delete:
            delete_repository(repo, token)

    except Exception as e:
        print(f"An error occurred: {e}")
