from .subtitle import subfetch
VERSION = '3.0.0'
from .vidsrcme import get as vidsrcmeget
from .vidsrcto import get as vidsrctoget
from .utils import fetch
# UTILS
async def info():
    return {
    "note":"Vidsrc filemoon rest api",
    "version": VERSION,
    "dev":"highrisk"
    }
