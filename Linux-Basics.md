# Linux Basics
Started: December 2025

---

## File & Directory Commands

| Command            | Description                                         |
| ------------------ | --------------------------------------------------- |
| `ls`               | Displays files inside a directory                   |
| `cd`               | Changes current directory                           |
| `cd ~`             | Shortcut to go to home directory                    |
| `cd ..`            | Go back to previous folder                          |
| `mkdir`            | Creates a new directory                             |
| `cp`               | Copies files/directories from source to destination |
| `mv`               | Moves or renames files and directories              |
| `rm`               | Removes files or directories                        |
| `rmdir`            | Removes an empty folder                             |
| `rm foldername -r` | Removes a folder with all its contents              |
| `rm * -r`          | Deletes everything in current directory             |
| `pwd`              | Displays the current directory path                 |

---

## File Reading & Editing

| Command           | Description                                          |
| ----------------- | ---------------------------------------------------- |
| `cat filename`    | Displays contents of a file                          |
| `cat -n filename` | Displays contents with line numbers                  |
| `file filename`   | Shows the file type                                  |
| `nano filename`   | Opens text editor (creates file if it doesn't exist) |
| `vim filename`    | Opens vim text editor                                |

### Vim Shortcuts
- `i` → Enter insert mode (write/delete text)
- `Esc` + `:wq` → Save and quit
- `Esc` + `:q` → Quit without changes
- `Esc` + `:q!` → Quit and discard all changes

---

## Output & Redirection

| Command | Description |
|---|---|
| `echo "text"` | Prints text to terminal |
| `echo "text" > file.txt` | Writes text to file (creates file if not exists, overwrites if exists) |
| `echo "text" >> file.txt` | Appends text to end of file (keeps existing content) |
| `grep "word" file` | Searches for a string inside a file or command output |

---

## System & User Commands

| Command | Description |
|---|---|
| `ps` | Lists currently running processes |
| `su` | Switch to another user / become superuser |
| `sudo` | Run a command as superuser |
| `passwd` | Change password (current user if no params given) |
| `shutdown` | Shuts down / restarts the computer |
| `man command` | Shows documentation for any command |

---

## File Permissions

### chmod — Modify file permissions
```
chmod (who) (action) (permission) filename

who:    u = user | g = group | o = others | a = all
action: + = add  | - = remove | = = set exactly
perm:   r = read | w = write  | x = execute
```
**Example:** `chmod u+x 1.txt` → gives the user execute permission on 1.txt

### chown — Change file ownership
```
sudo chown root filename       # change owner to root
sudo chown :root filename      # change group to root
```
> Note: The user you're changing ownership to must already exist.

---

## Networking Commands

| Command | Description |
|---|---|
| `ifconfig` | Display/configure network card info (deprecated, use `ip a`) |
| `ip a` | Modern replacement for ifconfig |
| `iwconfig` | Display/configure wireless network card info |

---

## Other Useful Commands

| Command | Description |
|---|---|
| `apt-get` | Install, update, remove packages (Debian/Kali) |
| `dd if=input.txt of=output.txt` | Copy contents from one file to another (very fast) |
| `ncal -wM` | Show calendar (-w = weeks, M = start from Monday) |

---

## What I Still Need to Practice
- [ ] Using grep with pipes
- [ ] chmod with numeric values (e.g. chmod 755)
- [ ] Process management (kill, top, htop)
- [ ] SSH basics
- [ ] Package installation with apt-get
