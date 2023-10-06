# Contributing to Awesome Python Scripts

First off, thanks for taking the time to contribute!

All types of contributions are encouraged and valued. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for the maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 🎉


# Steps for Contribution

## 1. Fork this repository
Fork this repository by clicking on the fork button on the top of this page. This will create a copy of this repository in your account.

## 2. Clone the forked repository
In your cloned repository click on the **green code button** and copy the link shown.

Clone your forked repository by running the **git clone** command with you copied link on you command line.

```git clone <url_you_just_copied>```

Do the following command to get into the repository directory:

```cd <your_directory>```

Then create your own branch in the repo using:

```git checkout -b <your_branch_name>```

## 3. Add your changes
You can see what all you changes using the `git status` command.

## 4. Add all you changes 
Add all your changes to you branch using the `git add .` command

## 5. Commit your changes
Commit your changes to your branch using `git commit -m "commit message"` command.

## Commit Message Conventions

- Start with a short summary (50 characters or less) of the changes made.
- Use the present tense and imperative mood.
- Separate the summary from the body of the message with a blank line.
- Use the body to explain what and why changes were made, as well as any necessary details.
- Additionally, you can consider using [semantic commit messages](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716?permalink_comment_id=3867882) like "feat:", "docs:", etc. which will provide additional context to the commit message.

| Commit Type | Description |
| ---- | ---- |
| `feat` | New feature or functionality added |
| `fix` | Bug fix |
| `docs` | Changes to documentation |
| `test` | Adding or updating tests |
| `chore` | Maintenance tasks such as refactoring, dependencies updates, or removing unused code |
| `ci` | Changes to the build or continuous integration process |

## 5. Push you changes to GitHub
Switch to the master branch using this command:

```git checkout master``` 

Push all your changes to GitHub using the command:

```git push --set-upstream origin <your_branch_name>```


