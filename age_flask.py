from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def home():
    # Load data from CSV file
    data = pd.read_csv('india_population_by_age_groups.csv')

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.bar(data['Age Group'], data['Population'], color='skyblue', edgecolor='black')

    # Define the y-ticks for the population
    y_ticks = [i * 100000000 for i in range(1, 10)]
    plt.yticks(y_ticks)

    # Set the title and labels
    plt.title('Population of India per age group')
    plt.xlabel('Age groups')
    plt.ylabel('Population')

    # Save the plot to a BytesIO object and encode it in base64 to send to the browser
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')

    # Render the HTML template with the plot embedded as a base64 image
    return render_template('index.html', img_base64=img_base64)

if __name__ == '__main__':
    app.run(debug=True)
