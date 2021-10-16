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

	args = parser.parse_args()

	project_name = args.project
	if project_name == "":
		return None

	project_name = validate_project_name(project_name)

	create_folder(project_name)
	copy_file(project_name, "Makefile")
	copy_file(project_name, ".env")
	copy_file(project_name, ".env.example")
	copy_file(project_name, "README.md")
	copy_file(project_name, "tasks.todo")
	create_execute_file(project_name)
	create_script_file(project_name)

	os.system(f"cd ./{project_name} && make venv-create")


def create_folder(folder_name):
	Path(f"./{folder_name}").mkdir(parents=True, exist_ok=True)


def current_folder():
	return Path(__file__).parent.resolve()


def copy_file(project_name, file):
	"""
    Copy a file from the current folder to the destination project folder.
    """
	cur_folder = current_folder()
	copyfile(f"{cur_folder}/{file}", f"./{project_name}/{file}")


def create_execute_file(project_name):
	cur_folder = current_folder()
	temp = open(f"{cur_folder}/execute.sh", "r")
	content = temp.read().replace("project", project_name)
	temp.close()

	f = open(f"{project_name}/execute.sh", "w")
	f.write(content)
	f.close()


def create_script_file(project_name):
	cur_folder = current_folder()
	temp = open(f"{cur_folder}/template.py", "r")
	content = temp.read()
	temp.close()

	f = open(f"{project_name}/{project_name}.py", "w")
	f.write(content)
	f.close()


def validate_project_name(project_name):
	return project_name.lower().replace(" ", "_").replace("-", "_")


if __name__ == "__main__":
	main()