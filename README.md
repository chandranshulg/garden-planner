# Interactive Garden Planner

An interactive web application that allows users to design their garden by dragging and dropping plant icons onto a virtual garden canvas. Users can see detailed information about each plant, including compatibility with other plants and sunlight requirements.

## Installation

To get started with the project, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/chandranshulg/garden-planner.git
   cd garden-planner
2. **Install Dependencies** 

   pip install -r requirements.txt

3. **Run the Application**

    python app.py

## Usage

Open the web application in your browser.
Select a plant from the "Select a plant to add" section.
Drag the plant icon onto the garden canvas.
The plant icon will appear on the canvas, and its details will be displayed below the canvas.

## Plant Data

The following plant data is used in the application:

Tomato: Compatibility: Basil, Carrot | Sunlight: Full Sun

Basil: Compatibility: Tomato, Pepper | Sunlight: Partial Sun

Carrot: Compatibility: Tomato, Lettuce | Sunlight: Full Sun

Pepper: Compatibility: Basil | Sunlight: Full Sun

Lettuce: Compatibility: Carrot | Sunlight: Partial Sun

## Requirements

Ensure the following Python packages are installed:

Flask==2.3.3

Create a requirements.txt file with these dependencies:
Flask==2.3.3

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.


