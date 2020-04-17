# GUI Programming (Tkinter) :

Python provides various options for developing graphical user interfaces(GUIs).
Tkinter: Tkinter is the Python interface to the Tk GUI toolkit shipped with Python.

wxPython: This is open-source Python interface for wxWidgets GUI toolkit.

PyQt: This is also a Python interface for a popular cross-platform Qt GUI library.

JPython: JPython is a Python port for Java which gives Python scripts seamless access to
    Java class libraries on the local machine http://www.jpython.org

Creating a GUI application using Tkinter is an easy task:

   1. Import the Tkinter module.
   2. Creating The GUI application main window
   3. Add one or more of the above-mentioned widgets to the GUI application.
   4. Enter the maim event loop to take action against each event triggered
      by the usage of PyQt.

# Geometry Management:
All Tkinter widgets have access to specific geomerty management methods. Which have
    the purpose of organizing widgets throughout the parent widget area.

Tkinter exposes the following geometry manager classes: pack, grid, and place.

The pack() Method - This geometry manager organizes widgets in blocks before
    placing them in the parent widget.

The grid() Method - This geometry manager organizes widgets in a table-like
    structure in the parent widget.

The place() Method - This geometry manager organizes widgets by
    placing them in a specific position in the parent widget.