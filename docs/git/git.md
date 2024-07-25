# Git

- [Git](#git)
  - [Git Initialization](#git-initialization)
    - [Configuring Git](#configuring-git)
    - [Initializing a repository](#initializing-a-repository)
    - [Adding a remote](#adding-a-remote)
    - [Changing the remote](#changing-the-remote)
  - [Commiting changes](#commiting-changes)
    - [Commit \& Push](#commit--push)
  - [Branches](#branches)
    - [Show branches](#show-branches)
    - [Merging a branch](#merging-a-branch)
    - [Deleting a local branch](#deleting-a-local-branch)

## Git Initialization

### Configuring Git

```shell
$ git config --global user.name "Your Name"
$ git config --global user.email "yourname@email.com"
```

### Initializing a repository

The first step is to initialize (or add) git to our repository.

```shell
$ git init

# Add a .gitignore file
```

### Adding a remote

```shell
# Set a new remote
$ git remote add origin https://github.com/user/repo.git

# Verify new remote
$ git remote -v
```

### Changing the remote

```shell
$ git remote set-url origin https://github.com/user/repo2.git
$ git remote -v
```

## Commiting changes

### Commit & Push

```shell
# Show changes
$ git show

$ git add .
$ git ls-files
$ git commit -m "whatever comment"
$ git push origin master
```

## Branches

### Show branches

```shell
# Show branches
$ git branch

# Show current branch
$ git branch --show-current
```

### Merging a branch

```shell
# Checkout and create new local branch from current branch
$ git checkout -b [branchName]

# Return to master branch
$ git checkout master

# Merge branch to master
$ git merge [branchName]
```

### Deleting a local branch

```shell
$ git branch -d <local-branch>

# Forcing
$ git branch -D <local-branch>
```

