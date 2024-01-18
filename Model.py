import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from NewSong import extract_features
from sklearn.neighbors import KNeighborsClassifier

# Load the dataset
df = pd.read_csv('song_data.csv')

# Features (X) and target variable (y)
X = df.iloc[:, 2:]  # Columns 3 to the end are features
y = df['song_popularity']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Use KNeighborsClassifier instead of RandomForestClassifier
k_neighbors = 5
model = KNeighborsClassifier(n_neighbors=k_neighbors)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy * 100:.2f}%')

# Call the function to get the new song features
song_duration, acousticness, danceability, energy, instrumentalness, key, liveness, loudness, mode, speechiness, \
    tempo, time_signature, valence = extract_features()

# Incorporate the new features
new_song_features = [song_duration, acousticness, danceability, energy, instrumentalness, key, liveness, loudness, mode,
                     speechiness, tempo, time_signature, valence]
prediction = model.predict([new_song_features])
print(f'Predicted Popularity: {prediction[0]}')  # Scale of 0 - 100
