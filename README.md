Turtle Graphics MiniProject 
This project allows the end user to compose a turtle graphics model, and it also contains 3 plugins to generate models, python code, or SVG images

#Installation
First, install the Turtle following:
- [NodeJS](https://nodejs.org/en/) (LTS recommended)
- [MongoDB](https://www.mongodb.com/)
- Second, start mongodb locally by running the `mongod` executable in your mongodb installation (you may need to create a `data` directory or set `--dbpath`).
- Open a second terminal and run: node app.js
- Then, run `webgme start` from the project root to start . Finally, navigate to `http://localhost:8888` to start using Turtle!

#WebGME composition.
To compose a model for your turtle graphics:
1. Load the WebGME project. The root will be inclusize of the FCO and the turtleMETA.
2. To begin, create a Turle entity within root. 

#Building your composition
1. You can drag and drop different Commands,Functions and For loops. 
2. Each node will have an attribute named "start". It is set to "no" as default. The attribute is used to identify the starting position. One will need to change the attribute to "yes" for this first item in their model, so the system knows where to begin. Whenever one enters a function or forLoop, the "start" should also be selected so the program knows where to begin within the function/loop as well. Please make sure there is only one starting point per overall model and per function/loop.
3. To connect a node, utilize the "next" within the pointer tab. Select the appropriate node to point to. The last node of your model(or within a function/loop) must point to NULL.
4. The list of commands are: forward, left, right, penUp, penDown, width, color, clear, goto, forLoop, and Function. 
5. Functions/ForLoops:
	a. Make sure a Function/ForLoop itself points to the next command/Function/ForLoop after exiting the function. (The last command within a Function/ForLoop points to NULL)
	b. Nested Functions and ForLoops are allowed in this model
	c. Within a Function/ForLoop, a single starting point MUST be selected
6. When using forward, left, right, width, color, and goto. Attributes can be selected to determine the value. 
	a. Forward will have an integer value(can be negative if going backwards)
	b. Left and right will have an integer angle value
	c. Width will have an integer value for thickness
	d. Goto will have an x-value(xCor) and y-value(yCor) as coordinates  
	e. Color will offer a drop down on available colors(red, orange, yellow, green, blue, purple, black, white)
	
#Plugins
-There are 3 PlugIns Available for usage 
1. ToPythonFile
	- this plugin will take an existing model and create a python file 
	- Click in any turtle and run the plugin. 
	- A file "turtle_art.py" will be generated 
	- Download the plugin and run from any Python3 interpreter so visualize a picture
2. PythonToSVG
	- this plugin will take an existing model and create a SVG file 
	- Click in any turtle and run the plugin. 
	- A file "turtle_SVG.py" will be generated 
	- Download the plugin and run from any Python3 interpreter to generate a "image_file.svg" that will be saved in the directory
	- The SVG file can be opened with any web based client
3. ImportPython
	- this plugin should be run from the root
	- it will take any .py turgle graphics file and produce a composition model
	- any complex commands that are unknown will result in a error warning within the console
	- after a model is created, the user can access it on the composition pane within webgme

#Visuals
1. each command/function/loop will have nodes with pictures to help the user have a better identification.
2. the visuals are static, but the nodes will contain attributes within their name

#Notes
1. Recursion-safe
2. Function calls are numbered in the order they are encountered
3. Model must include starting points for:
	a. overall model  
	b. each function

#Assignment8 sample code 
- I have 2 turtles within webgme that can be used to run the plugins: ToPythonFile and PythonToSVG
- one turtle called "square_triangle" that draws a square and a triangle
- one turtle called "printLA" that draws the letters LA
- I have a sample code file "test1.py" within the project that will allow a user to generate a sample composition 




#Author
Michael Jan
Vanderbilt University
CS 6388 
Model Integrated Computing

