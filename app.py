from flask import Flask, render_template, request

app = Flask(__name__)

# Mock Predictions (replace this with actual model predictions once models are working)
def mock_predict(input_data):
    # Return mock predictions for testing
    return 3.50, "Region 1"  # Mock price and region

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        
            # Get user input from the form and ensure correct data types
            total_volume = float(request.form["total_volume"])
            plu_4046 = float(request.form["plu_4046"])
            plu_4225 = float(request.form["plu_4225"])
            plu_4770 = float(request.form["plu_4770"])
            total_bags = float(request.form["total_bags"])
            small_bags = float(request.form["small_bags"])
            large_bags = float(request.form["large_bags"])
            xlarge_bags = float(request.form["xlarge_bags"])
            month = int(request.form["month"])
            day = int(request.form["day"])
            avocado_type = request.form["type"]

            # Prepare input data for the models
            input_data = {
                'Total Volume': total_volume,
                'PLU 4046': plu_4046,
                'PLU 4225': plu_4225,
                'PLU 4770': plu_4770,
                'Total Bags': total_bags,
                'Small Bags': small_bags,
                'Large Bags': large_bags,
                'X-Large Bags': xlarge_bags,
                'Month': month,
                'Day': day,
                'Type': avocado_type
            }

            # Use the mock prediction function instead of the real model
            price_prediction, region_prediction = mock_predict(input_data)

            # Return result to the HTML template
            return render_template("index.html", 
                                   price=round(price_prediction, 2), 
                                   region=region_prediction)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

