import asyncio
import logging


LOGGER_FORMAT = "%(levelname)s %(asctime)s %(message)s"
logging.basicConfig(format=LOGGER_FORMAT, datefmt='[%H:%M:%S]', level=logging.INFO)
logging.getLogger("asyncio").setLevel(logging.DEBUG)


async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    logging.info(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    logging.info(f'Received: {data.decode()}')

    logging.info('Close the connection')
    writer.close()

asyncio.run(tcp_echo_client('Hello World!'), debug=True)