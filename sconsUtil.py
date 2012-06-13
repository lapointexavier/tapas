import os
import sys
import fnmatch
import string

tryedImportingBuildEnv = False
def importBuildEnvs():
    global tryedImportingBuildEnv
    
    if "buildEnv" not in sys.modules.keys():
        try:
            import buildEnv
            print "* Build: imported buildEnv.py"
        except:
            if tryedImportingBuildEnv == False:
                print "Build: Tried importing buildEnv.py but failed."
                tryedImportingBuildEnv = True

def getEnvVar(varName):
    var = ""
    if varName in os.environ:
        var = os.environ[varName]
    else:
        raise Exception("Could not find env var: " + str(varName))
    
    return var


