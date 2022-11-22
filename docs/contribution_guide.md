# Contributing Guide

First off, thanks for taking the time to contribute! :rocket:

## The Basics

If you are looking to help with a code contribution, this project uses [MKDocs](https://www.mkdocs.org/) for documentation generation, [Python](https://www.python.org/) for the plugin, along with a splattering of [Markdown](https://www.markdownguide.org/) and [yaml](https://yaml.org/).  I've included my [VSCode](https://code.visualstudio.com/) workspace and a [Docker](https://docs.docker.com/) development container.  Read about [how I develop using VSCode and Docker](https://www.allisonthackston.com/articles/docker-development.html). If you don't feel ready to make autobot code contribution yet, no problem! You can also check out the issues we have in the [Github issue tracker](https://github.com/OSCA-Kampala-Chapter/autobot/issues).

<!-- TODO ---- hassan am looking forward to adding this. I think it maight be helpfull!
If you are interested in making autobot code contribution and would like to learn more about the technologies that this project uses, check out the list below.

* _[bulleted list of resources (tutorials, videos, books) that new contributors
can use to learn what they need to know to contribute to your project]_ i will put them here if provided
-->

### How to Contribute

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

## Getting Help

If you need help, you can ask questions on the [issue tracker](https://github.com/OSCA-Kampala-Chapter/autobot/issues)

<!-- TODO ---- hassan am looking forward to creating the code of conduct as well
## Code of Conduct

Our [Code of Conduct](CODE_OF_CONDUCT.md) means that you are responsible for treating everyone on the project with respect and courtesy regardless of their identity. If you are the victim of any inappropriate behavior or comments as described in our [Code of Conduct](CODE_OF_CONDUCT.md), we are here for you and will do the best to ensure that the abuser is reprimanded appropriately, per our code. 
-->
