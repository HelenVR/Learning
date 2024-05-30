"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
import random

from homework_04.models import User, Post, Base, engine, Session
from aiohttp import ClientTimeout, ClientSession
from homework_04.jsonplaceholder_requests import fetch_users_data, fetch_posts_data


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    session = ClientSession(timeout=ClientTimeout(total=5.0))
    users_data, posts_data = await asyncio.gather(fetch_users_data(session),
                                                  fetch_posts_data(session))
    users, users_ids = users_data
    await session.close()
    for post in posts_data:
        post.user_id = random.choice(users_ids)
    async with Session() as session:
        async with session.begin():

            session.add_all(users)

            posts = posts_data
            session.add_all(posts)

        await engine.dispose()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
