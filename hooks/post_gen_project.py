#!/usr/bin/env python

# https://github.com/audreyr/cookiecutter/issues/723#issuecomment-350561930

# print(os.getcwd())

import os
import subprocess


def subprocess_cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print proc_stdout


if '{{ cookiecutter.add_travis_config }}' == 'n':
    os.remove('.travis.yml')

if '{{ cookiecutter.add_Gitlab_CI_config }}' == 'n':
    os.remove('.gitlab-ci.yml')

subprocess_cmd('git init')
subprocess_cmd('git add .')
subprocess_cmd('pre-commit install')
subprocess_cmd('git commit -a -m "Initial commit by cookiecutter"')

print "Path to your new role in the local machine is " + os.getcwd()
