from module import X as module_X
from importlib import reload
reload(module)  # Python 3 dùng importlib.reload
import module
print(X)
print(module.X)
