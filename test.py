import requests
import json

headers = {
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImEyZWRlYTcyYmI5NjU3NDk2Mjk4Y2IyOTJhMThhMmNiMDA4MjViN2EyOTU1NDQ2NDQxNjU5OGU5ZjQyMzFkZmYyNzhiZjc4NWQzOGIxZGIyIn0.eyJhdWQiOiIyIiwianRpIjoiYTJlZGVhNzJiYjk2NTc0OTYyOThjYjI5MmExOGEyY2IwMDgyNWI3YTI5NTU0NDY0NDE2NTk4ZTlmNDIzMWRmZjI3OGJmNzg1ZDM4YjFkYjIiLCJpYXQiOjE2MDkyMDQxMTAsIm5iZiI6MTYwOTIwNDExMCwiZXhwIjoxNjA5MjkwNTEwLCJzdWIiOiIxMzQ3ZTc3MC02ZjhiLTExZTktOTJmZS00OTljNjUxZTVhNWEiLCJzY29wZXMiOltdfQ.K02rbmx46NBmjr2c9uFfBqO6hgeb_gDiEgqyEsE6E8gMAQ1rBFZ_qwiGhUS7V1Wpd5_mucXRTFx61U6FJiWnot3plA1RYnEK7uuWC5KkVXCronktkkTK9PgdR4q08H_NIf3mSo3JgzEKAfqsQixoiEdtuSjjgh1kS7ha8jfwfUwJfA87-GJ9PoUisxoobmDapuL9QpmtUVaO0CEIjLMd53uIyCbOJtNm6HN7RqAg2osXO9aEFSaF54_AfNsaCCA-GtDuWurf7_j2lubxOs3FACjvfuUMIGXsgBJPxuNlDh_RAY5YwusoCi39oc9wXqt7MJHhs_TaXvUefeN4daV-MALRDzha1GehV2O72aX6Rimozyi9rapmBWvm5yP2F6Ay7hrD8RdVk2Vqv9fqws9OziGEve-L8elX0BMMeZZtYpefmyIBcfD-MyGHq_zvldYcqn4UBgCIlE9dQBFYWgR_TXFZyXR2sgCsHh1PUZjpAQj0taC5laZEG-CmTUIwX9TfvhCwbdJGShpOtirbShrynQDACz8nPC4fCsWnF1Rg2WmUkJNWNVvNhuK-v4ALbwHvSkKFUp44H9UFzbJ0VP57vmjhvoXAF88CZwUYiy-DfXBfiGTQhe6PoPgv3Ujl-VZsD6cbVZYf8kxn0e2bSOah0xqHnur9kkEcyak3ngRC5uI",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

source_file = open("10.txt", "r")

for aline in source_file:
    code = aline
    host_url = "https://mpm-motor.qtrust.id/api/agent/qrcode?code=" + code
    response_code = requests.get(host_url, headers=headers)
    print (response_code.elapsed, end ="\t")
    print (code, end ="")
    # print (response_code.json())

source_file.close()
