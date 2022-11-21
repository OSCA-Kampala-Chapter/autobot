# autobot
![autobot-logo](./res/autobot.png)

Autobot is a bot library targetted to build software bots for various platforms with ease of integration in mind.
project still under active construction, so there's no proper documentation or support information to help that much. 
To contribute to the project, please follow along with the issues being posted and also the discussions.

# **Contributing Guide**

First off, thanks for taking the time to contribute! :rocket:

## **The Basics**

If you are looking to help with a code contribution, this project uses [MKDocs](https://www.mkdocs.org/) for documentation generation, [Python](https://www.python.org/) for the writing the project code along with a splattering of [Markdown](https://www.markdownguide.org/) and [yaml](https://yaml.org/).  I've included our [VSCode](https://code.visualstudio.com/) workspace.  Read about [how I develop using VSCode](https://www.allisonthackston.com/articles/docker-development.html). If you don't feel ready to make autobot code contribution yet, no problem! You can also check out the issues we have in the [Github issue tracker](https://github.com/OSCA-Kampala-Chapter/autobot/issues)

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

## **Pull Request Instructions**
Please, go through these steps before you submit a pull request (PR).

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