import pandas as pd
import ollama
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Memuat dataset
df = pd.read_csv('BooksDatasetClean.csv')

# Menghapus baris yang memiliki deskripsi kosong atau NaN
df = df.dropna(subset=['Description'])

# Jika data lebih dari 5000, pilih 5000 data pertama
if len(df) > 500:
    df = df.head(500)

# Fungsi untuk mendapatkan embeddings dari model Ollama
def get_embeddings(text: str):
    try:
        response = ollama.embeddings(model="nomic-embed-text", prompt=text)
        return response['embedding']  # Mendapatkan embeddings dari response
    except Exception as e:
        print(f"Error: {e}")
        return []

# Membuat embeddings untuk setiap deskripsi buku
df['Description_embeddings'] = df['Description'].apply(get_embeddings)

# Fungsi untuk mencari rekomendasi berdasarkan kemiripan deskripsi buku
def recommend_books(user_input, df):
    # Mendapatkan embedding untuk input pengguna
    user_embedding = get_embeddings(user_input)
    
    if len(user_embedding) == 0:
        return pd.DataFrame()  # Menghindari error jika embedding kosong
    
    # Menghitung kemiripan dengan deskripsi buku yang ada di dataset
    similarity_scores = []
    for emb in df['Description_embeddings']:
        similarity_scores.append(cosine_similarity([user_embedding], [emb])[0][0])
    
    df['Similarity'] = similarity_scores
    recommendations = df.sort_values(by='Similarity', ascending=False).head(5)  # Mengambil 5 buku teratas
    return recommendations[['Title', 'Authors', 'Category', 'Price Starting With ($)', 'Similarity']]

# Streamlit GUI untuk sistem rekomendasi
def main():
    st.title('Book Recommendation System')
    
    # Input dari pengguna
    user_input = st.text_input("Enter a description of a book:")
    
    if st.button('Get Recommendations'):
        if user_input:
            recommendations = recommend_books(user_input, df)
            if not recommendations.empty:
                st.write("Top 5 Recommended Books:")
                st.write(recommendations)
            else:
                st.write("No recommendations found. Please try again.")
        else:
            st.write("Please enter a description to get recommendations.")

if __name__ == '__main__':
    main()
