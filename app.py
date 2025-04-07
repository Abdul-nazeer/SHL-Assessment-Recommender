import streamlit as st
from api import SHLRecommender
import time

def main():
    st.set_page_config(
        page_title="SHL Assessment Recommender",
        layout="wide"
    )
    
    # Add custom CSS for gradient background and black input
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #ffffff;
        }
        .stTextArea textarea {
            background-color: #000000;
            color: #ffffff;
            border: 1px solid #ffffff;
        }
        .stButton>button {
            background-color: #ffffff;
            color: #667eea;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Initialize recommender
    try:
        recommender = SHLRecommender()
    except Exception as e:
        st.error(f"Failed to initialize recommender: {str(e)}")
        st.stop()
    
    # Sidebar filters
    st.sidebar.title("Filters")
    category = st.sidebar.selectbox(
        "Assessment Category",
        options=["All"] + recommender.get_categories()
    )
    duration_filter = st.sidebar.slider(
        "Maximum Duration (minutes)", 
        min_value=15, 
        max_value=120, 
        value=60,
        step=5
    )
    
    # Main interface
    st.title("""🤖 SHL Assessment Recommender  
_Matching Job Roles with SHL Assessments_
""")
    #st.write("Find the perfect SHL assessment for your hiring needs")
    st.markdown("---")
    # Search query
    query = st.text_area(
        "Describe your needs:",
        placeholder="e.g., We need a cognitive test for software engineers under 45 minutes ",
        height=150
    )
    
    if st.button("Get Recommendations"):
        if not query.strip():
            st.warning("Please enter a description of your needs")
        else:
            with st.spinner("Finding the best assessments..."):
                try:
                    start_time = time.time()
                    recommendations = recommender.recommend(
                        query,
                        category=None if category == "All" else category,
                        duration_max=duration_filter
                    )
                    elapsed = time.time() - start_time
                    
                    if not recommendations:
                        st.warning("No matching assessments found. Try broadening your filters.")
                    else:
                        st.success(f"Found {len(recommendations)} recommendations in {elapsed:.2f} seconds")
                        
                        for i, rec in enumerate(recommendations, 1):
                            with st.expander(f"{i}. {rec['name']} (Score: {rec['score']:.2f})"):
                                cols = st.columns([1, 3])
                                with cols[0]:
                                    st.markdown(f"**Test Link**: {rec['url']}")
                                    st.markdown(f"**Category**: {rec['category']}")
                                    st.markdown(f"**Duration**: {rec['duration']}")
                                    st.markdown(f"**Remote**: {'Yes' if rec['remote'] else 'No'}")
                                    st.markdown(f"**Adaptive**: {'Yes' if rec['adaptive'] else 'No'}")
                                
                                with cols[1]:
                                    st.markdown(f"**Description**: {rec['description']}")
                                    if rec.get('skills_tested'):
                                        st.markdown(f"**Skills Tested**: {', '.join(rec['skills_tested'])}")
                                    if rec.get('use_cases'):
                                        st.markdown(f"**Best For**: {', '.join(rec['use_cases'])}")
                                    
                                    st.markdown(f"[View Details]({rec['url']})")
                
                except Exception as e:
                    st.error(f"Error generating recommendations: {str(e)}")
    
    # Footer with your name and details
    st.markdown("---")
    st.markdown("📎 [GitHub](https://github.com/Abdul-nazeer) | 🤖 Powered by FastAPI, Streamlit, and SentenceTransformers")
    st.caption("© 2025 Abdul Nazeer | SHL GenAI Assignment")

if __name__ == "__main__":
    main()