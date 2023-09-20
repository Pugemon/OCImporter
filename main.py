from tortoise import Tortoise, run_async
from Models.product import OC_Product
from config import tortoise_db_config, logger
import asyncio

if __name__ == '__main__':
    logger.info("Starting")
    async def init_db():
        await Tortoise.init(
            config=tortoise_db_config
        )
        await Tortoise.generate_schemas()

run_async(init_db())