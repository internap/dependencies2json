[![Build Status](https://travis-ci.org/internap/dependencies2json.svg?branch=master)](https://travis-ci.org/internap/dependencies2json)

Library of tools to turn a list of dependencies to unified json structure easy to read

USAGE
=====

```
pip freeze | python <(curl https://raw.githubusercontent.com/internap/dependencies2json/master/pip_dependencies2json.py)

composer show --installed | python <(curl https://raw.githubusercontent.com/internap/dependencies2json/master/composer_dependencies2json.py)
```
