import asyncio
import aiohttp


REVIEW_ID = "z9FjBK43Cg9qum55W"
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MjMsInVzZXJuYW1lIjoiIiwiZW1haWwiOiJuaWtheWxlekBnbWFpbC5jb20iLCJwYXNzd29yZCI6IjgyN2NjYjBlZWE4YTcwNmM0YzM0YTE2ODkxZjg0ZTdiIiwicm9sZSI6ImN1c3RvbWVyIiwiZGVsdXhlVG9rZW4iOiIiLCJsYXN0TG9naW5JcCI6IjAuMC4wLjAiLCJwcm9maWxlSW1hZ2UiOiIvYXNzZXRzL3B1YmxpYy9pbWFnZXMvdXBsb2Fkcy9kZWZhdWx0LnN2ZyIsInRvdHBTZWNyZXQiOiIiLCJpc0FjdGl2ZSI6dHJ1ZSwiY3JlYXRlZEF0IjoiMjAyNi0wNS0yMCAyMDozNzozNy40NTAgKzAwOjAwIiwidXBkYXRlZEF0IjoiMjAyNi0wNS0yMCAyMDozNzozNy40NTAgKzAwOjAwIiwiZGVsZXRlZEF0IjpudWxsfSwiaWF0IjoxNzc5MzA5NDYzfQ.hGgrjMoEBi4Jn00nYPFnUfoQFCYFgSAyF4b7Nx-j4DFyDVMm_AfTrS81-4ezgI4mgb1g_kkKa2i42ht-ye8xWaGhRFX3-hDcgi0ztdwHeUsO9i6-idrcAMKtKKu0OJ4p8YOwRMHwzeui6B4SahoV49CscDs0FEJT9OehxW6eVfw" 


URL = "http://10.0.2.15:65/rest/products/reviews"

async def send_like(session, id_review, n):
    body = {"id": id_review}
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    try:
        async with session.post(URL, json=body, headers=headers) as resp:
            text = await resp.text()
            print(f"[{n}] Status: {resp.status} - {text[:100]}")
    except Exception as e:
        print(f"[{n}] Error: {e}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [send_like(session, REVIEW_ID, i+1) for i in range(3)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())