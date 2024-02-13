task_specific_env_variable % task list_directories_under_parent_dir 
task: [list_directories_under_parent_dir] find $DIR -type d
../../../taskfile_tutorial
../../../taskfile_tutorial/environment_variables
../../../taskfile_tutorial/environment_variables/task_specific_env_variable
../../../taskfile_tutorial/call_another_task
../../../taskfile_tutorial/special_variables
../../../taskfile_tutorial/special_variables/sub_directory
../../../taskfile_tutorial/special_variables/sub_directory_2
../../../taskfile_tutorial/variables
../../../taskfile_tutorial/multiple_taskfiles_in_1_taskfile
../../../taskfile_tutorial/hello

task_specific_env_variable % task list_files_under_current_dir 
task: [list_files_under_current_dir] find $DIR -type f
/some/long/path/taskfile_tutorial/environment_variables/task_specific_env_variable/Taskfile.yml

task_specific_env_variable % DIR=new_dir_name task create_new_dir
task: [create_new_dir] mkdir -p $DIR && ls ./
Taskfile.yml    new_dir_name

---

variables % task print-global-variable
Hello

variables % task run_same_task_multiple_times_with_different_variables
       7
      17


---

special_variables % tree -L 2
.
├── Taskfile.yml
├── sub_directory
│   ├── 1.md
│   ├── a.txt
│   └── b.txt
└── sub_directory_2
    ├── 2.md
    └── c.txt

special_variables % cd sub_directory_2

special_variables/sub_directory_2 % task count_files 
Number of files in /special_variables/sub_directory_2 
       2

special_variables/sub_directory_2 % task count_only_txt_files -- '*.txt'
Number of files in /special_variables/sub_directory_2 
       1

---

# Running Task 1
/my/home/directory % cd /some/directory
/some/directory % task --global count_files_inside_current_dir 
Number of files in /some/directory
       6

# Running Task 2
/some/directory % task --global search_files_inside_current_dir -- "*.pdf"

/some/directory/2019BurkovTheHundred-pageMachineLearning.pdf
/some/directory/Generative_AI_Learning_Labs.pdf
/some/directory/thinkstats.pdf

# Running Task 3
/my/home/directory % cd /some/directory
/some/directory % task --global search_all_files_except -- ".pdf"

/some/directory/understanding_mathematics.jpeg
/some/directory/git_cheatsheet.jpeg
/some/directory/README.md

---

multi-line-commands % cat contact_details.txt
I am <NAME>. My email id is <EMAIL>

multi-line-commands % task multi-line-replace-command
I am SENTHIL. My email id is senthilkumar.m1901@gmail.com

---

The Python Conda Environments are
base
boto3_local
openai_tiktoken_dotenv_pandas

The Python Docker images are
ubuntu 22.04
amazon/aws-lambda-python 3.8_with_zip
public.ecr.aws/lambda/python 3.8
