import os
from typing import List, Dict, Optional
import numpy as np
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from dotenv import load_dotenv
 
# Load environment variables
load_dotenv()
 
# Initialize Pinecone with your specific index
def get_pinecone_index():
    """Initialize and return Pinecone index using the specific host."""
    api_key = os.getenv("PINECONE_API_KEY")
    if not api_key:
        raise ValueError("PINECONE_API_KEY environment variable not set")
    
    # Initialize with your specific index host
    pc = Pinecone(api_key=api_key)
    return pc.Index(host="https://llm-cache-9hmd096.svc.aped-4627-b74a.pinecone.io")


index = get_pinecone_index()


