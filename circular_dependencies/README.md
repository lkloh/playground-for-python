
# Not working

running `python alice.py` gives an error `ImportError: cannot import name bobby` due to circular dependencies.

# Working

running `python alice.py` will compile when the import is placed INSIDE the function