import asyncio
from datetime import datetime

messages_list = [
    {
        "datetime": "%Y-%m-%dT%H:%M:%S",
        "payload": int
    },
]
valid = list()

for i in range(300):
    if (i % 10 == 0 and i != 0):
        valid.append(i)

result = list()
checker = list()
up_status = list()
down_status = list()

async def sensor_eight(messages_list):
    await asyncio.sleep(1)
    for i in range(11):
        time = datetime.utcnow()
        result.append({"datetime": time.strftime("%Y-%m-%dT%H:%M:%S"), "payload": i})

    for i in range(len(result)):
        checker = result[i]
        for key, value in checker.items():
            if (type(value) == int and value % 10 == 0 and value != 0):
                datetime_obj = datetime.strptime(checker["datetime"], "%Y-%m-%dT%H:%M:%S")
                checker[key] = "Up"
                up_status.append({"datetime":datetime_obj.strftime("%M:%S"), "payload": checker[key]})  
                print(up_status, "EIGHT", "\n")
                up_status.clear()
            elif(type(value) == int and value % 10 != 0 and value != 0):
                datetime_obj = datetime.strptime(checker["datetime"], "%Y-%m-%dT%H:%M:%S")
                checker[key] = "Down"
                down_status.append({"datetime":datetime_obj.strftime("%M:%S"), "payload": checker[key]})
                print(down_status, "EIGHT", "\n")
                down_status.clear()
    print("\n\n\n")
    result.clear()

async def main():
    asyncio.create_task(sensor_eight(messages_list))
