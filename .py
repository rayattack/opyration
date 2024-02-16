from asyncio import get_event_loop

from opyration import Operation
from asyncpg import create_pool, Pool


async def run():
    pool: Pool = await create_pool('postgres://postgres:postgres@localhost:5432/sample')
    op = Operation('usernames', pool)
    op.select().where(username='username')
    await op.run()
    print(op.json)


if __name__ == '__main__':
    loop = get_event_loop()
    loop.run_until_complete(run())
