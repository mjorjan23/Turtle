"""
This is where the implementation of the plugin code goes.
The testplug-class is imported from both run_plugin.py and run_debug.py
"""
import sys
import logging
from webgme_bindings import PluginBase

# Setup a logger
logger = logging.getLogger('ToPythonFile')
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)  # By default it logs to stderr..
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class ToPythonFile(PluginBase):
  def main(self):
    active_node = self.active_node
    core = self.core
    logger = self.logger
        
    
    
    FCO = None
    turtle_meta = None  
    commands = []
    self.functions = []
    self.loops = []
    turtle_model = None
    starting_point = None
    self.func_count = 0
    self.loop_count = 0
    
    
    #starting point  
    starting_point = self.find_starting_point(core, logger, active_node)
    logger.info( 'starting point is: ' + core.get_attribute(starting_point,'name'))

    #traversing through model
    self.traverse(core, logger, active_node, starting_point, commands)

    
    logger.info(commands)
    logger.info(self.functions)
    
    
    #code generation
    #header
    generated_lines = [
    "import turtle",
    "t = turtle.Turtle()",
     ]
    
    #functions
    func_iter = 0;
    for each_func in self.functions:
      func_iter+=1
      generated_lines.append(f"def function{func_iter}():")
      for f_com in each_func:
        generated_lines.append(f"    {f_com}")
        
    #loops
    loop_iter = 0;
    for each_loop in self.loops:
      loop_iter+=1
      generated_lines.append(f"def loop{loop_iter}():")
      for i, l_com in enumerate(each_loop):
        if i == 0:
          generated_lines.append(f"    for _ in range({l_com}):")
        else:
          generated_lines.append(f"        {l_com}")

    #commands
    for c_com in commands:
      generated_lines.append(c_com)
        
        
        
        
        
    generated_lines.append('turtle.done()')
    code_str = "\n".join(generated_lines)

    # Make file downloadable from WebGME plugin UI
    self.add_file("turtle_art.py", code_str)

         
    
  def traverse(self, core, logger, active_node, current, array):
    while True:
      if core.get_attribute(current, 'name') == 'forward':
        value = core.get_attribute(current, 'value')
        array.append(f"t.forward({value})")
      elif core.get_attribute(current, 'name') == 'left':
        angle = core.get_attribute(current, 'angle')
        array.append(f"t.left({angle})")
      elif core.get_attribute(current, 'name') == 'right':
        angle = core.get_attribute(current, 'angle')
        array.append(f"t.right({angle})")
      elif core.get_attribute(current, 'name') == 'width':
        width = core.get_attribute(current, 'width')
        array.append(f"t.width({width})")
      elif core.get_attribute(current, 'name') == 'color':
        selection = core.get_attribute(current, 'selection')
        array.append(f"t.color('{selection}')")
      elif core.get_attribute(current, 'name') == 'goto':
        x = core.get_attribute(current, 'xCor')
        y = core.get_attribute(current, 'yCor')
        array.append(f"t.goto({x}, {y})")
      elif core.get_attribute(current, 'name') == 'Function':
        self.func_count+=1
        array.append(f"function{self.func_count}()")
      elif core.get_attribute(current, 'name') == 'forLoop':
        self.loop_count+=1
        array.append(f"loop{self.loop_count}()")
      else:
        array.append(f"t.{core.get_attribute(current, 'name').lower()}()")
      
      
      
      
      if core.get_attribute(current, 'name') == 'Function':
        function_start = self.find_starting_point(core, logger, current)
        logger.info(core.get_attribute(function_start, 'name'))
        temp = []
        self.functions.append(temp)
        self.traverse(core, logger, active_node, function_start, temp)
        
      if core.get_attribute(current, 'name') == 'forLoop':
        function_start = self.find_starting_point(core, logger, current)
        logger.info(core.get_attribute(function_start, 'name'))
        temp = []
        self.loops.append(temp)
        temp.append( core.get_attribute( current, 'iterations'))
        self.traverse(core, logger, active_node, function_start, temp)
        
      
      cur_pointer = core.get_pointer_path(current, 'next')
    
      
      #killing current instance of method because no items next
      if not cur_pointer:
        logger.info("There's no next item. Traversing stops")
        break
      #else go to next node  
      next_node = core.load_pointer(current, 'next')
      current = next_node
    
                    
     
    
  def find_starting_point(self, core, logger, parent_node):
    for child in core.load_children(parent_node):
      if core.get_attribute(child, 'start') == 'yes':
        return child
    logger.error(f"No starting point found under node: {core.get_attribute(parent_node, 'name')}")  
    return None

