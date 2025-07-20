#!/usr/bin/env python3
"""
Complete library verification script for Healthcare Chatbot Project
"""
import sys
print(f"🐍 Python version: {sys.version}")
print("="*60)

# Test core libraries
tests = [
    ("NumPy", "import numpy as np; print(f'   Version: {np.__version__}')"),
    ("Pandas", "import pandas as pd; print(f'   Version: {pd.__version__}')"),
    ("Scikit-learn", "import sklearn; print(f'   Version: {sklearn.__version__}')"),
    ("Matplotlib", "import matplotlib; print(f'   Version: {matplotlib.__version__}')"),
    ("Seaborn", "import seaborn as sns; print(f'   Version: {sns.__version__}')"),
    ("NLTK", "import nltk; print(f'   Version: {nltk.__version__}')"),
    ("Requests", "import requests; print(f'   Version: {requests.__version__}')"),
    ("BeautifulSoup", "from bs4 import BeautifulSoup; print('   OK')"),
    ("TQDM", "from tqdm import tqdm; print('   OK')"),
    ("NetworkX", "import networkx as nx; print(f'   Version: {nx.__version__}')"),
    ("WordCloud", "from wordcloud import WordCloud; print('   OK')"),
    ("Jupyter", "import jupyter; print('   OK')"),
]

# Advanced libraries (optional)
advanced_tests = [
    ("spaCy", "import spacy; print(f'   Version: {spacy.__version__}')"),
    ("Sentence Transformers", "from sentence_transformers import SentenceTransformer; print('   OK')"),
    ("HDBSCAN", "import hdbscan; print(f'   Version: {hdbscan.__version__}')"),
    ("Plotly", "import plotly; print(f'   Version: {plotly.__version__}')"),
]

print("📦 Core Libraries:")
passed = 0
failed = 0

for name, test_code in tests:
    try:
        exec(test_code)
        print(f"✅ {name}")
        passed += 1
    except Exception as e:
        print(f"❌ {name}: {e}")
        failed += 1

print(f"\n🚀 Advanced Libraries:")
for name, test_code in advanced_tests:
    try:
        exec(test_code)
        print(f"✅ {name}")
        passed += 1
    except Exception as e:
        print(f"❌ {name}: {e}")
        failed += 1

print(f"\n📊 Summary:")
print(f"   ✅ Passed: {passed}")
print(f"   ❌ Failed: {failed}")

# Test spaCy model
print(f"\n🔍 Testing spaCy model:")
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("This is a test sentence.")
    print("✅ spaCy en_core_web_sm model: OK")
except Exception as e:
    print(f"❌ spaCy model: {e}")
    print("💡 Run: python -m spacy download en_core_web_sm")

print(f"\n🎉 Verification completed!")
if failed == 0:
    print("🚀 All libraries ready for Healthcare Chatbot project!")
else:
    print("⚠️ Some libraries failed. Check errors above.")
