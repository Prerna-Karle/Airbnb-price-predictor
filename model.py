def predict_price(data):
    # simple fake logic (replace later with ML)
    price = (
        data["bedrooms"] * 50 +
        data["bathrooms"] * 30 +
        data["accommodates"] * 20 +
        data["amenities"] * 5
    )
    return round(price, 2)