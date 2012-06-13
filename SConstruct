import sys
import os
import platform
import sconsUtil

sconsUtil.importBuildEnvs()

env = Environment(
  CPPPATH =
  [
    sconsUtil.getEnvVar("TAPAS_PYTHON_INCLUDES_PATH"), 
    sconsUtil.getEnvVar("TAPAS_BOOST_INCLUDES_PATH")
  ],
  LIBS = 
  [
    sconsUtil.getEnvVar("TAPAS_PYTHON_LIB"), 
    sconsUtil.getEnvVar("TAPAS_BOOST_PYTHON_LIB"),
  ],
  LIBPATH =
  [
    sconsUtil.getEnvVar("TAPAS_PYTHON_LIBS_PATH"), 
    sconsUtil.getEnvVar("TAPAS_BOOST_LIBS_PATH")
  ],
  TARGET_ARCH = platform.machine()
)

cppFiles = Split("""
	pythonWrappers/tapasWrapper.cpp
	""")


target = env.SharedLibrary(
			target = "build/tapas", source = cppFiles,
			LIBPREFIX = "")

print "SCons Starting building Shared Library :", target[0]

Return("target")

