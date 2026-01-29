# Git Commands Documentation

This file documents the basic Git commands used in this assignment, with explanations and sample outputs.

---

## 1. `git init`
**Description:** Initializes a new Git repository in the current directory.

**Command:**
```
git init
```
**Sample Output:**
```
Reinitialized existing Git repository in C:/Tejas/GitDVC/.git/
```

---

## 2. `git status`
**Description:** Shows the current status of the working directory and staging area.

**Command:**
```
git status
```
**Sample Output:**
```
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

---

## 3. `git add <file>`
**Description:** Stages changes for the next commit.

**Command:**
```
git add hello.py
```

---

## 4. `git commit -m "message"`
**Description:** Commits the staged changes with a message.

**Command:**
```
git commit -m "Initial commit"
```
**Sample Output:**
```
[main 9314a70] Initial commit
 1 file changed, 1 insertion(+)
 create mode 100644 hello.py
```

---

## 5. `git log`
**Description:** Shows the commit history.

**Command:**
```
git log --oneline
```
**Sample Output:**
```
9314a70 (HEAD -> main) Initial commit
b367f3c (origin/main) first commit
```

---


## 6. Branching and Merging

### a. `git branch`
**Description:** Lists all local branches in the repository.

**Command:**
```
git branch
```
**Sample Output:**
```
* main
  feature-branch
```

---

### b. `git checkout -b <branch>`
**Description:** Creates a new branch and switches to it.

**Command:**
```
git checkout -b feature-branch
```
**Sample Output:**
```
Switched to a new branch 'feature-branch'
```

---

### c. `git add <file>` and `git commit -m "message"`
**Description:** Stages and commits changes in the new branch.

**Command:**
```
git add hello.py
git commit -m "Feature: add message in feature-branch"
```
**Sample Output:**
```
[feature-branch 9f9d672] Feature: add message in feature-branch
 1 file changed, 1 insertion(+)
```

---

### d. `git checkout main`
**Description:** Switches back to the main branch.

**Command:**
```
git checkout main
```
**Sample Output:**
```
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)
```

---

### e. `git merge <branch>`
**Description:** Merges the specified branch into the current branch.

**Command:**
```
git merge feature-branch
```
**Sample Output:**
```
Updating 9314a70..9f9d672
Fast-forward
 hello.py | 1 +
 1 file changed, 1 insertion(+)
```

---

## 7. Other Useful Commands
- `git push` – Push changes to remote
- `git pull` – Fetch and merge changes

---

*This file was generated as part of the Git and DVC assignment.*
