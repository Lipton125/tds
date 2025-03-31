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
-F 'question=Answer the question in attached text file.' \
-F 'file=@/path/to/your/file.txt'

