import asyncio
import aiohttp
import time

REVIEW_ID = "ZQdzyRCbwQ4ys3PCG"  # 
TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
URL = "http://localhost:3000/rest/products/reviews"

async def send_like(session, id_review, n):
    body = {"id": id_review}
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    async with session.post(URL, json=body, headers=headers) as resp:
        text = await resp.text()
        print(f"[{n}] Status: {resp.status} - {text[:100]}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(3):
            tasks.append(send_like(session, REVIEW_ID, i+1))

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(f"Tiempo total: {(time.time() - start)*1000:.2f} ms")
