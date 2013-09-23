# autogit
`autogit` saves local history automatically using git. It watches current directory, and `git commit` when something changes. `autogit` let you keep local history without IDE.

## Install
`autogit` require `fswatch`. AFAIK, it works only for OS X, so `autogit` supports only OS X.

	brew install fswatch
	pip install autogit
	
## Usage
Go to your project directory. It should have `.git` directory.

	autogit watch

Then it create new branch named `autosave` and commit when git status changes. If you want to stop watching, press `CTRL+C`

You can manually create savepoint.

	autogit savepoint
	
Actually, `autogit watch` is same as this:

	fswatch . "autogit savepoint"

I guess you can do the same using `inotify` in linux.

## Plan
* Portable watch command.
* Easy commands to merge savepoint commits to master branch.