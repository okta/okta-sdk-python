oktasdk-python
=======================

This SDK allows managing an Okta instance via Python.

## :warning: :construction: Alpha Preview :construction: :warning:

**Support Disclaimer:** This SDK is not actively maintained. This SDK is community supported and is maintained by members of the Okta team for developers and IT professionals. This library is not an official Okta product and does not qualify for any Okta support. Anyone who chooses to use this library must ensure that their implementation meets any applicable legal obligations including any Okta terms and conditions

## Running tests

### Pre-conditions

Tests are run via tox under python2/3 environments.
Please, make sure you have installed python2.7 and python3.7 on your system.
It can be done using [`pyenv`](https://github.com/pyenv/pyenv), which is
a python version manager.

```bash
$ pyenv install 2.7.17
$ pyenv install 3.7.7
```

To activate those versions for current directory

```bash
$ pyenv local 2.7.17 3.7.7
```

Also we need to install dev dependencies (which is just `tox` for now).

```bash
$ make install
```

### Running integration tests

```bash
$ make test
```

NB: it'll run mock server behind the scenes (see `npm run test` command and `package.json` for details).

## Releasing a new version

1. Switch to master
2. Bump the version in `okta/__init__.py`
3. Commit changes and run `make push-and-tag`
