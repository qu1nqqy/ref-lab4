# 🧠 needref — TODO-лист на FastAPI + Cython + Redis

Экспериментальный проект, где backend написан на **FastAPI** с бизнес-логикой на **Cython**, а все данные хранятся в **Redis**.  
Фронт — простой HTML/JS, запускается отдельно. Всё собирается через **Docker Compose**.

---

## 🚀 Запуск

```bash
docker compose up --build
```

⬇️ После сборки:

- 🌐 **Фронт**: http://localhost:3000  
- ⚙️ **Backend (Swagger)**: http://localhost:8000/docs  
- 🧱 **Redis**: http://localhost:6379 (если хочешь смотреть вручную через `redis-cli`)

---

## 📦 Стек

- **FastAPI** — HTTP API
- **Cython** — ускоренная логика работы с Redis
- **Redis** — единственное хранилище
- **HTML/JS** — простейший фронт
- **Docker Compose** — сборка и запуск
- **Nginx (alpine)** — для фронта

---

## 📁 Структура

```
needref/
├── backend/
│   ├── app/
│   │   ├── main.py        # FastAPI-приложение
│   │   ├── todo.pyx       # Cython логика
│   │   ├── todo.pxd       # Cython сигнатуры
│   ├── requirements.txt   # зависимости
│   ├── Dockerfile
├── frontend/
│   ├── index.html
│   ├── static/
│   │   └── script.js
│   ├── Dockerfile         # nginx + фронт
├── docker-compose.yml
```

---

## ✅ Возможности

- Добавить задачу
- Просмотреть список задач
- Пометить как выполненную
- Удалить задачу

---

## 🧠 Что можно отрефакторить / улучшить

- [ ] 🐍 Вынести бизнес-логику Cython в отдельный пакет
- [ ] 🔒 Добавить авторизацию (JWT / Telegram login / пароль)
- [ ] 📦 Перейти на базу (PostgreSQL) в проде
- [ ] 🖼 Добавить красивый фронт на React/Vite
- [ ] 🧪 Добавить тесты (unit + интеграционные)
- [ ] ⚡️ Ускорить cython-функции с `nogil`, `typed memoryviews`
- [ ] 🧱 Обернуть Redis в абстракцию (можно подменять хранилище)

---

## 💬 Пример API

```http
POST /add?text=Починить билд
GET  /list
POST /done/{task_id}
DELETE /delete/{task_id}
```

---

## 🛠 Команды для отладки

```bash
# Зайти в бэкенд-контейнер
docker compose exec backend sh

# Проверить Redis
docker compose exec redis redis-cli
> keys *
```

---

## 🧑‍💻 Автор

Создан как прикол-проект в MTUCI ❤️  
Если хочешь доработать — форкни и пиши свои фичи!
