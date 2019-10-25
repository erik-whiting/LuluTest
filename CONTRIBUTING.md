# Contribution Guide

If you would like to contribute to development, please pull the latest version of development,
create a local branch with a descriptive name, write your code, and push the branch to the
repository. After this, create a pull request for your feature branch to the development branch.
Please do not create PRs against the master branch.

## An example workflow

After you've followed the steps in the [Setup Guide](./SETUP.md), think of a meaningful
name for the branch you're about to make and run these commands:

`git checkout -b my-cool-branch-name`

Write your code and try to make meaningful commits. Here's an example:

```cmd
# Write some code
$> git commit -am "Add new class to a module"
# Make some more changes
$> git commit -am "Add test for new class"
 ```

Once you've finished, please run all tests and correct any new failures. To run
all tests, run the following from the terminal while in the project root:

`python -m unittest discover tests`

Once you've committed everything, run:

`git push origin my-cool-branch-name`

Then, head over to the [repository on Github](https://github.com/erik-whiting/LuluTest)
and create your pull request **against the development branch**. That's it!

### A note on testing

Pull requests without tests will most likely be rejected unless the work
you've done is minor enough that a test would be overkill. If you're an
absolute beginner, don't let this scare you! Writing tests is good practice,
and there are most likely enough tests in the `tests`
directory that you can figure out what you need to do :)

Keep in mind, this framework is designed to be a tool for software testing
and quality assurance, lets practice what we preach.

## Issues Label Guide

* Beginner Friendly - Issues tagged with this label are so tagged because they
are likely within the realm of a novice Pythoneer
* Bug - These issues are functionality-breaking issues that prevent the
software from doing what a user would expect
* Documentation - These issues revolve around documenting the system with
things like READMEs, set up guides, various Wikis, etc
* Duplicate - Issues will be marked duplicate if they have already been
addressed
* Enhancement - These issues are for taking LuluTest from what it is now, to
what we want it to be. It includes adding features as well as refactoring
* Good First Issue - These are issues that will help newcomers to the *project*
in getting acquainted with the project, not neccessarily new programmers
* Help Wanted - These issues are either beyond the expertise of the current
contributors or need further discussion with someone who knows about the issue
at hand
* Integration and Management - Issues around building a CI server, setting up a
Slack chat, and deployment/packaging solutions fall under this label