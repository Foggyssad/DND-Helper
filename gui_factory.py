from abc import ABC, abstractmethod
import tkinter as tk


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
        return tk.Label(master, text=text)

    def create_entry(self, master):
        return tk.Entry(master)

    def create_dropdown(self, master, options, command):
        var = tk.StringVar(master)
        var.set(options[0])  # Set default value
        dropdown = tk.OptionMenu(master, var, *options, command=command)
        dropdown.config(width=10)
        return dropdown

    def create_button(self, master, text, command):
        return tk.Button(master, text=text, command=command)