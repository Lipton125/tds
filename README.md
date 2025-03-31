# tds
## Uses DeepSeek - V3
## Made with help of ChatGPT 
## Hosted using [Render](https://tds-9h1p.onrender.com/)

### Send POST request : 
curl -X POST 'https://tds-9h1p.onrender.com/api/' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'question=What is the capital of India?'

### Send POST request with file upload:
curl -X POST 'https://tds-9h1p.onrender.com/api/' \
-F 'question=What is the total number of ducks across players on page number 39 of https://stats.espncricinfo.com/stats/engine/stats/index.html?class=2;template=results;type=batting' \
-F 'file=@/path/to/your/file.txt'

