




import os
from webgme_bindings import PluginBase

class testplug(PluginBase):
    def main(self):

        active_node = self.active_node
        core = self.core
        logger = self.logger
        root_node = self.root_node
        META = self.META
        #self.arrayIt = 2
        new_list = []
        
        input_path = self.get_current_config().get('inputPath', '')

        if not input_path:
            self.logger.error("No input file path provided in config 'inputPath'.")
            print("No input file path provided in config 'inputPath'.")
            return False

        plugin_dir = os.path.dirname(os.path.abspath(__file__))
        abs_input_path = os.path.join(plugin_dir, input_path)

        if not os.path.exists(abs_input_path):
            self.logger.error(f"Input file not found: {abs_input_path}")
            print(f"Input file not found: {abs_input_path}")
            return False

        with open(abs_input_path, 'r') as f:
            self.lines = [line.strip('\n') for line in f]
        #print(self.lines[self.arrayIt])
        print(self.lines)


        new_list = self.lines[2:-1]        
        print(new_list)

        
        smNode = core.create_child(active_node, META['Turtle'])
        self.traverse(smNode, core, META, new_list)
        '''
        s1 = core.create_child(smNode, META['left'])
        core.set_attribute(s1, 'angle', '50')
        core.set_attribute(s1, 'start', 'yes')
        s2 = core.create_child(smNode, META['right'])
        core.set_attribute(s2, 'angle', '-50')
        core.set_pointer(s1,'next',s2)
        '''




        self.util.save(root_node, self.commit_hash, 'master', 'Imported Turtle from file')
        return True


    def traverse( self, parent, core, META, new_list):
        #first = True
        x = []
        for item in new_list:
            if 'goto' in item:
                xCor, yCor = map(int, item[item.find('(')+1 : item.find(')')].split(','))
                temp = core.create_child(parent, META['goto'])
                core.set_attribute(temp, 'xCor', xCor)
                core.set_attribute(temp, 'yCor', yCor)
                x.append(temp)
            elif 'left' in item:
                value = item[item.find('(')+1 : item.find(')')]
                temp = core.create_child(parent, META['left'])
                core.set_attribute(temp, 'angle', value)
                x.append(temp)
            elif 'right' in item:
                value = item[item.find('(')+1 : item.find(')')]
                temp = core.create_child(parent, META['right'])
                core.set_attribute(temp, 'angle', value)
                x.append(temp)
            elif 'forward' in item:
                value = item[item.find('(')+1 : item.find(')')]
                temp = core.create_child(parent, META['forward'])
                core.set_attribute(temp, 'value', value)
                x.append(temp)
            elif 'color' in item:
                col = item[item.find('(')+1 : item.find(')')].strip("'\"")
                temp = core.create_child(parent, META['color'])
                core.set_attribute(temp, 'selection', col)
                x.append(temp)
            elif 'width' in item:
                value = item[item.find('(')+1 : item.find(')')]
                temp = core.create_child(parent, META['width'])
                core.set_attribute(temp, 'width', value)
                x.append(temp)
            elif 'penup' in item:
                x.append(core.create_child(parent, META['penUp']))
            elif 'pendown' in item:
                x.append(core.create_child(parent, META['penDown']))
            elif 'clear' in item:
                x.append(core.create_child(parent, META['clear']))
            else:
                self.logger.error("command not supported")
                continue
        core.set_attribute(x[0], 'start', 'yes')
        print( len(x))
        for i in range(len(x)-1):
            core.set_pointer(x[i],'next',x[i+1])





        


