# Git

## Configuring Git

```shell
$ git config --global user.name "Your Name"
$ git config --global user.email "yourname@email.com"
```

## Initializing a repository

The first step is to initialize (or add) git to our repository.

```shell
$ git init

# Add a .gitignore file
```

## Adding a remote

```shell
# Set a new remote
$ git remote add origin https://github.com/user/repo.git

# Verify new remote
$ git remote -v
```