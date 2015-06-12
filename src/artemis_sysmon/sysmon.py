#!/usr/bin/env python
import os
import rospy
import argparse
from qt_gui.plugin import Plugin
from .sysmon_widget import SysmonWidget

class Sysmon(Plugin):
  """
  Subclass of Plugin to display SLAM status
  """
  def __init__(self, context):
    
    # Init Plugin
    super(Sysmon, self).__init__(context)
    self.setObjectName('SysmonPlugin')

    # Create QWidget
    self._widget = SysmonWidget()
    
    # Show _widget.windowTitle on left-top of each plugin (when 
    # it's set in _widget). This is useful when you open multiple 
    # plugins at once. Also if you open multiple instances of your 
    # plugin at once, these lines add number to make it easy to 
    # tell from pane to pane.
    if context.serial_number() > 1:
        self._widget.setWindowTitle(self._widget.windowTitle() + (' (%d)' % context.serial_number()))
    
    # Add widget to the user interface
    context.add_widget(self._widget)
