# devnotes

Working the exercises in [Publishing Python Packages](https://pypackages.com/) by Dane Hillard

Book:
- O'Reilly: [Publishing Python Packages](https://learning.oreilly.com/library/view/publishing-python-packages/9781617299919/)
- GitHub: [daneah/publishing-python-packages](https://github.com/daneah/publishing-python-packages)

---

## Tools Installed

Installed [asdf](https://asdf-vm.com/).

Initially, installing Python versions using `asdf` failed due to missing dependencies.

To build Python on the Linux Mint host I was using, I needed to install some packages as described in the [pyenv Wiki](https://github.com/pyenv/pyenv/wiki#suggested-build-environment). *Pyenv* was not used, but the list of build requirements for Python worked.

Used `asdf` to install several Python versions:

```bash
asdf install python 3.10.10
asdf install python 3.9.16
```

[Installed Rust](https://www.rust-lang.org/tools/install) to have `cargo` available.

Installed [Python launcher for Unix](https://github.com/brettcannon/python-launcher).

```bash
cargo install python-launcher
```
Installed [pipx](https://github.com/pypa/pipx/).

```bash
py -m pip install --user pipx
py -m pipx ensurepath
```

Installed other tools using **pipx**:
- [build](https://pypa-build.readthedocs.io/en/latest/index.html) ([github](https://github.com/pypa/build))
- [tox](https://tox.wiki/en/latest/)
- [pre-commit](https://pre-commit.com/)
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/)

```bash
pipx install build
pyproject-build --version

pipx install tox
tox --version

pipx install pre-commit
pre-commit --version

pipx install cookiecutter
cookiecutter --version
```

---

## Coursework Links and Commits

[Python Documentation](https://docs.python.org/3/)

[An Overview of Packaging for Python](https://packaging.python.org/en/latest/overview/) - Python Packaging User Guide

[TOML](https://toml.io/en/) - Tom's Obvious Minimal Language

[PEP 518](https://peps.python.org/pep-0518/) - Specifying Minimum Build System Requirements for Python Projects

- [x] **Initial commit**
<sup>Commit [b2ca63c](https://github.com/wmelvin/pub-py-pkg/commit/b2ca63c01dac7c7bde296fddcb56642138934511) (2023-04-06 18:53:31)</sup>

- [x] **Add setuf.cfg**
<sup>Commit [3e3508d](https://github.com/wmelvin/pub-py-pkg/commit/3e3508dd3425807dd911569feb4add6fcb08e1db) (2023-04-06 18:57:25)</sup>

---

[gitignore/Python](https://github.com/github/gitignore/blob/main/Python.gitignore)

- [x] **Add .gitignore**
<sup>Commit [827ba99](https://github.com/wmelvin/pub-py-pkg/commit/827ba99d00a9e015057ba21fb8d72e761889732c) (2023-04-06 19:01:09)</sup>

---

### 3.2.2 Optional core metadata

#### About Metadata
- [PEP 621](https://peps.python.org/pep-0621/) - Storing project metadata in pyproject.toml
- [PEP 241](https://peps.python.org/pep-0241/) - Metadata for Python Software Packages
- [PEP 301](https://peps.python.org/pep-0301/) - Package Index and Metadata for Distutils
- [PEP 314](https://peps.python.org/pep-0314/) - Metadata for Python Software Packages 1.1
- [PEP 345](https://peps.python.org/pep-0345/) - Metadata for Python Software Packages 1.2
- [PEP 566](https://peps.python.org/pep-0566/) - Metadata for Python Software Packages 2.1

- [x] **Add metadata**
<sup>Commit [8ece636](https://github.com/wmelvin/pub-py-pkg/commit/8ece6364021b140b3ba9a784e38742459c765125) (2023-04-06 19:12:47)</sup>

- [x] **Add description**
<sup>Commit [e705ee2](https://github.com/wmelvin/pub-py-pkg/commit/e705ee24d9e1835b0c0d30cd1353d792d1de39fe) (2023-04-06 19:16:19)</sup>

---

- [x] **Add README.md**
<sup>Commit [f07c4b9](https://github.com/wmelvin/pub-py-pkg/commit/f07c4b96c683f65a82688136c761fe4e2da4422a) (2023-04-06 19:25:12)</sup>

---

### 3.2.3 Specifying a license

[SPDX License List](https://spdx.org/licenses/) - Software Package Data Exchange (SPDX)

[Classifiers](https://pypi.org/classifiers/) - PyPI

- [x] **Add LICENSE**
<sup>Commit [c2a33fd](https://github.com/wmelvin/pub-py-pkg/commit/c2a33fd91dc15bdafb9007b5fbab9540531f5af3) (2023-04-06 19:44:41)</sup>

---

### 3.3 Controlling source code and file discovery

Ionel's codelog: [Packaging a python library](https://blog.ionelmc.ro/2014/05/25/python-packaging/)

- [x] **Add imppkg**
<sup>Commit [77dfe8f](https://github.com/wmelvin/pub-py-pkg/commit/77dfe8f1ccbc1b149eb72890510e48b3445dd648) (2023-04-09 08:32:17)</sup>

- [x] **Add options to setup.cfg**
<sup>Commit [401a48b](https://github.com/wmelvin/pub-py-pkg/commit/401a48bac81806bf909f7178dd96c08002101bda) (2023-04-09 08:39:53)</sup>

- [x] **Exclude any test modules outside test dir**
<sup>Commit [c696ee9](https://github.com/wmelvin/pub-py-pkg/commit/c696ee9378db50e4759ce1e771a31cc09a70a047) (2023-04-09 08:42:42)</sup>

---

### 3.4 Including non-Python files in a package

- [x] **Add data.json and MANIFEST.in**
<sup>Commit [ae5db55](https://github.com/wmelvin/pub-py-pkg/commit/ae5db559edcfd9cb9aa43b4dca9b71c616bd13ef) (2023-04-09 08:53:46)</sup>

- [x] **Add option to include package data in wheel**
<sup>Commit [fddce0b](https://github.com/wmelvin/pub-py-pkg/commit/fddce0b16728dced74e37ff148aa7bd59f6d20e9) (2023-04-09 08:56:56)</sup>

---

### 4.2 Creating a C extension for Python

Wikipedia: [Harmonic mean](https://en.wikipedia.org/wiki/Harmonic_mean)

[Cython: C-Extensions for Python](https://cython.org/)

- [x] **Add harmonic_mean.py**
<sup>Commit [cf23142](https://github.com/wmelvin/pub-py-pkg/commit/cf2314235cff84303573cf2ebc0b2388752ac1f7) (2023-04-15 07:03:50)</sup>

*Check execution time before creating extension.*

```bash
py -m timeit --setup 'from harmonic_mean import harmonic_mean' \
  --setup 'from random import randint' \
  --setup 'nums = [randint(1, 1_000_000) for _ in range(1_000_000)]' \
  'harmonic_mean(nums)'

5 loops, best of 5: 78.9 msec per loop
```

- [x] **Rename harmonic_mean as Cython source**
<sup>Commit [13560d5](https://github.com/wmelvin/pub-py-pkg/commit/13560d58dd904205615ccbe340c4fde53cf99940) (2023-04-15 07:05:46)</sup>

- [x] **Add Cython to the build process**
<sup>Commit [7c706ab](https://github.com/wmelvin/pub-py-pkg/commit/7c706ab42bec7b726e46cf8512ae00f616d2d617) (2023-04-16 07:21:41)</sup>

- [x] **Add setup.py to run Cython**
<sup>Commit [bc26d12](https://github.com/wmelvin/pub-py-pkg/commit/bc26d12c18fe02960e74d35a70cb3a26847baa7a) (2023-04-16 07:34:11)</sup>

*Check execution time after creating Cython extension.*

```bash
py -m timeit --setup 'from imppkg.harmonic_mean import harmonic_mean' \
  --setup 'from random import randint' \
  --setup 'nums = [randint(1, 1_000_000) for _ in range(1_000_000)]' \
  'harmonic_mean(nums)'

5 loops, best of 5: 62.6 msec per loop
```

---

- [x] **Git ignore .venv**
<sup>Commit [a594834](https://github.com/wmelvin/pub-py-pkg/commit/a59483416a9bdeb99e7a234524af40401175d746) (2023-04-24 20:38:53)</sup>

- [x] **Git ignore build dir**
<sup>Commit [2e2b403](https://github.com/wmelvin/pub-py-pkg/commit/2e2b403595be42f513900163ea742d75ec9828ae) (2023-04-24 20:54:48)</sup>

---

### 4.2.5 Specifying required Python versions

[PEP 440](https://peps.python.org/pep-0440/) - Version Identification and Dependency Specification

- [x] **Specify minimum Python version**
<sup>Commit [2e858d6](https://github.com/wmelvin/pub-py-pkg/commit/2e858d6c8857c748e042893b8c5c35abc269c89a) (2023-04-25 21:42:52)</sup>

---

[pypa/build](https://github.com/pypa/build/blob/cd7ee56bcc00a89741811d937238c889710b053d/setup.cfg#L43) specifies a *console_scripts* configuration for launching from the command line using `pyproject-build`.

- [x] **Add harmony.py console script**
<sup>Commit [892033a](https://github.com/wmelvin/pub-py-pkg/commit/892033a34e4aeaa8783b030eae028615d03f1e8a) (2023-04-25 22:04:05)</sup>

---

### 4.4 Specifying dependencies for Python packages

- [x] **Add termcolor dependency**
<sup>Commit [5e63563](https://github.com/wmelvin/pub-py-pkg/commit/5e63563bc41918f0c9bc2f84ede51581d358f079) (2023-04-26 20:53:13)</sup>

---

### 5.1 Integrating a testing setup

- [x] **Add initial test that always passes**
<sup>Commit [fd33da7](https://github.com/wmelvin/pub-py-pkg/commit/fd33da77dff24b7b23feb2612a7f1e2ad6e11676) (2023-05-05 20:28:02)</sup>

- [x] **Configure testpaths and move test**
<sup>Commit [2dca65b](https://github.com/wmelvin/pub-py-pkg/commit/2dca65b6d09bce448ca8136250421c7071c40652) (2023-05-05 20:47:11)</sup>

---

### 5.1.2 Adding test coverage measurement

[Coverage.py](https://coverage.readthedocs.io/en/7.2.5/)

- [x] **Add pytest-cov. Delete hello.py**
<sup>Commit [b710f1e](https://github.com/wmelvin/pub-py-pkg/commit/b710f1eb8ff55c61590902515d0764c1028d52d8) (2023-05-07 11:05:54)</sup>

- [x] **Configure coverage testing**
<sup>Commit [42eb871](https://github.com/wmelvin/pub-py-pkg/commit/42eb871b697b6b871931a6041e7722637c90addd) (2023-05-07 13:45:12)</sup>

- [x] **Handle errors in main. Add test for happy path**
<sup>Commit [592a961](https://github.com/wmelvin/pub-py-pkg/commit/592a961787d5881db00930eee04ffd9c47751988) (2023-05-11 19:09:36)</sup>

- [x] **Fix result not set. Add tests for unhappy input**
<sup>Commit [7bff327](https://github.com/wmelvin/pub-py-pkg/commit/7bff327d71e90b9e90d6da8305cc3e418c8bfa69) (2023-05-11 19:29:44)</sup>

---

### 5.2.1 Addressing repetitive, data-driven tests

- [x] **Replace 3 tests with one using parametrize**
<sup>Commit [5ecd73d](https://github.com/wmelvin/pub-py-pkg/commit/5ecd73d16401164678095d4fa34c9fc5766b13ea) (2023-05-24 10:24:22)</sup>

---

### 5.2.2 Addressing frequent package installation

tox: [Configuration](https://tox.wiki/en/latest/config.html#setup-cfg)

tox: [parallel-mode](https://tox.wiki/en/latest/user_guide.html#parallel-mode)

- [x] **Add tox configuration**
<sup>Commit [6883cdc](https://github.com/wmelvin/pub-py-pkg/commit/6883cdcd5b2fd0272991be81beeeacfeda687819) (2023-05-26 21:55:59)</sup>


- [x] **Configure tox to run pytest**
<sup>Commit [cd8db98](https://github.com/wmelvin/pub-py-pkg/commit/cd8db98ee9cd0729306d609c9e0054b637ffa3ac) (2023-05-31 18:05:15)</sup>

---

### 5.2.4 Tips for quicker and safer testing

GitHub: [pytest-dev/pytest-randomly](https://github.com/pytest-dev/pytest-randomly) - Pytest plugin to randomly order tests and control random.seed.

- [x] **Add pytest-randomly to testenv**
<sup>Commit [4eb0986](https://github.com/wmelvin/pub-py-pkg/commit/4eb09863d5f0ae5837dc54d662d06f48ee423732) (2023-06-01 11:30:18)</sup>

strict-markers: [Working with custom markers](https://docs.pytest.org/en/7.3.x/example/markers.html)

- [x] **Add --strict-markers to pytest addopts**
<sup>Commit [8372504](https://github.com/wmelvin/pub-py-pkg/commit/8372504c01c5fff19a7537fe0f087a60094073fa) (2023-06-01 11:32:26)</sup>

---

### 6.1.1 Creating nondefault tox environments

- [x] **Add non-default tox environment get_my_ip**
<sup>Commit [7e6d2cb](https://github.com/wmelvin/pub-py-pkg/commit/7e6d2cb97a823831413fd1c02c6a7bee114cad8f) (2023-06-01 17:26:25)</sup>

---

### 6.2 Analyzing type safety

[An Introduction to the PyCQA](https://pycqa.org/introduction.html)

GitHub: [python/mypy](https://github.com/python/mypy) - Optional static typing for Python

[The mypy configuration file](https://mypy.readthedocs.io/en/stable/config_file.html)

[PEP 420](https://peps.python.org/pep-0420/) - Implicit Namespace Packages

- [x] **Refactor harmony.main. Add typecheck tox config**
<sup>Commit [54fd817](https://github.com/wmelvin/pub-py-pkg/commit/54fd8170ab634b58c4eb813883218262640a9d57) (2023-06-02 13:28:44)</sup>

- [x] **Add mypy configuration for type checking**
<sup>Commit [dd61bfa](https://github.com/wmelvin/pub-py-pkg/commit/dd61bfa1dcb7b8edbb7ea961028ddd307392606d) (2023-06-02 16:13:45)</sup>

- [x] **Add py.typed file**
<sup>Commit [0fffa95](https://github.com/wmelvin/pub-py-pkg/commit/0fffa95e102f3f09480f398f6233eb41d1b2a71d) (2023-06-02 16:17:14)</sup>

---

### 6.3 Creating a tox environment for code formatting

[PEP 8](https://peps.python.org/pep-0008/) - Style Guide for Python Code

Docs: [Black](https://black.readthedocs.io/en/stable/)

- [x] **Add black formatter. Apply reformat**
<sup>Commit [534425a](https://github.com/wmelvin/pub-py-pkg/commit/534425ac2be8c6306be7987d2fbf627210bd3a23) (2023-06-02 16:33:23)</sup>

- [x] **Add config for black. Reformat**
<sup>Commit [cae3efa](https://github.com/wmelvin/pub-py-pkg/commit/cae3efa44cb9126e40efd6cdf8e17f5d91263c1f) (2023-06-03 16:29:26)</sup>

Alternatives to *black* formatter:
- GitHub: [hhatto/autopep8](https://github.com/hhatto/autopep8) - A tool that automatically formats Python code to conform to the PEP 8 style guide.
- GitHub: [google/yapf](https://github.com/google/yapf) - A formatter for Python files

---

### 6.4 Creating a tox environment for linting

[Flake8](https://flake8.pycqa.org/en/latest/) - Your Tool For Style Guide Enforcement

Flake8 combines:
- GitHub: [PyCQA/pyflakes](https://github.com/PyCQA/pyflakes) - A simple program which checks Python source files for errors
- GitHub: [PyCQA/pycodestyle](https://github.com/PyCQA/pycodestyle) - Simple Python style checker in one Python file
- GitHub: [PyCQA/mccabe](https://github.com/PyCQA/mccabe) - McCabe complexity checker for Python

The author recommends [Radon](https://radon.readthedocs.io/en/latest/) for complexity checking, done separately from linting.

GitHub: [PyCQA/flake8-bugbear](https://github.com/PyCQA/flake8-bugbear) - A plugin for Flake8 finding likely bugs and design problems in your program. Contains warnings that don't belong in pyflakes and pycodestyle.

flake8 documentation: [Full Listing of Options and Their Descriptions](https://flake8.pycqa.org/en/latest/user/options.html)

Alternative linters:
- GitHub: [pylint-dev/pylint](https://github.com/pylint-dev/pylint)
- GitHub: [landscapeio/prospector](https://github.com/landscapeio/prospector)
- GitHub: [PyCQA/bandit](https://github.com/PyCQA/bandit)
- GitHub: [jendrikseipp/vulture](https://github.com/jendrikseipp/vulture)

- [x] **Add linting with flake8.**
<sup>Commit [1ec1c79](https://github.com/wmelvin/pub-py-pkg/commit/1ec1c796d387ebeba6fce92ba3cf3f974eeeed14) (2023-06-03 17:15:21)</sup>

---

### 7.2 Continuous integration with GitHub Actions

From the book:
> You need to make use of the following **GitHub Actions concepts** to build your CI pipeline:
> - **Workflow** - The highest level of granularity for a CI pipeline. You can create multiple workflows that happen in response to different events.
> - **Job** - A high-level phase you define for a workflow, such as building or testing something.
> - **Step** - A specific task you define in a job, usually consisting of a single shell command. Steps can also reference other predefined actions, which is useful when building off of common tasks like checking out your code.
> - **Trigger** - An event or activity that causes a workflow to happen. Even when a workflow is triggered, you can skip jobs in that workflow conditionally with expressions.
> - **Expression** - One of a set of GitHub-specific conditions and values that you can check to control your CI pipeline.

Alternatives:
- [GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
- [CircleCI](https://circleci.com/)
- [Azure DevOps](https://azure.microsoft.com/en-us/products/devops/)
- [Google Cloud CI/CD Platform](https://cloud.google.com/build)
- [Jenkins](https://www.jenkins.io/)

Regarding *Travis CI*, the author says
> I strongly recommend staying away from Travis CI, and I won’t link to it here. Although it used to be one of the most beloved platforms for open source projects, it has suffered from slow feature development, poor communication, security concerns, and a push toward paid plans since its acquisition in 2019.

I call this out not to pick on Travis CI, but as a reminder to look into it closely if in a situation where it is being considered.

---

[GitHub Actions](https://github.com/features/actions)

[Learn GitHub Actions](https://docs.github.com/en/actions/learn-github-actions)

[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idruns-on)

[The Official YAML Web Site](https://yaml.org/)

- [x] **Add workflow main.yml**
<sup>Commit [c9080ca](https://github.com/wmelvin/pub-py-pkg/commit/c9080cab48f1e47b88678642b255e6f6e2bb3c16) (2023-06-06 13:39:28)</sup>

- [x] **Change hello message**
<sup>Commit [3c64f87](https://github.com/wmelvin/pub-py-pkg/commit/3c64f87e0c81bf61759735db82e5087a578d12a8) (2023-06-06 13:46:13)</sup>

---

Installed the [indent-rainbow](https://marketplace.visualstudio.com/items?itemName=oderwat.indent-rainbow) extension for Visual Studio Code. It helps when working with YAML.

- [x] **Add format job to workflow**
<sup>Commit [513372e](https://github.com/wmelvin/pub-py-pkg/commit/513372ef308215f76d5f1fc9317d1b4fa889af10) (2023-06-07 11:58:25)</sup>

- [x] **Edit workflow**
<sup>Commit [fe39466](https://github.com/wmelvin/pub-py-pkg/commit/fe39466e00b4d83dbbada8bcb449573b12276975) (2023-06-07 12:04:16)</sup>

- [x] **Add lint job to workflow**
<sup>Commit [85a1f38](https://github.com/wmelvin/pub-py-pkg/commit/85a1f385e06ca1514ea695a46ccff6f674e43e99) (2023-06-07 13:17:23)</sup>

- [x] **Edit lint job**
<sup>Commit [3ded6de](https://github.com/wmelvin/pub-py-pkg/commit/3ded6deb3f9ef080f89da38d4b037d506de48282) (2023-06-07 13:22:50)</sup>

- [x] **Add typecheck job to workflow**
<sup>Commit [41fe818](https://github.com/wmelvin/pub-py-pkg/commit/41fe818d5a581a276a19ed70ca217edca21ee852) (2023-06-07 15:17:50)</sup>

---

### 7.3.1 Running a job multiple times with a build matrix

GitHub Docs: [Contexts](https://docs.github.com/en/actions/learn-github-actions/contexts)

- [x] **Add test job to workflow**
<sup>Commit [16753aa](https://github.com/wmelvin/pub-py-pkg/commit/16753aabe7bb7ddedadba30c99b6e6cc960145ee) (2023-06-07 15:31:59)</sup>

---

### 7.3.2 Building Python package distributions for a variety of platforms

GitHub: [pypa/cibuildwheel](https://github.com/pypa/cibuildwheel) - Build Python wheels for all the platforms on CI with minimal configuration.

- [x] **Add wheels job to workflow**
<sup>Commit [a95c138](https://github.com/wmelvin/pub-py-pkg/commit/a95c138dbbb701fab4ccc72899d29d1463386344) (2023-06-07 17:52:17)</sup>

- [x] **Add build_dist job to workflow**
<sup>Commit [3dc1bbe](https://github.com/wmelvin/pub-py-pkg/commit/3dc1bbe3b624792b44692bafae39fcadc9d29dfa) (2023-06-07 18:20:01)</sup>

- [x] **Remove macos from wheels matrix for now**
<sup>Commit [9c27628](https://github.com/wmelvin/pub-py-pkg/commit/9c27628ec07db19470e62acb3fc3e53a5187eabd) (2023-06-07 18:25:12)</sup>

---

### 7.4 Publishing a package

Created an account on [PyPI](https://pypi.org/) - The Python Package Index.

The Python Package Index makes [TestPyPI](https://test.pypi.org/) available for testing the publishing process (using a separate account). *Did not use this.*

On PyPI, created an API token at `https://pypi.org/manage/account/token/`.
- name: `pypkg1`
- scope: `Project "pubpypack-harmony-bill-melvin"`

Copied token and pasted as GitHub secret.
- On GitHub repo page, select Settings
- Secrets and Variables
- Actions
- New repository secret
- PYPI_API_TOKEN

The [twine](https://twine.readthedocs.io/en/stable/) tool is used to publish.

The [pypi-publish](https://github.com/marketplace/actions/pypi-publish) GitHub Action runs twine.

- [x] **Rename package for publishing**
<sup>Commit [b029cc7](https://github.com/wmelvin/pub-py-pkg/commit/b029cc7fd56aa6db3432c7a5891c971c00083b6c) (2023-06-08 08:57:19)</sup>

- [x] **Increment version**
<sup>Commit [223d679](https://github.com/wmelvin/pub-py-pkg/commit/223d679356c2b470bac645cab84674d2ff69bf0e) (2023-06-08 22:12:50)</sup>

- [x] **Add publish job to workflow**
<sup>Commit [d8307a1](https://github.com/wmelvin/pub-py-pkg/commit/d8307a1974de1b78e2506ff1a1b440e44a543f00) (2023-06-09 09:38:49)</sup>

- [x] **Edit publish job**
<sup>Commit [44c1101](https://github.com/wmelvin/pub-py-pkg/commit/44c11016a54ba0641f6fb9d3b60b866c9084d0a4) (2023-06-09 10:05:20)</sup>

- [x] **Increment version to publish**
<sup>Commit [f54c2ec](https://github.com/wmelvin/pub-py-pkg/commit/f54c2ec56f2a744f33406479b765342564ae5e70) (2023-06-09 10:08:40)</sup>

- [x] **Update gh-action-pypi-publish version**
<sup>Commit [01a04e0](https://github.com/wmelvin/pub-py-pkg/commit/01a04e010d66a84124c0ac78fbd9d0199a257aa9) (2023-06-09 10:51:17)</sup>

---

### 8 Authoring and maintaining documentation

[Sphinx documentation](https://www.sphinx-doc.org/en/master/)

[reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)

[Read the Docs](https://readthedocs.org/)

[ISO 639-2 Language Code List](https://www.loc.gov/standards/iso639-2/php/code_list.php) - Codes for the representation of names of languages (Library of Congress)

PyPI: [sphinx-autobuild](https://pypi.org/project/sphinx-autobuild/)

Sphinx documentation: [sphinx-apidoc](https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html)

Sphinx documentation: [sphinx.ext.autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) - Include documentation from docstrings


- [x] **Add docs env. Run sphinx-quickstart**
<sup>Commit [b67b906](https://github.com/wmelvin/pub-py-pkg/commit/b67b90653ed0d1f683b4b90e89a15bf4a8854de7) (2023-06-10 14:19:07)</sup>

- [x] **Replace sphinx-quickstart with sphinx-build.**
<sup>Commit [6492e65](https://github.com/wmelvin/pub-py-pkg/commit/6492e65f95155e7b0aed242abc00db539c770efa) (2023-06-10 14:30:53)</sup>

- [x] **Add devdocs env to use sphinx-autobuild**
<sup>Commit [46339fc](https://github.com/wmelvin/pub-py-pkg/commit/46339fc02f1a6fe7e20f2a046b2611a0180ba8b8) (2023-06-10 14:42:20)</sup>

- [x] **Add sphinx-apidoc**
<sup>Commit [a5f4ea1](https://github.com/wmelvin/pub-py-pkg/commit/a5f4ea103f2c70c6671b61bff0ae9cd79728f481) (2023-06-10 15:40:56)</sup>

- [x] **Building docs needs install. Add some docstrings**
<sup>Commit [25c3273](https://github.com/wmelvin/pub-py-pkg/commit/25c32730e7ce63cc77d03a450011a5f615b3a264) (2023-06-11 21:22:07)</sup>

---

Read the Docs user documentation: [Configuration file v2](https://docs.readthedocs.io/en/stable/config-file/v2.html)

Sphinx documentation: [Application API - sphinx-core-events](https://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx-core-events)

Sphinx documentation: [Application API - event-builder-inited](https://www.sphinx-doc.org/en/master/extdev/appapi.html#event-builder-inited)

- [x] **Add importlib to get package version**
<sup>Commit [215aea8](https://github.com/wmelvin/pub-py-pkg/commit/215aea82f9253b5485577dfc70fe4a068f1ddae1) (2023-06-13 11:32:52)</sup>

- [x] **Add link to book site to README**
<sup>Commit [2852455](https://github.com/wmelvin/pub-py-pkg/commit/285245592a3d5252adcb73535aac4e96d21ecf33) (2023-06-13 11:44:57)</sup>

- [x] **Add note to README**
<sup>Commit [3471e88](https://github.com/wmelvin/pub-py-pkg/commit/3471e8895316bedc938382fdd3804524439dcc96) (2023-06-13 11:51:40)</sup>

- [x] **Hold off building for Windows and Mac**
<sup>Commit [d54ca1a](https://github.com/wmelvin/pub-py-pkg/commit/d54ca1a3dc3c3cb833ab5b586939db6ff565792e) (2023-06-13 11:57:44)</sup>

---

- [x] **Configure readthedocs**
<sup>Commit [8ca457f](https://github.com/wmelvin/pub-py-pkg/commit/8ca457faadd84d0247aa565d4d1e958fc15e5712) (2023-06-13 22:39:04)</sup>

- [x] **Fix Sphinx.connect args**
<sup>Commit [82874fb](https://github.com/wmelvin/pub-py-pkg/commit/82874fb2be0ffde7a9aaeded62feafd3e768dc4a) (2023-06-13 22:50:53)</sup>

---

**More Sphinx**

Sphinx documentation: [Roles](https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html)
Added: `2023-06-15 16:47:49`
Folder: `/toolbar/PyPkg/D/`

Sphinx documentation: [sphinx.ext.intersphinx](https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html) - Link to other projects

Sphinx + Markdown: [MyST](https://myst-parser.readthedocs.io/en/latest/faq/index.html)

Python documentation: [doctest](https://docs.python.org/3/library/doctest.html) - Test interactive Python examples

Sphinx documentation: [sphinx.ext.napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html) - Support for NumPy and Google style docstrings

Sphinx documentation: [HTML Theming](https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes)

[Sphinx Themes Gallery](https://sphinx-themes.org/)

---

### 9.2.2 Mitigating security vulnerabilities with Dependabot

[CodeQL](https://codeql.github.com/)

[Cron Helper](https://cron.help/) - Crontab syntax for us humands.

- [x] **Configure code scanning**
<sup>Commit [1cecb85](https://github.com/wmelvin/pub-py-pkg/commit/1cecb854178566036a463fe2b41632bea9eeb45f) (2023-06-20 17:35:09)</sup>

---
