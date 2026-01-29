# DVC Commands Documentation

This file documents the basic DVC commands used in this assignment, with explanations and sample outputs.

---

## 1. `dvc init`
**Description:** Initializes DVC in the current repository.

**Command:**
```
dvc init
```
**Sample Output:**
```
Initialized DVC repository.
```

---

## 2. `dvc add <data>`
**Description:** Track data/model files with DVC.

**Command:**
```
dvc add data/data.txt
```
**Sample Output:**
```
To track the changes with git, run:
        git add 'data\.gitignore' 'data\data.txt.dvc'
```

---

## 3. `dvc stage add`
**Description:** Create a DVC stage to run a script using data as dependency and producing an output file.

**Command:**
```
dvc stage add -n print_data -d data/data.txt -o output.txt python hello.py
```

---

## 4. `dvc repro`
**Description:** Reproduce the DVC pipeline, running the stage and generating outputs.

**Command:**
```
dvc repro
```
**Sample Output:**
```
Running stage 'print_data':
> python hello.py
Generating lock file 'dvc.lock'
Updating lock file 'dvc.lock'
To track the changes with git, run:
        git add dvc.lock
```

---

## 5. `dvc status`
**Description:** Check data and pipeline status.

**Command:**
```
dvc status
```
**Sample Output:**
```
Data and pipelines are up to date.
```

---

## 6. `dvc push`
**Description:** Push data and outputs to remote storage.

**Command:**
```
dvc push
```
**Sample Output:**
```
2 files pushed
```

---

## 7. `dvc remote add -d <name> <path>`
**Description:** Add a remote storage location for DVC data.

**Command:**
```
dvc remote add -d myremote /tmp/dvc-storage
```
**Sample Output:**
```
Setting 'myremote' as a default remote.
```

---

## 8. `dvc commit`
**Description:** Save data changes (if needed).

**Command:**
```
dvc commit
```

---

## 9. `dvc metrics show`
**Description:** Show metrics (if defined).

**Command:**
```
dvc metrics show
```

---

## 10. `dvc params show`
**Description:** Show parameters (if defined, command may differ by DVC version).

**Command:**
```
dvc params show
```

---

## 11. `dvc exp run`
**Description:** Run experiments (requires pipeline defined in dvc.yaml).

**Command:**
```
dvc exp run
```
**Sample Output:**
```
ERROR: 'C:\Tejas\GitDVC\dvc.yaml' does not exist
```

---

*This file was generated as part of the Git and DVC assignment.*
