# 📰 News Feed Aggregator  

## 📌 Overview  
This project is a **News Feed Aggregator** that collects, categorizes, and displays news articles from multiple sources. It utilizes **hash functions** for efficient data retrieval and duplication prevention, ensuring an optimized and up-to-date news feed.  

## 🚀 Features  
- 📰 **Aggregates News from Multiple Sources**  
- ⚡ **Efficient Hash-Based Deduplication** – Prevents duplicate articles  
- 🎯 **Smart Categorization** – Groups news into topics (Politics, Sports, Tech, etc.)  
- 🔄 **Real-Time Updates** – Fetches the latest news dynamically  
- 📊 **User-Friendly Interface** – Displays articles in an organized format  

## 🛠️ Tech Stack  
- **Programming Language:** Python  
- **Libraries:** Requests, BeautifulSoup, Hashlib, JSON  
- **Data Handling:** Hash Functions for deduplication  
- **APIs Used:** RSS Feeds / News API  

## 📂 Folder Structure  
```
📂 News-Feed-Aggregator   
│── 📜 app.py  # Main script for fetching and processing news  
│── 📜 requirements.txt  # Dependencies list  
│── 📜 index.html
│── 📜 styles.css
│── 📜 .envy
 
```

## 📖 How It Works  
1. **Fetch News** – The system collects articles from predefined sources (APIs, RSS Feeds).  
2. **Process & Filter** – Extracts titles, summaries, and URLs while removing duplicates.  
3. **Hashing for Deduplication** – Uses hash functions to ensure unique articles.  
4. **Categorize News** – Groups news by topic based on keywords or predefined tags.  
5. **Display Results** – Outputs the latest news in a structured and readable format.  


