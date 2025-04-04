# Lecture: Running Code on a Remote Server

## Introduction

### Why ?

- *Resource Availability*: Access to powerful hardware (CPU, GPU, memory) that may not be available on local machines.

- *Dedicated Environment*: Isolated environment for running experiments without affecting local setup.

- *Collaboration*: Easier to share and collaborate on projects with team members.

- *Consistency*: Ensures a consistent environment for running experiments, reducing discrepancies due to different local setups.

- *Accessibility*: Ability to access and run code from anywhere, as long as you have an internet connection.

## Connecting to a Remote Server

### SSH (Secure Shell)

SSH (Secure Shell) is a protocol for securely connecting to a remote server.
It provides a secure channel over an unsecured network, allowing you to access the remote server's shell.
Basic SSH Command:

```bash
ssh username@remote_server_address
```
After entering the command, you will be prompted to enter the password for the specified username on the remote server.

For seccury reasons, it is recommended to use SSH keys for authentication.

In order to avoid typing the address every time, you can add an entry to the `~/.ssh/config` file:

```bash
Host myserver
    HostName remote_server_address
    User username
```

Then you can connect to the server using the alias `myserver`.

### Using SSH Keys for Authentication

SSH keys provide a more secure and convenient way to authenticate with a remote server.
It involves generating a pair of cryptographic keys (public and private) and copying the public key to the remote server.
Here's how you can generate SSH keys:

```bash
ssh-keygen -t rsa -b 4096 -C "<your_email>"
```

A secure passphrase can be added to the key pair for additional security.

Once the keys are generated, you can copy the public key to the remote server using the `ssh-copy-id` command:

```bash
ssh-copy-id username@remote_server_address
```

Note: if there are multiple keys, you can specify the key to use with the `-i` flag.

This will add your public key to the `authorized_keys` file on the remote server, allowing you to authenticate without entering a password.


### Forward SSH keys

It is also usesfull to forward the SSH agent to the remote server, so you can use your local SSH keys on the
remote server. This can be done by adding the `-A` flag to the `ssh` command:

```bash
ssh -A username@remote_server_address
```

This is commonly use to access private repositories on GitHub or other services.

## Managing Users and Processes 

Multiple users can connect to a remote server simultaneously, and it's important to know who is logged in and what processes are running.

You can check who is logged in using the `who` command:

```bash
who
```

To see all running processes on the server, you can use the `ps` command:
```bash
ps aux
```

- a: show processes for all users
- u: display the process's user/owner
- x: also show processes not attached to a terminal

You can filter the processes by a specific user using the `grep` command:
```bash
ps aux | grep username
```

You can also use the `top` or `htop` command to monitor the system's resource usage in real-time.

It is also possible to message other users on the server using the `write` command:

```bash
write username
```

After entering this command, you can type your message ended by `Ctrl+D`.

## Transferring Files

Two common methods for transferring files between your local machine and a remote server are `scp` (Secure Copy) and `rsync`.

The `scp` command allows you to securely copy files between a local and a remote machine. Here's how you can use `scp`:

```bash
scp local_file username@remote_server_address:/remote/directory
```

This command will copy `local_file` to the specified directory on the remote server.
To copy files from the remote server to your local machine, you can reverse the order of the arguments:

```bash
scp username@remote_server_address:/remote/file /local/directory
```

## Running Long-Running Processes

When running long-running processes on a remote server, it's important to ensure that they continue running even after you log out.
By default, processes started in a terminal session will be terminated when the session is closed.

There are several ways to run processes in the background and keep them running:
- Using `nohup` command
- Using `screen` or `tmux` terminal multiplexers

### Using nohup

`nohup` is a command that runs another command and keeps it running even after you log out.
It is useful for running long-running processes that should continue running in the background.

The basic syntax for using `nohup` is:

```bash
nohup your_command &
```

This will run `your_command` in the background and keep it running even if you disconnect from the remote server.

To check the output of the command, you can redirect it to a file:

```bash
nohup your_command > output.log &
```

Logs can be checked later by opening the `output.log` file.
For example:

```bash
tail -f output.log
```

To stop a process started with `nohup`, you can find its process ID (PID) using the `ps` command and then use the `kill` command to terminate it.
For example:

```bash
ps aux | grep your_command
kill -9 <PID>
```


## Remote connect with VSCode

You can also use Visual Studio Code to connect to a remote server and edit files directly on the server.
This can be done by installing the Remote - SSH extension in VSCode and connecting to the remote server using the SSH command.

Once connected, you can edit files on the remote server as if they were on your local machine.

