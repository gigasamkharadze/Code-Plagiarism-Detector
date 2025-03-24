import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
import yaml


def task(repository_url, repository_name, script_path, destination_base_path):
    destination_path = os.path.join(destination_base_path, repository_name)
    try:
        subprocess.run([script_path, repository_url, destination_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error cloning {repository_name}: {e}")


def main():
    _dir = os.path.dirname(os.path.realpath(__file__))
    script_path = os.path.join(_dir, 'scripts', 'clone.sh')
    destination_base_path = os.path.join(_dir, 'repositories')

    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    repositories = config['repositories']

    with ThreadPoolExecutor(max_workers=2) as executor:
        for repository in repositories:
            url, name = repository['url'], repository['name']
            executor.submit(task, url, name, script_path, destination_base_path)


if __name__ == "__main__":
    main()