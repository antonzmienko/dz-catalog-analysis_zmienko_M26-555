# Анализ каталога фильмов

Скрипт `catalog_analysis.py` считает статистику по встроенному каталогу и печатает отчёт.

## Требования

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Python 3.12. Если его нет в системе, `uv` поставит его сам по файлу `.python-version`.

## Запуск с нуля

```bash
git clone https://github.com/antonzmienko/dz-catalog-analysis_zmienko_M26-555.git
cd dz-catalog-analysis_zmienko_M26-555
uv sync
uv run python catalog_analysis.py
```

`uv sync` создаёт виртуальное окружение `.venv` и ставит зависимости из `uv.lock`. Для самого скрипта внешних пакетов нет; в dev-группе установлен `ruff`.

## Проверка стиля

```bash
uv run ruff check .
```
