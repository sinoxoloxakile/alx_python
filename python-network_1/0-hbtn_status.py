import requests
response = requests.get("https://alu-intranet.hbtn.io/status")
print(response.text)
- {
    "status": "OK",
    "version": "1.0.0",
    "timestamp": "2023-03-08T10:15:36.123Z"
}