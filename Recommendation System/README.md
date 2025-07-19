
# Anime Recommendation System using Cosine Similarity

## Objective
The goal of this project is to build a content-based recommendation system that suggests anime based on genre similarity using **cosine similarity**. This system helps users discover anime titles similar to their preferences.

---

## Dataset Description
The dataset contains information about various anime titles, including:
- `anime_id`: Unique identifier
- `name`: Anime title
- `genre`: Genre tags (e.g., Action, Romance)
- `type`: Broadcast type (TV, OVA, etc.)
- `episodes`: Number of episodes
- `rating`: Average user rating
- `members`: Number of community members

---

## Tasks Performed

### 1. **Data Preprocessing**
- Loaded dataset using `pandas`
- Handled missing values and cleaned inconsistent entries
- Converted genre text data into TF-IDF numerical vectors

### 2. **Feature Extraction**
- Extracted and encoded the `genre` feature using `TfidfVectorizer`
- Constructed a cosine similarity matrix for all anime entries

### 3. **Recommendation Engine**
- Built a `recommend()` function to return top-N similar anime
- Used cosine similarity scores between genre vectors
- Adjusted similarity thresholds via the `top_n` parameter

### 4. **Evaluation**
- Evaluated model using genre-overlap-based precision
- Analyzed strengths and limitations of genre-only content-based systems

---

## Sample Output
```python
recommend("Naruto", top_n=5)
```
Returns 5 anime titles most similar to Naruto based on genre.

---

## Future Improvements
- Include collaborative filtering using user ratings
- Integrate additional features like `episodes`, `type`, or `popularity`
- Use hybrid approaches combining content-based and collaborative filtering

---
