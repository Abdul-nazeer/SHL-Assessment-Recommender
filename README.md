
# **SHL Assessment Recommendation System 🎯🤖**  
AI-powered recommendation system for **SHL Assessments**, using **LLMs, ranking metrics, and API-based recommendations**.  

---

## **Overview**  
The **SHL Assessment Recommendation System** is an AI-driven tool that suggests the most relevant SHL assessments based on:  

**Natural language queries**  
**Job descriptions**  
**Specific skill requirements**  

Using **Sentence Transformers**, **Cosine Similarity**, and **Ranking Evaluation Metrics (Recall@K, MAP@K)**, this project ensures **precise recommendations** tailored to hiring needs.  

🔍 **Intelligent Assessment Matching**  
⚡ **Fast & Efficient API-based Search**  
📊 **Optimized Ranking with Evaluation Metrics**  

---

## **✨ Key Features**  

✅ **AI-Powered Assessment Matching** – Uses **LLMs** for natural language understanding.  
✅ **Cosine Similarity-based Ranking** – Ensures **accurate recommendations**.  
✅ **Custom Filters** – Filter assessments by **category, duration, and relevance**.  
✅ **API-Driven Integration** – Access recommendations via a REST API.  
✅ **Evaluation Metrics (MAP@K, Recall@K)** – Measure the ranking quality of recommendations.  
✅ **Scalable & Efficient** – Handles large datasets effectively.  

---

## **🛠 Tech Stack**  

| Technology | Purpose |
|------------|---------|
| **Python** 🐍 | Core Language |
| **Sentence Transformers** 🧠 | Text Embeddings |
| **Scikit-Learn** 📊 | Cosine Similarity & Metrics |
| **FastAPI** 🚀 | API Framework |
| **JSON Dataset** 📂 | SHL Assessment Data Storage |
| **NumPy & Pandas** 🔢 | Data Processing |
| **Re (Regex)** 🔍 | Text Parsing |

---

## **💡 Concept & Future Enhancements**  

This project is designed to **optimize hiring decisions** by recommending the best SHL assessments based on **natural language queries**. 🚀  

🔹 **Fine-Tuning LLM Models** – Improve the model’s contextual understanding.  
🔹 **Database Integration (SQL/NoSQL)** – Store and retrieve assessments more efficiently.  
🔹 **Real-time User Feedback** – Allow users to **rate recommendations** and refine results.  
🔹 **Web-Based Dashboard** – Interactive UI for recruiters to explore recommendations.  
🔹 **Multi-Language Support** – Expand beyond English-based queries.  

---

## **📌 How to Install & Run**  

1️⃣ **Clone the Repository:**  
```bash
git clone https://github.com/yourusername/shl-recommendation.git
cd shl-recommendation
```

2️⃣ **Install Dependencies:**  
```bash
pip install -r requirements.txt
```

3️⃣ **Run the API Server:**  
```bash
uvicorn api:app --reload
```

4️⃣ **Access the API:**  
Open your browser and go to:  
```
http://127.0.0.1:8000/docs
```
Explore the API using **Swagger UI**.

---

## **💬 How to Use the API?**  

### **🔍 Get Assessment Recommendations**  
```http
POST /recommend
```
#### **Request Body:**
```json
{
  "query": "Data Science skills assessment",
  "top_k": 5,
  "category": "Technical",
  "duration_max": 60
}
```
#### **Response:**
```json
[
  {
    "name": "SHL Data Science Test",
    "description": "Evaluates data science proficiency.",
    "category": "Technical",
    "duration": "45 minutes",
    "skills_tested": ["Python", "Machine Learning", "Data Analysis"],
    "score": 0.92
  },
  ...
]
```

### **📂 Get Available Categories**  
```http
GET /categories
```
#### **Response:**
```json
{
  "categories": ["Technical", "Aptitude", "Leadership", "Cognitive Ability"]
}
```

---

## **📊 Evaluation Metrics**  

To **measure the accuracy and relevance** of recommendations, this project uses:  

📌 **Mean Average Precision at K (MAP@K)** – Evaluates **ranking precision** across multiple queries.  
📌 **Mean Recall at K (Recall@K)** – Measures the **recall** of relevant assessments within the top-K recommendations.  

---

## **📜 License**  
This project is licensed under the **MIT License**. Feel free to **modify and contribute**!  

---

## **📬 Contact & Contributions**  
👤 **Author:** Abdul Nazeer M 
📧 **Email:** roxnazeer@gmail.com.com  
🔗 **LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/abdul-nazeer-m-ba4111253/)  
🐍 **GitHub:** [Your GitHub](https://github.com/Abdul-nazeer)  

💡 **Want to contribute?** Fork the repo and submit a **Pull Request (PR)**!  

---

🚀 **Revolutionizing hiring with AI-powered SHL assessments!** Let’s build the future of **intelligent recruitment** together. 🎯
