# Local System Set Up  for Development

This guide will take you from cloning the repository
to getting ready to start coding. There are a few things you need first:
* GitHub Account (duh)
* SSH key to push from command line
  * It's not as hard as it sounds, check out [this guide](https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
* Python!
  * Currently the supported version is Python 3.6
* virtualenv (recommended)
  * Just run `pip install virtualenv`

### Step 1 - Clone the Repository
Navigate to a folder/directory where you'd like to install the project and run

`git clone git@github.com:erik-whiting/LuluTest.git`

cd into the directory and type

`git branch`

The output *should* say "development." If it doesn't, run

`git checkout development`

### Step 2 - Install requirements
If you have virtualenv, go ahead and activate it now. If you already have an
environment you'd like to use, go ahead and use it. If not, cd into the project
root and run

`python -m venv LuLuTest`

You can name your environment whatever you want, I'm just using LuluTest as
an example. To activate the environment, run

Windows: `LuluTest\Scripts\activate.bat`

Unix/MacOS: `LuluTest/bin/activate`

That will activate your virtual environment and you should see `(LuluTest)`
in front of your command prompt.

Now, install the requirements. If you've opted out of using virtualenv, you still
need to do this part

`pip install -r requirements.txt`

Let's make extra sure everything is ready to go by running the test suite. From
the project root, run this command in the terminal:

`python -m unittest discover tests`

### Step 3 - Get ready to contribute!
If you're planning on writing some code and committing a PR, please see the
[Contribution Guide](./CONTRIBUTING.md). For convenience, here is the part
about branching:

Think of a meaningful name for the branch you're about to make and run these commands:

`git checkout -b my-cool-branch-name`

Write your code and try to make meaningful commits. Here's an example:

```cmd
# Write some code
$> git commit -am "Add new class to a module"
# Make some more changes
$> git commit -am "Add test for new class"
 ```

Once you've finished, please run all tests and correct any new failures. To run all
tests, run the following from the terminal while in the project root:

`python -m unittest discover tests`

Once you've committed everything, run:

`git push origin my-cool-branch-name`

Then, head over to the [repository on Github](https://github.com/erik-whiting/LuluTest)
and create your pull request **against the development branch**. That's it!

***

### Setting up selenium webdriver
To be able to run the selenium tests in this project, you will have to install a selenium webdriver. Otherwise you'll get an error similar to this:

`WebDriverException: Message: 'chromedriver' executable needs to be available in the path.`

Firstly, download your preferred browser driver. In this instance, we'll download the selenium chromedriver from https://sites.google.com/a/chromium.org/chromedriver/downloads


Once you've downloaded the chromedriver, add it to your system path. Put it in the same directory where you have your python script:

`DRIVER_PATH = r'path\to\chromedriver.exe'`

`driver = webdriver.Chrome(executable_path=DRIVER_PATH)`

_If you're instrested in browsers other than chrome, please look at the selenium documentation:_ https://www.seleniumhq.org/download/
