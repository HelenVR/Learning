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
from homework_04.models import User, Post, Base, engine, Session
from aiohttp import ClientTimeout, ClientSession
from homework_04.jsonplaceholder_requests import fetch_json, USERS_DATA_URL, POSTS_DATA_URL


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    session = ClientSession(timeout=ClientTimeout(total=5.0))
    users_data, posts_data = await asyncio.gather(fetch_json(session, USERS_DATA_URL),
                                                  fetch_json(session, POSTS_DATA_URL))
    async with Session() as session:
        async with session.begin():

            users = [User(**user_data) for user_data in users_data]
            session.add_all(users)
            await session.commit()

            posts = [Post(**post_data) for post_data in posts_data]
            session.add_all(posts)
            await session.commit()

        await engine.dispose()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()