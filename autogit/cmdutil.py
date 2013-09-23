import subprocess

class CommandResult(object):
    def __init__(self, p):
        self.stdout, self.stderr = p.communicate()
        self.exitcode = p.returncode
    
    def __str__(self):
        return self.stdout
        
def run(cmd, pipe=True):
    options = {}
    if pipe:
        options['stdout'] = subprocess.PIPE
        options['stderr'] = subprocess.PIPE
        
    p = subprocess.Popen(cmd, shell=True, **options)
    return CommandResult(p)
