## Тестовое задание для расчета депозита вклада

### Подготовка окружения

1. Установка [Python](https://www.python.org/downloads/) 3.12

2. Установка [Poetry](https://python-poetry.org/). Рекомендуюется устанавливать через [pipx](https://pipx.pypa.io/stable/installation/)

```bash
python -m pip install --user pipx
pipx install poetry
```

3. Установка зависимостей

```bash
poetry install
```

### Способы запуска приложения

Перед запуском нужно объявить переменную окружения PORT.

1. Используя [Make](https://www.gnu.org/software/make/)

```bash
make
```

2. Через poetry
 
```bash
poetry run python src/main.py
```

3.Запуск в Docker

```bash
docker compose up -d --build
```

Swagger файлт доступен по эндпоинту **/docs**
