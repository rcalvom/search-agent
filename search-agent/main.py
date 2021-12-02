from drawer.drawer import Drawer
from drawer.models import *
import time

drawer = Drawer()
for i in range(100):
    drawer.draw(status=State())
    time.sleep(1);