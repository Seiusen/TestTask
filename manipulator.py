import asyncio
from sensor_one import main as one
from sensor_two import main as two
from sensor_three import main as three
from sensor_four import main as four
from sensor_five import main as five
from sensor_six import main as six
from sensor_seven import main as seven
from sensor_eight import main as eight

async def main():
    for i in range(10):
        await asyncio.gather(one(), two(), three(), four(), five(), six(), seven(), eight())
        await asyncio.sleep(1)
    

if __name__ == '__main__':
    asyncio.run(main())