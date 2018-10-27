# Cookiecutter template for ansible roles

Template for ansible role with [molecule](https://molecule.readthedocs.io/en/latest/) testing

## Requirements

The template itself only needs python and cookicuter. Install it in a virtualenv if needed doing `pip install cookiecutter`

## What this template provides?

* Initialize a new git repo in the local machine
* Add [.yamllint](https://github.com/adrienverge/yamllint) config file (used by molecule)
* Add .pre-commit-config.yaml used by [pre-commit](http://pre-commit.com/)
* Add .gitignore with common files I don't want to track in git
* Add configuration for [Molecule](http://molecule.readthedocs.io) in the "molecule" folder
  * default molecule scenario uses Vagrant + centos7 (2GB ram)
  * second molecule scenario docker + centos/systemd image
  * molecule runs [testinfra](https://testinfra.readthedocs.io) in verbose mode
* And probably something else that I forget... :)

## Usage

### To initialize the role with cookiecuter
```
$ pip install cookiecutter
$ cookiecutter gh:pescobar/cookiecutter-ansible-role-molecule
```

### To initialize the role with molecule

```
$ molecule init template --url https://github.com/pescobar/cookiecutter-ansible-role-molecule
```

### To test the default scenario vagrant + centos7
```
$ molecule test
```

### To test the second scenario docker + centos/systemd image
```
$ molecule test -s docker
```

## Directory structure
```
role_name/
├── defaults
│   └── main.yml
├── handlers
│   └── main.yml
├── meta
│   └── main.yml
├── molecule
│   ├── default
│   │   ├── create.yml
│   │   ├── destroy.yml
│   │   ├── INSTALL.rst
│   │   ├── molecule.yml
│   │   ├── playbook.yml
│   │   └── prepare.yml
│   ├── docker
│   │   ├── create.yml
│   │   ├── destroy.yml
│   │   ├── Dockerfile.j2
│   │   ├── INSTALL.rst
│   │   ├── molecule.yml
│   │   ├── playbook.yml
│   │   └── prepare.yml
│   └── tests
│       ├── __pycache__
│       │   └── test_default.cpython-27-PYTEST.pyc
│       └── test_default.py
├── README.md
├── tasks
│   └── main.yml
└── vars
    └── main.yml
```
