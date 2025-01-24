---
title: "Basics of version control"
subtitle: "Data plumbers' corner, session 7"
author: "Arianna Masciolini"
theme: "lucid"
date: "24 January 2025"
institute: "Språkbanken Text, University of Gothenburg"
---

## Today's session
1. intro to version control and Git (again)
2. hands-on Git(Hub) tutorial

## What you will need
- a Unix-like shell 
- the basic Git CLI program
- a GitHub account
- (if you use VSCode, I can recommend an extension called Git Graph)

## Manual versioning
\bigskip
\bigskip
![](final.png)

## Version Control Systems
1. need to save disk space: __patch-based VCS__ (e.g. RCS)
3. need for collaborative development: __centralized VCSs__ (e.g. SVN)
4. need to work offline and prevent the server from being the "single point of failure": __distributed VCSs__ (e.g. Git, the current _de facto_ standard)

## Behind Git
\bigskip
\bigskip

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flinuxreviews.org%2Fimages%2Fthumb%2F9%2F90%2FLinuxCon_Europe_Linus_Torvalds_upperhalf.jpg%2F1800px-LinuxCon_Europe_Linus_Torvalds_upperhalf.jpg&f=1&nofb=1&ipt=05b41b7ad432ef5cf5d9677317a42bcc50b21761e3c7919ec5bc5d7ab2484a29&ipo=images)

\vskip -5pt \footnotesize \centering Linus Torvalds, the creator of both Linux and Git

\vskip -7pt \tiny \centering recommended: [\underline{youtube.com/watch?v=4XpnKHJAok8}](youtube.com/watch?v=4XpnKHJAok8)

## Git: basic concepts
![](xkcd.png)

\vskip -10pt \tiny \centering image from [\underline{xkcd.com}](xkcd.com)

- (named) filesystem snapshots rather than patches
- version history as a directed graph
- distributed, supports easy branching
- several interfaces and "hubs"

## Hands-on Git tutorial
1. __local usage__ (simple versioning)
2. __setting up a remote GitHub repository__ \newline (versioning + backup)
3. collaborative usage with GitHub

## Basic commands overview

\small
| __`git` command__ | __meaning__ |
| --- | --- |
| `init` | initialize a new repository in the current folder |
| `status` | see what files have been modified/added/removed |
| `add` | add file to staging area to include it in the next commit |
| `commit` | create a named snapshot |
| `stash` | saves current state on a stack of unfinished changes |
| `log` | see commit history |
| `checkout` | move to a different branch/commit |
| `push` | send changes to a remote repo |
| `pull` | download changes from a remote repo |