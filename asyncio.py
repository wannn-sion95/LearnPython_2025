import asyncio

async def tugas():
    print("Mulai tugas")
    await asyncio.sleep(3)
    print("Tugas Selesai!")

async def main():
    await asyncio.gather(tugas())

asyncio.run(main())
