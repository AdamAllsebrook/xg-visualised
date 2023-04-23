from rocketry import Rocketry
from rocketry.conds import every
from app.data.update import update_cache

# Creating the Rocketry app
app = Rocketry(config={"task_execution": "async"})


@app.task(every("1 hour"))
async def update_cache_task():
    await update_cache()


if __name__ == "__main__":
    app.run()
