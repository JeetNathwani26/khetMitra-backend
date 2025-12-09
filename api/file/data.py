import joblib

model=joblib.load("crop_model.pkl")

sample = [[10, 20, 70, 8.5]]
prediction = model.predict(sample)
print("🌾 Recommended Crop:", prediction[0])