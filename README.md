# Turtle Graphics MiniProject

This project allows users to create turtle graphics models using WebGME. It includes three plugins that allow users to generate Python code, generate SVG images, and import Python turtle graphics files into WebGME models.

## Installation

### Prerequisites

Before running the project, install the following:

- [Node.js](https://nodejs.org/en/) (LTS recommended)
- [MongoDB](https://www.mongodb.com/)
- WebGME and the project's required Node.js dependencies

### Starting the Project

1. Clone or download the project repository.
2. Open a terminal and navigate to the project directory.
3. Install the project dependencies:

   ```bash
   npm install
   ```

4. Start MongoDB locally using the `mongod` executable. You may need to create a data directory or specify a database path using `--dbpath`.
5. Open a second terminal and navigate to the project directory.
6. Start the WebGME application using the startup command configured for the project, such as:

   ```bash
   node app.js
   ```

7. Open a web browser and navigate to:

   http://localhost:8888

The WebGME application should now be available.

## WebGME Model Composition

To create a turtle graphics model:

1. Open the WebGME project.
2. The root contains the FCO and turtleMETA.
3. Create a Turtle entity within the root.
4. Add commands, functions, and loops to build your turtle graphics composition.

## Building Your Composition

### 1. Adding Nodes

Users can drag and drop different Commands, Functions, and ForLoops into their model.

### 2. Setting the Starting Point

Each node contains an attribute named `start`, which is set to `no` by default.

- Change the attribute to `yes` for the first node in the model.
- Each Function or ForLoop must also have a starting node within its own composition.
- There must be exactly one starting point for the overall model and exactly one starting point within each Function or ForLoop.

This allows the system to identify where execution should begin.

### 3. Connecting Nodes

Nodes are connected using the `next` pointer.

1. Select the node.
2. Open the Pointer tab.
3. Select the `next` pointer.
4. Connect it to the appropriate node.

The final node in a model, Function, or ForLoop must have its `next` pointer set to `NULL`.

### 4. Available Commands

The model supports the following commands:

- `forward` — Moves the turtle forward or backward.
- `left` — Rotates the turtle left.
- `right` — Rotates the turtle right.
- `penUp` — Lifts the pen so movement does not draw.
- `penDown` — Lowers the pen so movement draws.
- `width` — Changes the pen thickness.
- `color` — Changes the pen color.
- `clear` — Clears the drawing.
- `goto` — Moves the turtle to specified coordinates.
- `forLoop` — Repeats a sequence of commands.
- `Function` — Organizes a sequence of commands into a function.

### 5. Functions and ForLoops

Functions and ForLoops allow users to create more complex turtle graphics compositions.

- Each Function or ForLoop must have a starting point within its contents.
- The final command inside a Function or ForLoop must point to `NULL`.
- The Function or ForLoop node itself must point to the next command, Function, or ForLoop that should execute afterward.
- Nested Functions and ForLoops are supported.

### 6. Command Attributes

Several commands have attributes that determine their behavior.

| Command | Attribute | Description |
|---|---|---|
| `forward` | `value` | Integer distance; negative values move backward |
| `left` | `angle` | Integer angle for left rotation |
| `right` | `angle` | Integer angle for right rotation |
| `width` | `value` | Integer pen thickness |
| `goto` | `xCor`, `yCor` | X and Y coordinates |
| `color` | `selection` | Selects a pen color |

Available colors include red, orange, yellow, green, blue, purple, black, and white.

## Plugins

The project includes three plugins.

### 1. ToPythonFile

This plugin converts an existing turtle graphics model into executable Python code.

**Instructions:**

1. Select a Turtle model in WebGME.
2. Run the `ToPythonFile` plugin.
3. Download the generated `turtle_art.py` file.
4. Run the file using a Python 3 interpreter to display the turtle graphics drawing.

### 2. PythonToSVG

This plugin generates Python code that produces an SVG image from an existing turtle graphics model.

**Instructions:**

1. Select a Turtle model in WebGME.
2. Run the `PythonToSVG` plugin.
3. Download the generated `turtle_SVG.py` file.
4. Run the file using a Python 3 interpreter.
5. The script generates an `image_file.svg` file in the working directory.
6. Open the SVG file using a web browser or another SVG-compatible application.

### 3. ImportPython

This plugin imports Python turtle graphics code and converts it into a WebGME composition model.

**Instructions:**

1. Select the root of the WebGME project.
2. Run the `ImportPython` plugin.
3. Provide a Python turtle graphics file.
4. The plugin processes the file and generates a corresponding composition model.
5. The generated model can be accessed through the WebGME composition pane.

Unsupported or unrecognized commands may generate error warnings in the console.

## Visuals

The project includes visual representations of Commands, Functions, and ForLoops.

- Each node has a picture to help users identify its purpose.
- The visuals are static.
- Node names display attribute information to help users understand the configured commands.

## Additional Notes

1. The project includes safeguards against recursive execution.
2. Function calls are numbered in the order they are encountered.
3. Every model must have a starting point.
4. Every Function and ForLoop must have its own starting point.
5. The final command within each execution sequence must have its `next` pointer set to `NULL`.

## Assignment 8 Sample Models

The WebGME project includes two sample turtle graphics models that can be used to test the `ToPythonFile` and `PythonToSVG` plugins.

### square_triangle

Draws a square and a triangle.

### printLA

Draws the letters LA using turtle graphics commands.

### test1.py

The project also includes a sample Python file named `test1.py`, which can be used with the `ImportPython` plugin to generate a sample WebGME composition.

## Author

Michael Jan  
Vanderbilt University  
CS 6388 — Model Integrated Computing