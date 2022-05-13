from PyQt5.QtWidgets import QApplication
from msView import *

# This is the main application that sets up a Qt application
# Show our msView window and then let Qt take over

app = QApplication([])
window = msView()
window.show()
sys.exit(app.exec_())