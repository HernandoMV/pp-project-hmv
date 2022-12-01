### pp-project-hmv

pip install pp-project-hmv

But!:

import pp_project_hmv


.gitignore lives outside the actual package, together with other stuff

We are using a template


.toml file is needed for having a nice configuration in pypi

for those things that toml does not support you need a setup.py file

There is no reason for most people to have a setup.py file, or a setup.cfg

.toml file is the newest format


Version will be infered automatically and written to the file.

This line: 'pre-commit install' will need to be run by developers to install the package
that allows the automated checks before commiting
