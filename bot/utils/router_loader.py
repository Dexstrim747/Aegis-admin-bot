import importlib
import pkgutil

from aiogram import Dispatcher


def register_all_routers(dp: Dispatcher):
    package = "bot.handlers"

    for _, module_name, _ in pkgutil.iter_modules(["bot/handlers"]):
        if module_name == "__init__":
            continue

        module = importlib.import_module(f"{package}.{module_name}")

        if hasattr(module, "router"):
            dp.include_router(module.router)