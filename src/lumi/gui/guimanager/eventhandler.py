from callbacks.callbacks_routing import ROUTING
from PyQt5.QtCore import pyqtSignal as EVENT

from callbacks.printok_callback import print_ok

from importlib import import_module 

class GUIEventHandler():
    
    def get_gui_object_by_name(self, object_name):
        return getattr(self, object_name)
    
    def get_object_event_attribute_by_name(self,gui_object ,trigger_event):
        return getattr(gui_object, trigger_event)

    def get_module_object_by_path(self, module_path):
        return import_module(module_path)
    
    def get_callback_function_by_module_and_name(self, module, function_name):
        return getattr(module, function_name)

    def split_path_into_module_and_function(self, callback_path):
        """@return : a dict with 'module' and 'function_name' indexes.
           example: callbacks.example_callbacks.first_callback_function
                    {'module': callbacks.example_callbacks,
                    'function_name': first_callback_function}
        """
        return {
            'module': '.'.join(callback_path.split('.')[:-1]),
            'function_name': callback_path.split('.')[-1]
        }


    def route_callbacks_to_objects(self):
        for object_name in ROUTING:
            trigger_event = ROUTING[object_name]['trigger_event']
            callbacks_paths_list = ROUTING[object_name]['callback_functions']

            gui_object = self.get_gui_object_by_name(object_name)
            event = self.get_object_event_attribute_by_name(gui_object, trigger_event)

            path_info = self.split_path_into_module_and_function(callbacks_paths_list[0])
            module = self.get_module_object_by_path(path_info['module'])
            callback_function = self.get_callback_function_by_module_and_name(module, path_info['function_name'])
            
            event.connect(callback_function)