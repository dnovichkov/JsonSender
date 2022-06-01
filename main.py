import argparse
import json
import loguru
import os
import requests


def load_json(json_filename):

    filename = os.path.join(os.path.dirname(__file__), json_filename)
    if not json_filename:
        return None
    with open(filename, encoding='utf-8') as f:
        data = f.read()
        json_data = json.loads(data)
        return json_data


def send_json(filename, url):

    loguru.logger.debug(f'Загружаем файл: {filename}')
    data = load_json(filename)
    loguru.logger.debug(f'Файл: {filename} загружен')

    loguru.logger.debug(f'Отправляем запрос на: {url}')
    resp = requests.post(url, json=data)
    loguru.logger.debug(f'Получен code: {resp.status_code}')
    loguru.logger.debug(f'Получен ответ: {resp.content}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Json Sender')
    parser.add_argument('-file', type=str, default='simple_request.json', help='Файл для отправки')
    parser.add_argument('-url', type=str, default='http://10.100.127.1:8080/create_plan',
                        help='Адрес для запроса')

    args = parser.parse_args()
    loguru.logger.debug(f'Загружена программа')
    loguru.logger.debug(f'Файл: {args.file}')
    loguru.logger.debug(f'Адрес: {args.url}')

    send_json(args.file, args.url)
