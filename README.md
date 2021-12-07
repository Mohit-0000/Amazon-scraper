
# Amazon Scraping Using Scrapy.

A simple amazon scraper to extract Product details from Amazon.in using Scrapy.

# Usage

From a terminal

- Clone this project 
```bash
git clone https://github.com/Mohit-0000/Amazon-scraper.git and cd into it cd amazon_scrapy
```
- Add a Virtual Environment 
```bash
python3 -m venv .venv
```
- Activate the Virtual Environment 
```bash
source .venv/bin/activate
```
- Install Requirements 
```bash
pip3 install -r requirements.txt
```
- NOTE : Checkout to Updated branch 


# Scrape Product Details from Product Page

- run  command to get data in CSV format 
```bash 
scrapy crawl amazon_items -o file_name.csv
```
- run  command to get data in JSON format
```bash 
scrapy crawl amazon_items -o file_name.json
```
- Enter the product name 
```bash
Product name -
```

# Example Data Format

## Product Details

```bash
[
    {
        "brand": "Vincent Chase",
        "title": "by Lenskart | 
                Square Stylish Sunglasses | 
                Polarized & UV Protected | 
                For Men & Women | Large | 
                VC S12644",
        "price": "799",
        "rating": "3.8 out of 5 stars",
        "total_review": "86",
        "image_url": "https://m.media-amazon.com/images/I/51LyqBqc4KL._AC_UL320_.jpg"
    },
    {
        "brand": "VINCENT CHASE EYEWEAR",
        "title": "Vincent Chase by Lenskart |
                 Round Stylish Sunglasses | 
                 Polarized & UV Protected | 
                 For Men & Women | Large |
                  VC S13832",
        "price": "999",
        "rating": "3.4 out of 5 stars",
        "total_review": "12",
        "image_url": "https://m.media-amazon.com/images/I/41FxjmXd1gS._AC_UL320_.jpg"
    },
    {
        "brand": "VINCENT CHASE EYEWEAR",
        "title": "Vincent Chase by lenskart | 
                Square Stylish Sunglasses | 
                Polarized & UV Protected | 
                For Men & Women | 
                (54) Black Frame Green LensesS13159",
        "price": "799",
        "rating": "4.0 out of 5 stars",
        "total_review": "14",
        "image_url": "https://m.media-amazon.com/images/I/41-sJAb5jLL._AC_UL320_.jpg"
    },
    {
        "brand": "VINCENT CHASE EYEWEAR",
        "title": "Vincent Chase by Lenskart | 
                Round Stylish Sunglasses | 
                Polarized & UV Protected | 
                For Men & Women | Medium | 
                VC S13975",
        "price": "1,415",
        "rating": "4.5 out of 5 stars",
        "total_review": "5",
        "image_url": "https://m.media-amazon.com/images/I/514QMScQJVS._AC_UL320_.jpg"
    }
]
```


