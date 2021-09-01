from mainwindow import Ui_MainWindow
from simulation import Ui_Simulation
from router_list import Ui_Router
from PyQt5 import QtWidgets

from Router import RouterList
from IPv4 import IPv4

path = 'Router list.csv'

destination_addr_list = [
    '128.96.39.10',
    '128.96.40.12',
    '128.96.40.151',
    '192.4.153.17',
    '192.4.153.90'
]


if __name__ == "__main__":
    import sys

    router_list = RouterList(path)
    IPv4 = [IPv4(i) for i in destination_addr_list]
    my_next_step_list = [router_list.match_network(ipv4) for ipv4 in IPv4]
    print(my_next_step_list)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    main_ui = Ui_MainWindow()
    main_ui.setupUi(MainWindow)

    Router_Dialog = QtWidgets.QDialog()
    router_ui = Ui_Router(router_list)
    router_ui.setupUi(Router_Dialog)

    Simulation_Dialog = QtWidgets.QDialog()
    simulation_ui = Ui_Simulation(router_list, IPv4)
    simulation_ui.setupUi(Simulation_Dialog)

    main_ui.router_button.clicked.connect(Router_Dialog.show)
    main_ui.simulation_button.clicked.connect(Simulation_Dialog.show)

    MainWindow.show()
    sys.exit(app.exec_())