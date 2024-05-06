from update_components import Update
from gui_factory import GUIFactory
from windows_creation import FirstWindow, SecondWindow, ThirdWindow
from events import EventHandler
from utils import Utils
from tie_comp_events import Tie
from gui_manager import GUIManager


class Controller:

    def __init__(self, master):
        self.master = master
        self.master.title("Character Builder")
        self.factory = GUIFactory()
        self.labels = {}
        self.entries = {}
        self.gui_manager = GUIManager()
        self.utils = Utils(self.master, self.gui_manager)
        self.first_window = FirstWindow(self.master, self.utils, self.gui_manager)
        self.second_window = SecondWindow(self.master, self.utils, self.gui_manager)
        self.third_window = ThirdWindow(self.master, self.utils, self.gui_manager)
        self.tie = Tie(self.second_window, self.third_window, self.gui_manager)
        self.event_handler = EventHandler(self.master, self.first_window, self.second_window, self.third_window, self.gui_manager)
        self.update = Update(self.master, self.gui_manager)

    def create_first_window(self):
        print("create_first_window method called")
        self.first_window.create_window()