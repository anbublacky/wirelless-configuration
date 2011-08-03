#!/usr/bin/env python

# example wireless.py

import pygtk
import gtk

class NotebookExample:

    def delete(self, widget, event=None):
        gtk.main_quit()
        return False

    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.connect("delete_event", self.delete)
        window.set_border_width(10)
	window.set_title("Wireless Configuration")
 	window.set_border_width(10)
        table = gtk.Table(3,6,False)
        window.add(table)
	label=gtk.Label("Connection Name :")
	table.attach(label,0,1,0,1)
	label.show()
	entry=gtk.Entry()
	table.attach(entry,1,2,0,1)
	entry.show()
        # Create a new notebook, place the position of the tabs
        notebook = gtk.Notebook()
        notebook.set_tab_pos(gtk.POS_TOP)
        table.attach(notebook, 0,6,1,2)
        notebook.show()

        # Let's append a bunch of pages to the notebook
        frame = gtk.Frame("wireless")
        frame.set_border_width(10)
        frame.set_size_request(150, 150)
        frame.show()
	table1 = gtk.Table(6,3,True)
	frame.add(table1)
        label = gtk.Label("ssid")
	table1.attach(label,0,1,0,1)
	label.show()
        entry=gtk.Entry()
        table1.attach(entry,1,3,0,1)
        entry.show()
	label = gtk.Label("Bssid")
	table1.attach(label,0,1,2,3)
	label.show()
        entry=gtk.Entry()
        table1.attach(entry,1,3,2,3)
        entry.show()
	label = gtk.Label("mode")
	table1.attach(label,0,1,4,5)
        label.show()
	combobox = gtk.combo_box_new_text()
	combobox.append_text("Infrastructure")
	combobox.append_text("Ad-hoc")
	combobox.set_active(0)
	table1.attach(combobox,1,3,4,6)
	combobox.show()

        label = gtk.Label("Wireless")
        notebook.append_page(frame, label)
      
        frame = gtk.Frame("ipv4-settings")
        frame.set_border_width(10)
        frame.set_size_request(100, 75)
        frame.show()
        table2 = gtk.Table(6,3,True)
        frame.add(table2)

        label = gtk.Label("ip address")
	table2.attach(label,0,1,0,2)
        label.show()
        combobox = gtk.combo_box_new_text()
        combobox.append_text("Automatic Dhcp")
        combobox.append_text("Manual")
	combobox.append_text("Disabled")
        combobox.set_active(0)
        table2.attach(combobox,1,3,0,2)
        combobox.show()

        label = gtk.Label("ipv4-settings")
        notebook.append_page(frame, label)


        # Create a bunch of buttons
        button = gtk.Button("close")
        button.connect("clicked", self.delete)
        table.attach(button, 0,1,2,3)
        button.show()

        table.show()
	table1.show()
	table2.show()
        window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    NotebookExample()
    main()
