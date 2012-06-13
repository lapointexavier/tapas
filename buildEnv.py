# buildEnv.py
import os

os.environ["TAPAS_PYTHON_INCLUDES_PATH"] = "/usr/include/python2.7"
os.environ["TAPAS_PYTHON_LIB"] = "python2.7"
os.environ["TAPAS_PYTHON_LIBS_PATH"] = "/usr/lib/python2.7"

os.environ["TAPAS_BOOST_INCLUDES_PATH"] = "/usr/include/boost"
os.environ["TAPAS_BOOST_LIBS_PATH"] = "/usr/lib"
os.environ["TAPAS_BOOST_PYTHON_LIB"] = "boost_python"

