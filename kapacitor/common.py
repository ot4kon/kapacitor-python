from os import path

def join_path(*paths):
  return path.join(*paths).replace("\\", "/")