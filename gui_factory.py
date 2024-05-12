from abc import ABC, abstractmethod
import tkinter as tk
from component_factory import GUIComponent, LabelComponent, EntryComponent, DropdownComponent, ButtonComponent


class AbstractFactory(ABC):
    @abstractmethod
    def create_label(self, master, text):
        pass

    @abstractmethod
    def create_entry(self, master):
        pass

    @abstractmethod
    def create_dropdown(self, master, options, command):
        pass

    @abstractmethod
    def create_button(self, master, text, command):
        pass


class GUIFactory(AbstractFactory):
    def create_label(self, master, text):
        return LabelComponent().create(master, text=text)

    def create_entry(self, master):
        return EntryComponent().create(master)

    def create_dropdown(self, master, options, command, variable=None):
        return DropdownComponent().create(master, options=options, command=command, variable=variable)

    def create_button(self, master, text, command):
        return ButtonComponent().create(master, text=text, command=command)