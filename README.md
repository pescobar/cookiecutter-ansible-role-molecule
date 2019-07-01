[![Build Status](https://travis-ci.org/pescobar/cookiecutter-ansible-role-molecule.svg?branch=master)](https://travis-ci.org/pescobar/cookiecutter-ansible-role-molecule)

# Cookiecutter template for ansible roles

Template for ansible role with [molecule](https://molecule.readthedocs.io/en/latest/) testing

## Requirements

The template itself only needs python, [cookicuter](https://cookiecutter.readthedocs.io/) and [pre-commit](https://pre-commit.com/). Install them doing `pip install cookiecutter pre-commit`

## What this template provides?

* Initialize a new git repo in the local machine
* Add [.yamllint](https://github.com/adrienverge/yamllint) config file (used by molecule)
* Add .pre-commit-config.yaml used by [pre-commit](http://pre-commit.com/)
* Add .gitignore with common files I don't want to track in git
* Add configuration for [Molecule](http://molecule.readthedocs.io) in the "molecule" folder
  * default molecule scenario runs on docker + centos7/systemd image
  * There is another molecule scenario using Vagrant + bento/centos-7 box (1 core - 1GB ram - selinux=permissive)
  * molecule runs [testinfra](https://testinfra.readthedocs.io) in verbose mode
  * the role is executed with [become: true](https://github.com/pescobar/cookiecutter-ansible-role-molecule/blob/master/%7B%7Bcookiecutter.role_name%7D%7D/molecule/default/molecule.yml#L16-L18) (everything is executed as root/sudo)
* Add a travis or Gitlab-CI config file (Optional. By default it's not added)
* And probably something else that I forget... :)

## Usage

### To initialize the role with cookiecuter
```
$ pip install cookiecutter pre-commit
$ cookiecutter gh:pescobar/cookiecutter-ansible-role-molecule
```

### To initialize the role with molecule

```
$ pip install molecule pre-commit
$ molecule init template --url https://github.com/pescobar/cookiecutter-ansible-role-molecule
```

### To test the default scenario docker + centos7/systemd image
```
$ molecule test
```

### To test the scenario with vagrant + centos7
```
$ molecule test -s vagrant
```


## Directory structure
```
role_name/
├── defaults
│   └── main.yml
├── .gitignore
├── .gitlab-ci.yml
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── molecule
│   ├── default
│   │   ├── Dockerfile.j2
│   │   ├── INSTALL.rst
│   │   ├── molecule.yml
│   │   └── playbook.yml
│   ├── tests
│   │   └── test_default.py
│   └── vagrant
│       ├── INSTALL.rst
│       ├── molecule.yml
│       ├── playbook.yml
│       └── prepare.yml
├── .pre-commit-config.yaml
├── README.md
├── tasks
│   └── main.yml
├── .travis.yml
├── vars
│   └── main.yml
└── .yamllint
```
