from apscheduler.schedulers.asyncio import AsyncIOScheduler
from core.logger import logger

class SchedulerService:
    def __init__(self):
        self.scheduler = AsyncIOScheduler()
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.scheduler.start()
            self.is_running = True
            logger.info("Background scheduler started.")

    def shutdown(self):
        if self.is_running:
            self.scheduler.shutdown()
            self.is_running = False
            logger.info("Background scheduler stopped.")

    def get_status(self) -> str:
        return "running" if self.is_running else "stopped"

    def schedule_daily_task(self):
        # Example periodic task to run every day at midnight
        pass

scheduler_service = SchedulerService()
