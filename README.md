# python-django-practice-2
📌 Задачи
1. Корутины и asyncio
Реализация двух асинхронных API-запросов с разной задержкой.

Использование asyncio.create_task() для параллельного выполнения.

Файл: task1_coroutines.py

2. Состояния задач и as_completed
Проверка статуса задач через task.done().

Получение результатов по мере завершения с asyncio.as_completed().

Файл: task2_states.py

3. Многопоточность (threading)
Запуск блокирующих операций в отдельных потоках.

Ожидание завершения через thread.join().

Файл: task3_threads.py

4. Семафоры (asyncio.Semaphore)
Ограничение одновременного выполнения корутин с помощью Semaphore(2).

Файл: task4_semaphore.py

🚀 Запуск
Все задачи запускаются независимо. Требуется Python 3.7+.

bash
# Установка зависимостей (если нужны)
pip install asyncio

# Запуск задач
python task1_coroutines.py,
python task2_states.py,
python task3_threads.py,
python task4_semaphore.py,

🛠 Технологии
Python 3.7+

Модули:

asyncio (для асинхронных задач)

threading (для многопоточности)

📝 Примечания
Для задач 1–2 используется asyncio, для задачи 3 — threading.

В задаче 4 семафор ограничивает одновременный доступ к ресурсу.

