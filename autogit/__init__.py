from autogit.cmdutil import run

def watch():
    run('fswatch . "autogit savepoint"')
    
def savepoint():
    if not 'autosave' in run('git branch').stdout:
        run('git branch autosave')
    
    run('git checkout autosave')
    run('git diff --exit-code').exitcode
    if run('git diff --exit-code').exitcode:
        print run('git commit -a -m "autosave"')
    