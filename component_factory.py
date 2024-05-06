from abc import ABC, abstractmethod
import tkinter as tk


class GUIComponent(ABC):
    @abstractmethod
    def create(self, master, **kwargs):
        pass


class LabelComponent(GUIComponent):
    def create(self, master, text=None, **kwargs):
        return tk.Label(master, text=text, **kwargs)


class EntryComponent(GUIComponent):
    def create(self, master, **kwargs):
        return tk.Entry(master, **kwargs)


class DropdownComponent(GUIComponent):
    def create(self, master, options=None, command=None, **kwargs):
        var = tk.StringVar(master)
        var.set(options[0])  # Set default value
        dropdown = tk.OptionMenu(master, var, *options, command=command)
        dropdown.config(width=10)
        return dropdown


class ButtonComponent(GUIComponent):
    def create(self, master, text=None, command=None, **kwargs):
        return tk.Button(master, text=text, command=command, **kwargs)