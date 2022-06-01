Программа отправляет JSON-файлы на указанный url.
Параметры:
  -file FILE  Файл для отправки. Значение по умолчанию: simple_request.json
  -url URL    Адрес для запроса. Значение по умолчанию: http://10.100.127.1:8080/create_plan

Примеры запуска:
main.exe -file="request__2022-05-31 11-35-56_.json"
main.exe -url=http://127.0.0.1:8080/create_plan
main.exe -file="request__2022-05-31 11-35-56_.json" -url=http://127.0.0.1:8080/create_plan