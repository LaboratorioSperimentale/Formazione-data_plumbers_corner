# Basics of version control

## Intro to versioning

> Slides

### Historical notes/stages
1. need to save different versions of the same files: "manual" versioning (creating copies of different files, possibly with timestamps)
2. need to save disk space: patch-based Version Control Systems (e.g. RCS)
3. need to collaborate: Centralized VCSs (e.g. CVS and subversion)
4. need to avoid server as a single point of failure: Distributed VCS ($\to$ Git, the current _de facto_ standard: motivation and context)

### Git: basic concepts
- (named) filesystem snapshots rather than patches
- history as a directed graph (show graph of this repository)
- distributed
- several servers/"hubs" and clients (but we will use GitHub and the Git CLI today)

## Hands-on part

> Prerequisites: 
> - a Unix-like shell with the basic Git CLI installed
> - a GitHub account

### Local usage (pure versioning)
- `git init`
- `git status` (+ concept of _modified file_)
- `git add` (+ concept of _staged file_)
- `git commit` (+ concept of _committed file_)
- (`git stash`)
- `git log`/Graph
- if there is time: create and checkout a new branch
- bonus: .gitignores

### Remote usage with GitHub (as a simple backup)
- importing your repository in GitHub
- `git push` (+ authentication yay)
- `git pull`
