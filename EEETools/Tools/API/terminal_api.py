from EEETools.Tools.API.ExcelAPI.modules_importer import calculate_excel, import_excel_input
from EEETools.Tools.GUIElements.connection_and_block_check import CheckConnectionWidget
from EEETools.Tools.GUIElements.net_plot_modules import display_network
from EEETools.MainModules.main_module import CalculationOptions
from tkinter import filedialog
from EEETools import costants
from shutil import copyfile
import tkinter as tk
import os, warnings


def calculate(excel_path="", calculate_on_pf_diagram=True, loss_cost_is_zero=True, valve_is_dissipative=True,
              condenser_is_dissipative=True):

    if excel_path == "":

        root = tk.Tk()
        root.withdraw()
        excel_path = filedialog.askopenfilename()

    if excel_path == "":
        return

    option = CalculationOptions()
    option.calculate_on_pf_diagram = calculate_on_pf_diagram
    option.loss_cost_is_zero = loss_cost_is_zero
    option.valve_is_dissipative = valve_is_dissipative
    option.condenser_is_dissipative = condenser_is_dissipative

    calculate_excel(excel_path, option)


def launch_connection_debug(excel_path=""):

    if excel_path == "":
        root = tk.Tk()
        root.withdraw()
        excel_path = filedialog.askopenfilename()

    if excel_path == "":
        return

    array_handler = import_excel_input(excel_path)
    CheckConnectionWidget.launch(array_handler)


def launch_network_display(excel_path=""):

    if excel_path == "":
        root = tk.Tk()
        root.withdraw()
        excel_path = filedialog.askopenfilename()

    if excel_path == "":
        return

    array_handler = import_excel_input(excel_path)
    display_network(array_handler)


def paste_default_excel_file():
    __import_file("Default Excel Input_eng.xlsm")


def paste_user_manual():
    __import_file("User Guide-eng.pdf")


def paste_components_documentation():
    __import_file("Component Documentation-eng.pdf")


def __import_file(filename):

    root = tk.Tk()
    root.withdraw()

    dir_path = filedialog.askdirectory()

    if dir_path == "":
        return

    file_path = os.path.join(dir_path, filename)
    file_position = os.path.join(costants.RES_DIR, "Other", filename)

    if not os.path.isfile(file_position):

        try:

            from EEETools.Tools.Other.resource_downloader import update_resource_folder
            update_resource_folder()

        except:

            warning_message = "\n\n<----------------- !WARNING! ------------------->\n"
            warning_message += "Unable to save the file to the desired location!\n\n"

            warning_message += "file name:\t\t\t" + filename + "\n"
            warning_message += "file position:\t\t" + file_position + "\n"
            warning_message += "new file position:\t" + file_path + "\n\n"

            warnings.warn(warning_message)

    else:

        try:

            copyfile(file_position, file_path)

        except:

            warning_message = "\n\n<----------------- !WARNING! ------------------->\n"
            warning_message += "Unable to copy the file to the desired location!\n\n"

        else:

            warning_message = "\n\n<----------------- !SUCCESS! ------------------->\n"
            warning_message += "File successfully copied to the desired location!\n\n"

        warning_message += "file name:\t\t\t" + filename + "\n"
        warning_message += "file position:\t" + file_path + "\n\n"

        warnings.warn(warning_message)