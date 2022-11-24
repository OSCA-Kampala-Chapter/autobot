# **Contributing Guidelines**
## **Befor Contributing**

Welcome to [Autobot!](https://github.com/OSCA-Kampala-Chapter/autobot) Before sending your pull requests, make sure that you **read the whole guidelines.** If you have any doubt on the contributing guide, please feel free to [state it clearly in an issue](https://github.com/OSCA-Kampala-Chapter/autobot/issues) or ask the community in [Discord](/docs/404.md) 

## **Contributing**
### **Contributor**
We are very happy that you are considering implementing autobot for others! Being one of our contributors on this repository, you agree and confirm
-   You did your work - no plagiarism allowed
    -    Any plagiarized work will not be merged.
-   Your work will be distributed under [MIT](/LICENSE) License once your pull request is merged
-   Your submitted work fulfills mostly our styles and standards

**New implementation** is welcome! For example, new solutions for a problem, implementation of an existing implementation is not allowed. Please check whether the solution is already implemented before submitting your pull request.

Improving comments and writing proper tests are also highly welcome.

### **What is autobot?**
Autobot is a bot library targetted to build software bots for various platforms with ease of integration in mind.
project still under active construction, so there's no proper documentation or support information to help that much. 
To contribute to the project, please follow along with the issues being posted and also the discussions.

### **What does autobot do?**
This Bot is a programme that behaves like a normal chat partner with additional functions. It performs predefined tasks independently and without the user’s involvement. The term bot is derived from the term for robot.

Autobot can basically do everything a human chat partner does. Automatically or on request, it can send you the following information:

-   Text messages
-   Images
-   Videos
-   Files of any other kind

### **What makes it special?**
An important function of autobot is the possibility to execute commands in a Telegram chat, which then directly trigger actions or request information. For example, it is possible to send the bot the command `“/help”` or `“/help”`, which then outputs the commands possible for this bot in the chat as text feedback. This could be the following command list:

-   /status
-   /temperature
-   /last alarm
-   /stop

#### Coding Style

We want your work to be readable by others; therefore, we encourage you to note the following:

- Please write in Python 3.11+. For instance:  `print()` is a function in Python 3 so `print "Hello"` will *not* work but `print("Hello")` will.
- Please focus hard on the naming of functions, classes, and variables.  Help your reader by using __descriptive names__ that can help you to remove redundant comments.
  - Single letter variable names are *old school* so please avoid them unless their life only spans a few lines.
  - Expand acronyms because `gcd()` is hard to understand but `greatest_common_divisor()` is not.
  - Please follow the [Python Naming Conventions](https://pep8.org/#prescriptive-naming-conventions) so variable_names and function_names should be lower_case, CONSTANTS in UPPERCASE, ClassNames should be CamelCase, etc.

- We encourage the use of Python [f-strings](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python) where they make the code easier to read.

- Original code submission require docstrings or comments to describe your work.

- More on docstrings and comments:

  If you used a Wikipedia article or some other source material to create your algorithm, please add the URL in a docstring or comment to help your reader.

  The following are considered to be bad and may be requested to be improved:

  ```python
  x = x + 2	# increased by 2
  ```

  This is too trivial. Comments are expected to be explanatory. For comments, you can write them above, on or below a line of code, as long as you are consistent within the same piece of code.

  We encourage you to put docstrings inside your functions but please pay attention to the indentation of docstrings. The following is a good example:

  ```python
  def sum_ab(a, b):
      """
      Return the sum of two integers a and b.
      """
      return a + b
  ```

### **How to Contribute**

Never made an open-source contribution before? Wondering how contributions work in this project? Here's a quick rundown!

1. Find an issue that you are interested in addressing or a feature that you would like to add in the [issue tracker](https://github.com/OSCA-Kampala-Chapter/autobot/issues).  Don't see your issue?  Submit one!

2. Fork the repository associated with the issue to your local GitHub account. This means that you will have a copy of the repository under your-GitHub-username/repository-name.

3. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/OSCA-Kampala-Chapter/autobot
    ```

4. Create a new branch for your fix.

    ```bash
    git checkout -b branch-(name-here)
    ```

5. Make the appropriate changes for the issue you are trying to address or the feature that you want to add.

6. Add the file contents of the changed files to the "snapshot" git uses to manage the state of the project, also known as the index.

    ```bash
    git add <file_list>
    ```

7. Insert a short message of the changes made to store the contents of the index with a descriptive message.

    ```bash
    git commit -m "Insert a short message of the changes made here"
    ```

8. Push the changes to the remote repository

    ```bash
    git push origin branch-name-here.
    ```

9. Submit a pull request to the upstream repository.

10. Title the pull request with a short description of the changes made and the issue or bug number associated with your change. For example, you can title an issue like so "Added more log outputting to resolve #105".

11. In the description of the pull request, explain the changes that you made, any issues you think exist with the pull request you made, and any questions you have for the maintainer. It's OK if your pull request is not perfect (no pull request is), the reviewer will be able to help you fix any problems and improve it!

12. Wait for the pull request to be reviewed by a maintainer.

13. Make changes to the pull request if the reviewing maintainer recommends them.

14. Celebrate your success after your pull request is merged!

15. Most importantly,
  - __Be consistent in the use of these guidelines when submitting.__
  - __now!__
  - Happy coding!

#### Other Requirements for Submissions
- The file extension for code files should be `.py`. 
- Strictly use snake_case (underscore_separated) in your file_name, as it will be easy to parse in future using scripts.
- Please avoid creating new directories if at all possible. Try to fit your work into the existing directory structure.
- If possible, follow the standard *within* the folder you are submitting to.
- If you have modified/added code work, make sure the code compiles before submitting.
- If you have modified/added documentation work, ensure your language is concise and contains no grammar errors.
- Do not update the README.md or DIRECTORY.md file which will be periodically autogenerated by our GitHub Actions processes/MAintainers.
## **Pull Request Instructions**
Please, go through these steps before you submit a PR.

1. Make sure that your PR is not a duplicate.
2. If not, then make sure that:

    a. You have done your changes in a separate branch. Branches MUST have descriptive names that start with either the `fix/` or `feature/` prefixes. Good examples are: `fix/signin-issue` or `feature/issue-templates`.

    b. You have a descriptive commit message with a short title (first line).

    c. You have only one commit (if not, squash them into one commit).

    d. `npm test` doesn't throw any error. If it does, fix them first and amend your commit (`git commit --amend`).

3. **After** these steps, you're ready to open a pull request.

    a. Your pull request MUST NOT target the `master` branch on this repository. You probably want to target `staging` instead.

    b. Give a descriptive title to your PR.

    c. Describe your changes.

    d. Put `closes #XXXX` in your comment to auto-close the issue that your PR fixes (if such).

IMPORTANT: Please review the [contribution-guide](contribution_guide.md) file for detailed contributing guidelines.

## **Getting Help**

If you need help, you can ask questions on the [issue tracker](https://github.com/OSCA-Kampala-Chapter/autobot/issues)