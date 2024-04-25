# How to contribute to BigCode?

Everyone is welcome to contribute, and we value everybody's contribution. Code
is thus not the only way to help the community. Answering questions, helping
others, reaching out and improving the documentations are immensely valuable to
the community.

Whichever way you choose to contribute, please be mindful to respect our
[code of conduct](https://bigcode-project.org/docs/about/code_of_conduct/).

## You can contribute in so many ways!

There are 4 ways you can contribute to this repository:
* Fixing outstanding issues with the existing code;
* Contributing to the data or to the documentation;
* Submitting issues related to bugs or desired new features.

*All are equally valuable to the community.*

## License

Note that all contributions are licensed under Apache 2.0 by default. The 
Technical Steering Committee (TSC) may approve the use of an alternative 
license or licenses for inbound or outbound contributions on an exception basis. 
To request an exception, please describe the contribution, the alternative 
license, and the justification for using an alternative license for the 
described contribution. License exceptions must be approved by the TSC. 
Contributed files should contain license information indicating the open 
source license or licenses pertaining to the file.

## Submitting a new issue or feature request

Do your best to follow these guidelines when submitting an issue or a feature
request. It will make it easier for us to come back to you quickly and with good
feedback.

### Did you find a bug?

First, we would really appreciate it if you could **make sure the bug was not
already reported** (use the search bar on Github under Issues).

Did not find it? :( So we can act quickly on it, please follow these steps:

* Include your **OS type and version**, the versions of **Python**, **PyTorch** and
  **Tensorflow** when applicable;
* A short, self-contained, code snippet that allows us to reproduce the bug in
  less than 30s;
* Provide the *full* traceback if an exception is raised.

### Do you want a new feature?

A world-class feature request addresses the following points:

1. Motivation first:
  * Is it related to a problem/frustration with the current features? If so, please explain
    why. Providing a code snippet that demonstrates the problem is best.
  * Is it related to something you would need for a project? We'd love to hear
    about it!
  * Is it something you worked on and think could benefit the community?
    Awesome! Tell us what problem it solved for you.
2. Write a *full paragraph* describing the feature;
3. Provide a **code snippet** that demonstrates its future use;
4. In case this is related to a paper, please attach a link;
5. Attach any additional information (drawings, screenshots, etc.) you think may help.

If your issue is well written we're already 80% of the way there by the time you
post it.

## Start contributing! (Pull Requests)

Before writing code, we strongly advise you to search through the existing PRs or
issues to make sure that nobody is already working on the same thing. If you are
unsure, it is always a good idea to open an issue to get some feedback.

You will need basic `git` proficiency to be able to contribute to
BigCode. `git` is not the easiest tool to use but it has the greatest
manual. Type `git --help` in a shell and enjoy. If you prefer books, [Pro
Git](https://git-scm.com/book/en/v2) is a very good reference.

Follow these steps to start contributing:

1. Fork the repository by
   clicking on the 'Fork' button on the repository's page. This creates a copy of the code
   under your GitHub user account.

2. Clone your fork to your local disk, and add the base repository as a remote:

   ```bash
   $ git clone git@github.com:<your Github handle>/<Repo name>.git
   $ cd <Repo name>
   $ git remote add upstream https://github.com/bigcode-project/<Repo name>.git
   ```

3. Create a new branch to hold your development changes:

   ```bash
   $ git checkout -b a-descriptive-name-for-my-changes
   ```

   **Do not** work on the `main` branch.

4. Set up a development environment by running the following command in a virtual environment:

   ```bash
   $ pip install -r requirements.txt
   ```

5. Develop the features on your branch.

   Once you're happy with your changes, add changed files using `git add` and
   make a commit with `git commit` to record your changes locally:

   ```bash
   $ git add modified_file.py
   $ git commit
   ```

   Please write [good commit
   messages](https://chris.beams.io/posts/git-commit/).

   It is a good idea to sync your copy of the code with the original
   repository regularly. This way you can quickly account for changes:

   ```bash
   $ git fetch upstream
   $ git rebase upstream/main
   ```

   Push the changes to your account using:

   ```bash
   $ git push -u origin a-descriptive-name-for-my-changes
   ```

6. Once you are satisfied (**and the checklist below is happy too**), go to the
   webpage of your fork on GitHub. Click on 'Pull request' to send your changes
   to the project maintainers for review.

7. It's ok if maintainers ask you for changes. It happens to core contributors
   too! So everyone can see the changes in the Pull request, work in your local
   branch and push the changes to your fork. They will automatically appear in
   the pull request.


### Checklist

1. The title of your pull request should be a summary of its contribution;
2. If your pull request addresses an issue, please mention the issue number in
   the pull request description to make sure they are linked (and people
   consulting the issue know you are working on it);
3. To indicate a work in progress please prefix the title with `[WIP]`. These
   are useful to avoid duplicated work, and to differentiate it from PRs ready
   to be merged;
4. Make sure existing tests pass;
5. All public methods must have informative docstrings.

### Style guide

For documentation strings, BigCode follows the [google style](https://google.github.io/styleguide/pyguide.html).

**This guide was heavily inspired by the awesome [scikit-learn guide to contributing](https://github.com/scikit-learn/scikit-learn/blob/main/CONTRIBUTING.md).**

### Develop on Windows

On windows, you need to configure git to transform Windows `CRLF` line endings to Linux `LF` line endings:

`git config core.autocrlf input`

One way one can run the make command on Window is to pass by MSYS2:

1. [Download MSYS2](https://www.msys2.org/), we assume to have it installed in C:\msys64
2. Open the command line C:\msys64\msys2.exe (it should be available from the start menu)
3. Run in the shell: `pacman -Syu` and install make with `pacman -S make`
4. Add `C:\msys64\usr\bin` to your PATH environment variable.

You can now use `make` from any terminal (Powershell, cmd.exe, etc) 🎉

### Syncing forked main with upstream `main`

To avoid pinging the upstream repository which adds reference notes to each upstream PR and sends unnecessary notifications to the developers involved in these PRs,
when syncing the main branch of a forked repository, please, follow these steps:
1. When possible, avoid syncing with the upstream using a branch and PR on the forked repository. Instead merge directly into the forked main.
2. If a PR is absolutely necessary, use the following steps after checking out your branch:
```
$ git checkout -b your-branch-for-syncing
$ git pull --squash --no-commit upstream main
$ git commit -m '<your message without GitHub references>'
$ git push --set-upstream origin your-branch-for-syncing
```

## Working on Data

### Data Folder Structure

The data folder is structured as follows:

```
data
├── raw
├── clean
├── processed
```
The `raw` folder contains the raw data that is roughly refined by annotators. The `clean` folder contains the data that is mostly refined based on this [guidelines](https://docs.google.com/document/d/1zgMSoZKL6Z3gWw7n0pvrvhCbTOsPhWb7AD3hORQrs8g/edit). The `processed` folder contains the data that is correctly parsed and ready to be used for evaluation.

### How to Refine Data?
[Data Quality Guidelines](https://docs.google.com/document/d/1zgMSoZKL6Z3gWw7n0pvrvhCbTOsPhWb7AD3hORQrs8g/edit)

There are a few important points to consider when working on data:
- The docstring should be a clear and concise description of the function's behavior.
- All programming problems should have at least 2 libraries imported and used in the function.
- The interactive Python examples in docstrings should be as runnable as possible. They should pass `pytest --doctest-modules` without any errors.
- No additional files or folders should be explicitly accessed in the code. To test the correctness, all required file system operations should be done via `setUp` and `tearDown` methods in the `unittest` test class.
- The test cases should be deterministic. When the problem involves randomness, the random seed should be fixed to ensure the reproducibility of the test results.

The execution environment is mainted in the `requirements.txt` file. To install the required dependencies, run the following command:
```bash
pip install -r requirements.txt
```
If you notice any third-party libraries that are not included in the `requirements.txt` file but used in the `data/process.py` file, please add them with the compatible versions to the `requirements.txt` file.

### How to Validate Data?
We build a GitHub action to validate the data. The action is based on the `script/run.sh`. Specifically, any refined data will be copied to the `data/clean` folder and then parsed based on `script/parser.py`. The parsed data will be stored in the `data/processed` folder. The parsed data will be separate into two splits for `pytest`. The first split will be validated by running `pytest $FILE_NAME` and the second split will be validated by running `pytest --doctest-modules $FILE_NAME`. Please note that we validate each file separately, as `pytest` may fail unexpectedly when validating all files at once.

If you want to validate the data locally, you can run the following command:
```bash
sh script/run.sh
```

If you find any failed test cases, please fix the data in the `data/raw` folder based on the failed problem IDs. The refinement should be based on the [How to Refine Data?](#how-to-refine-data) section.