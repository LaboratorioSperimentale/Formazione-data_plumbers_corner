---
title: "Basics of version control and collaborative development with Git"
subtitle: "Data plumbers' corner, session 3"
author: "Arianna Masciolini"
theme: "lucid"
date: "8 November 2024"
institute: "Språkbanken Text, University of Gothenburg"
---

## Today's session
1. Variations on the theme of Alice (bash exercises)
2. Intro to version control and Git
3. Hands-on Git tutorial

## What you will need
- a Unix-like shell 
- the basic Git CLI program
- a GitHub account

## Manual versioning
\bigskip
![](final.png)

## Version Control Systems
1. need to save disk space: __patch-based VCS__ (e.g. RCS)
3. need for collaborative development: __centralized VCSs__ (e.g. SVN)
4. need to work offline and prevent the server from being the "single point of failure": __distributed VCSs__ (e.g. Git, the current _de facto_ standard)

## Behind Git
\bigskip

![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Flinuxreviews.org%2Fimages%2Fthumb%2F9%2F90%2FLinuxCon_Europe_Linus_Torvalds_upperhalf.jpg%2F1800px-LinuxCon_Europe_Linus_Torvalds_upperhalf.jpg&f=1&nofb=1&ipt=05b41b7ad432ef5cf5d9677317a42bcc50b21761e3c7919ec5bc5d7ab2484a29&ipo=images)

\footnotesize \centering Linus Torvalds, the creator of both Linux and Git

## Git: basic concepts
![](xkcd.png)

- (named) filesystem snapshots rather than patches
- version history as a directed graph
- distributed, supports easy branching
- several interfaces and "hubs"

## Hands-on Git tutorial
1. local usage (simple versioning)
2. setting up a remote GitHub repository \newline (versioning + backup)
3. collaborative usage with GitHub