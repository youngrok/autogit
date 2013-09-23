from autogit.cmdutil import run

def watch():
    print 'watching... if you want to stop watching, press CTRL+C'
    savepoint()
    run('fswatch . "autogit savepoint"', pipe=False)
    
def savepoint():
    if not 'autosave' in run('git branch').stdout:
        print 'create branch `autosave`'
        run('git branch autosave')
    
    run('git checkout autosave')
    if run('git status --porcelain').stdout:
        run('git add .')
        print run('git commit -m "autosave"')
    