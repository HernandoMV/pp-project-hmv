# These are conventions that would be accessible like this:
# print(pp_project_hmv.__author__)
__author__ = 'Hernando M. Vergara'
__version__ = '0.0.1'
__license__ = 'whatever'

print('I am being initiated, thank you... hehehe')

# here I could import stuff from the inner modules so that 
# they are importable directly from pp_project_hmv
# let's say 'stuff' is inside module A, I can add this here
# from .moduleA import stuff
# then I can do from within another repo that uses this:
# from pp_project_hmv import stuff

