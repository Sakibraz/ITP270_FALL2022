####Basic Git Workflow



####Git Workflow
#1.	Fetch and merge changes from the remote.
#2.	Create a branch to work on a new project feature.
#3.	Develop the feature on your branch and commit your work.
#4.	Fetch and merge from the remote again (in case new commits were made while you were working).
#5.	Push your branch up to the remote for review.



####Git Terms
#1.	Working Directory: A working directory where you’ll be doing all the work: creating, editing, deleting, and organizing files.
#2.	Staging Area: A staging area where you’ll list changes you make to the working directory.
#3.	Repository: A repository is where Git permanently stores those changes as different versions of the project.
#4.	A remote is a Git repository that lives outside your Git project folder. Remotes can live on the web, on a shared network or even in a separate folder on your local computer.
#5.	The Git Collaborative Workflow are steps that enable smooth project development when multiple collaborators are working on the same Git project.



####Git Commands
##SETUP: CONFIGURING USER INFORMATION USED ACROSS ALL LOCAL REPOSITORIES
#1.	git config --global user.name “[firstname lastname]”
#  a.	set a name that is identifiable for credit when review version history

#2.	git config --global user.email “[valid-email]”
#  a.	set an email address that will be associated with each history marker

#3.	git config --global color.ui auto
#  a.	set automatic command line coloring for Git for easy reviewing

##SETUP & INIT: CONFIGURING USER INFORMATION, INITIALIZING AND CLONING REPOSITORIES
#4.	git init
#  a.	initialize an existing directory as a Git repository

#5.	git clone [url]
#  a.	retrieve an entire repository from a hosted location via URL

##STAGE & SNAPSHOT: WORKING WITH SNAPSHOTS AND THE GIT STAGING AREA
#6.	git status
#  a.	show modified files in working directory, staged for your next commit

#7.	git add [file]
#  a.	add a file as it looks now to your next commit (stage)

#8.	git reset [file]
#  a.	unstage a file while retaining the changes in working directory

#9.	git diff
#  a.	diff of what is changed but not staged

#10.	git diff –staged
#  a.	diff of what is staged but not yet committed

#11.	git commit -m “[descriptive message]”
#  a.	commit your staged content as a new commit snapshot

##BRANCH & MERGE: ISOLATING WORK IN BRANCHES, CHANGING CONTEXT, AND INTEGRATING CHANGES
#12.	git branch
#  a.	list your branches. a * will appear next to the currently active branch

#13.	git branch [branch-name]
#  a.	create a new branch at the current commit

#14.	git checkout
#  a.	switch to another branch and check it out into your working directory

#15.	git merge [branch]
#  a.	merge the specified branch’s history into the current one

#16.	git log
#  a.	show all commits in the current branch’s history

##INSPECT & COMPARE: EXAMINING LOGS, DIFFS AND OBJECT INFORMATION
#17.	git log
#  a.	show the commit history for the currently active branch

#18.	git log branchB..branchA
#  a.	show the commits on branchA that are not on branchB

#19.	git log --follow [file]
#  a.	show the commits that changed file, even across renames

#20.	git diff branchB...branchA
#  a.	show the diff of what is in branchA that is not in branchB

#21.	git show [SHA]
#  a.	show any object in Git in human-readable format

##TRACKING PATH CHANGES: VERSIONING FILE REMOVES AND PATH CHANGES
#22.	git rm [file]
#  a.	delete the file from project and stage the removal for commit

#23.	git mv [existing-path] [new-path]
#  a.	change an existing file path and stage the move

#24.	git log --stat -M
#  a.	show all commit logs with indication of any paths that moved

##IGNORING PATTERNS: PREVENTING UNINTENTIONAL STAGING OR COMMITING OF FILES
#25.	logs/
#*.notes
#pattern*/
#  a.	Save a file with desired patterns as .gitignore with either direct string matches or wildcard globs

#26.	git config --global core.excludesfile [file]
#  a.	system wide ignore pattern for all local repositories

##SHARE & UPDATE: RETRIEVING UPDATES FROM ANOTHER REPOSITORY AND UPDATING LOCAL REPOS
#27.	git remote add [alias] [url]
#  a.	add a git URL as an alias

#28.	git fetch [alias]
#  a.	fetch down all the branches from that Git remote

#29.	git merge [alias]/[branch]
#  a.	merge a remote branch into your current branch to bring it up to date

#30.	git push [alias] [branch]
#  a.	Transmit local branch commits to the remote repository branch

#31.	git pull
#  a.	fetch and merge any commits from the tracking remote branch

##REWRITE HISTORY: REWRITING BRANCHES, UPDATING COMMITS AND CLEARING HISTORY
#32.	git rebase [branch]
#  a.	apply any commits of current branch ahead of specified one

#33.	git reset --hard [commit]
#  a.	clear staging area, rewrite working tree from specified commit

##TEMPORARY COMMITS: TEMPORARILY STORE MODIFIED, TRACKED FILES IN ORDER TO CHANGE BRANCHES
#34.	git stash
#  a.	Save modified and staged changes

#35.	git stash list
#  a.	list stack-order of stashed file changes

#36.	git stash pop
#  a.	write working from top of stash stack

#37.	git stash drop
#  a.	discard the changes from top of stash stack