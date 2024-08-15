from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Sample plant data for compatibility and sunlight exposure
plants_data = {
    'Tomato': {'compatibility': ['Basil', 'Carrot'], 'sunlight': 'Full Sun'},
    'Basil': {'compatibility': ['Tomato', 'Pepper'], 'sunlight': 'Partial Sun'},
    'Carrot': {'compatibility': ['Tomato', 'Lettuce'], 'sunlight': 'Full Sun'},
    'Pepper': {'compatibility': ['Basil'], 'sunlight': 'Full Sun'},
    'Lettuce': {'compatibility': ['Carrot'], 'sunlight': 'Partial Sun'},
}

# HTML template with JavaScript for interactive garden planner
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Garden Planner</title>
    <style>
        #garden-canvas {
            border: 2px solid #000;
            width: 100%;
            height: 500px;
            position: relative;
            background-color: #e0e0e0;
        }
        .plant-icon {
            width: 50px;
            height: 50px;
            position: absolute;
            cursor: grab;
        }
        #plant-options {
            margin-top: 20px;
        }
        #plant-options img {
            width: 50px;
            height: 50px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="mt-5 text-center">Interactive Garden Planner</h1>
        <div id="garden-canvas"></div>
        <div id="plant-options" class="mt-4">
            <h2>Select a plant to add:</h2>
            {% for plant in plants %}
                <img src="{{ url_for('static', filename='images/' + plant + '.png') }}" 
                     alt="{{ plant }}" 
                     data-plant="{{ plant }}" 
                     draggable="true" 
                     ondragstart="drag(event)">
            {% endfor %}
        </div>
        <div id="plant-info" class="mt-4">
            <h2>Plant Information</h2>
            <p id="plant-details">Drag a plant icon onto the garden to see its details.</p>
        </div>
    </div>
    <script>
        // Initialize plant data
        const plantsData = {{ plants_data | tojson }};
        const gardenCanvas = document.getElementById('garden-canvas');

        // Function to handle drag start event
        function drag(event) {
            event.dataTransfer.setData("text", event.target.dataset.plant);
        }

        // Function to allow drop
        function allowDrop(event) {
            event.preventDefault();
        }

        // Function to handle drop event
        function drop(event) {
            event.preventDefault();
            const plant = event.dataTransfer.getData("text");
            const plantIcon = document.createElement('img');
            plantIcon.src = `{{ url_for('static', filename='images') }}/${plant}.png`;
            plantIcon.className = 'plant-icon';
            plantIcon.style.left = `${event.clientX - 25}px`;
            plantIcon.style.top = `${event.clientY - 25}px`;
            gardenCanvas.appendChild(plantIcon);
            showPlantInfo(plant);
        }

        // Function to show plant information
        function showPlantInfo(plant) {
            const plantDetails = document.getElementById('plant-details');
            const plantData = plantsData[plant];
            plantDetails.innerHTML = `
                <strong>${plant}</strong><br>
                Compatibility: ${plantData.compatibility.join(', ')}<br>
                Sunlight: ${plantData.sunlight}
            `;
        }

        // Set up event listeners
        gardenCanvas.addEventListener('dragover', allowDrop);
        gardenCanvas.addEventListener('drop', drop);
    </script>
</body>
</html>
'''

# Home route
@app.route('/')
def index():
    return render_template_string(html_template, plants=plants_data.keys(), plants_data=plants_data)

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
