# Operating System Fundamentals

## Quick Note
Sorry to all my windows friends, but for now I will be skipping some of this part because:
- I am not a windows user.
- I am speedrunning making those notes.
- If I need to do windows attacks or anything like that later I can google the commands I need.
That's why for now do not expect a cover up of neither the CMD (command prompt), nor the windows power shell.
Feel free to do this research on your own, things you'll probably need to know:
1. The windows task manager
2. The windows command prompt
3. The windows power shell
4. Windows privilege and permissions
5. Windows Defender
6. Firewall usage and making exceptions
> This is a list that I made without looking into the things that you will actually need so keep in mind that this list might be missing some stuff.

## Linux

### What is Linux?

**Linux** is an open-source **operating system kernel** — the core program that interacts directly with your computer's hardware. But when most people say _Linux_, they’re actually referring to **Linux-based operating systems** (called **distributions** or **distros**) like:

- Ubuntu
    
- Fedora
    
- Arch Linux
    
- Debian
    
- Kali Linux
    

Each distro bundles the Linux kernel with tools, utilities, a shell (like `bash` or `zsh`), a package manager, and sometimes a graphical interface.

---

### Myth: “Linux Commands”

There is no such thing as _"Linux commands"_ in the sense that the commands you run aren't built into "Linux" itself.

When you open a terminal and type a command, you're actually doing one of the following:

#### 1. Running an external **tool**

These are programs installed on your system, found in places like `/bin`, `/usr/bin`, etc.

Examples:

```bash
ls      # list directory contents (external tool)
cp      # copy files (external tool)
mv      # move/rename files (external tool)
```

#### 2. Using a **shell built-in**

Some commands are built into the **shell** you're using (e.g., `bash`, `zsh`).

Examples:

```bash
cd      # change directory (built into the shell)
echo    # display text (also often a shell built-in)
```

#### 3. Using **kernel syscalls** indirectly

The Linux **kernel** manages things like filesystems, processes, and memory. The commands you run interact _with the kernel_ through tools or shell commands.

---

### Change of Perspective

So when people say "learning Linux commands", what they’re really learning is:

- How to use **tools** available in a Linux environment
    
- How to **navigate the filesystem** using a shell
    
- How to **combine tools** to accomplish tasks efficiently
    

---

### Introduction to Linux Navigation and File Creation

You interact with your Linux system using the **terminal**, a text interface that lets you issue commands.

#### Navigating the Filesystem

Think of Linux’s filesystem like a tree:
```
/
├── home/
│   └── you/
├── etc/
├── bin/
├── var/

```

The root of the filesystem is `/`. All files and folders are underneath this root.

#### Common Navigation Commands

|Command|Purpose|
|---|---|
|`pwd`|Print current directory|
|`cd`|Change directory|
|`ls`|List contents of a directory|
|`ls -l`|Long listing with permissions and sizes|
|`ls -a`|Show hidden files (start with `.`)|

Examples:

```bash
cd /home/you        # Go to your home folder
cd ..               # Go one directory up
ls -la              # List all files in long format
```
---

#### File and Directory Creation

##### Create Directories
```bash
mkdir new_folder
mkdir -p folder/subfolder  # create nested folders

```
##### Create Files
```bash
touch file.txt             # create empty file
echo "Hello" > file.txt    # create file with content
vim file.txt              # open file in text editor
```

##### Copy, Move, Delete
```bash
cp source.txt dest.txt     # copy file
mv file.txt folder/        # move file
rm file.txt                # delete file
rm -r folder/              # delete folder recursively
```

---

#### Bonus: Understanding Paths

- **Absolute Path**: starts from root `/`
	`/home/you/documents/file.txt`
    
- **Relative Path**: from your current directory
```bash
./file.txt     # file in current directory
../file.txt    # file one level up

```
    

---

### Wrap-Up

Learning Linux is not about memorizing magical “Linux commands.” It’s about understanding the **tools**, **shell**, and **kernel** interactions — and how to combine them effectively.

You’re learning how to talk to your machine like a pro

## Tasks
[[OS Tasks]]