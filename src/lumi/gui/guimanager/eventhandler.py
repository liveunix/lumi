from functools import partial

from callbacks.callbacks_routing import ROUTING
from PyQt5.QtCore import pyqtSignal as EVENT

from importlib import import_module 

class GUIEventHandler():
    
    def _get_gui_object_by_name(self, object_name):
        return getattr(self, object_name)
    
    def _get_object_event_attribute_by_name(self,gui_object ,trigger_event):
        return getattr(gui_object, trigger_event)

    def _get_module_object_by_path(self, module_path):
        return import_module(module_path)
    
    def _get_callback_class_by_module_and_name(self, module, function_name):
        return getattr(module, function_name)

    def _split_path_into_module_and_function(self, callback_path):
        """@return : a dict with 'module' and 'class_name' indexes.
           example: callbacks.example_callbacks.callback_class
                    {'module': callbacks.example_callbacks,
                    'class_name': callback_class}
        """
        return {
            'module': '.'.join(callback_path.split('.')[:-1]),
            'class_name': callback_path.split('.')[-1]
        }


    def route_callbacks_to_objects(self):
        for object_name in ROUTING:
            trigger_event = ROUTING[object_name]['trigger_event']
            callbacks_paths_list = ROUTING[object_name]['callback_functions']

            gui_object = self._get_gui_object_by_name(object_name)
            event = self._get_object_event_attribute_by_name(gui_object, trigger_event)

            for callback_class_path in callbacks_paths_list:
                path_info = self._split_path_into_module_and_function(callback_class_path)
                module = self._get_module_object_by_path(path_info['module'])
                callback_class = self._get_callback_class_by_module_and_name(module, path_info['class_name'])

                event.connect(partial(callback_class.init(self)))
