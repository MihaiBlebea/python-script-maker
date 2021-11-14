#!/usr/bin/python3

from shutil import copyfile
from pathlib import Path
import argparse
import os


def main():
	parser = argparse.ArgumentParser(
		prog= "script_maker", 
		usage="%(prog)s [options] \"project\"", 
		description="Generate template for new script project.",
	)

	parser.add_argument(
		"project", 
		metavar="project", 
		type=str,
		help="pass in the project name \"\"",
	)

	parser.add_argument(
		"-s",
		dest="scraper",
		required=False, 
		default=False,
		action="store_true",
		help="is scraper required",
	)

	parser.add_argument(
		"-d",
		dest="database",
		required=False, 
		default=False,
		action="store_true",
		help="is database required",
	)

	parser.add_argument(
		"-a",
		dest="ansible",
		required=False, 
		default=False,
		action="store_true",
		help="is ansible required",
	)

	parser.add_argument(
		"-w",
		dest="web",
		required=False, 
		default=False,
		action="store_true",
		help="is web api required",
	)

	args = parser.parse_args()

	project_name = args.project
	if project_name == "":
		print("project name is required")
		return None

	project_name = validate_project_name(project_name)

	create_folder(project_name)
	create_folder(f"{project_name}/src")
	copy_file(project_name, "Makefile")
	copy_file(project_name, ".env")
	copy_file(project_name, ".env.example")
	copy_file(project_name, "README.md")
	copy_file(project_name, "tasks.todo")
	create_execute_file(project_name)
	create_script_file(project_name)

	os.system(f"cd ./{project_name} && make venv-create")

	# copy ansible files
	if args.ansible is True:
		create_folder(f"{project_name}/ansible")
		copy_file(project_name, "ansible/deploy.yaml")
		copy_file(project_name, "ansible/remove.yaml")

	# copy scrapy files
	if args.scraper is True:
		copy_file(project_name, "scrape.py", "src/scrape.py")
		copy_file(project_name, "spider.py", "src/spider.py")
		os.system(f"cd ./{project_name} && make venv-activate && make venv-install package=scrapy")
		os.system(f"cd ./{project_name} && make venv-activate && make venv-install package=scrapy-splash")
		os.system(f"cd ./{project_name} && make venv-lock")

	if args.web is True:
		copy_file(project_name, "Dockerfile")
		copy_file(project_name, ".dockerignore")
		copy_file(project_name, "client.rest")
		os.system(f"cd ./{project_name} && make venv-activate && make venv-install package=flask")
		os.system(f"cd ./{project_name} && make venv-lock")

def create_folder(folder_name):
	Path(f"./{folder_name}").mkdir(parents=True, exist_ok=True)


def current_folder():
	return Path(__file__).parent.resolve()


def copy_file(project_name, file, dest = None):
	"""
    Copy a file from the current folder to the destination project folder.
    """
	cur_folder = current_folder()
	if dest is None:
		copyfile(f"{cur_folder}/templates/{file}", f"./{project_name}/{file}")
		return

	copyfile(f"{cur_folder}/templates/{file}", f"./{project_name}/{dest}")


def create_execute_file(project_name):
	cur_folder = current_folder()
	temp = open(f"{cur_folder}/templates/execute.sh", "r")
	content = temp.read().replace("project", project_name)
	temp.close()

	f = open(f"{project_name}/execute.sh", "w")
	f.write(content)
	f.close()


def create_script_file(project_name):
	cur_folder = current_folder()
	temp = open(f"{cur_folder}/templates/execute.py", "r")
	content = temp.read()
	temp.close()

	f = open(f"{project_name}/src/{project_name}.py", "w")
	f.write(content)
	f.close()


def validate_project_name(project_name):
	return project_name.lower().replace(" ", "_").replace("-", "_")


if __name__ == "__main__":
	main()