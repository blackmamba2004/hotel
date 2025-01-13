from typing import Any, Callable, Optional

class Stub:
    """
    Класс-заглушка для инъекции зависимостей
    """
    def __init__(self, dependency: Callable[..., Any]) -> None:
        """Сохраняем нашу абстракцию."""
        self._dependency = dependency

    def __call__(self) -> None:
        """Выкинем ошибку, если забыли подменить реализацию при старте приложения."""
        raise NotImplementedError(f"You forgot to register `{self._dependency}` implementation.")

    def __hash__(self) -> int:
        """Обманываем app.dependency_overrides, чтобы он считал Stub реальной зависимостью"""
        return hash(self._dependency)

    def __eq__(self, __value: object) -> bool:
        """Обманываем app.dependency_overrides, чтобы он считал Stub реальной зависимостью"""
        if isinstance(__value, Stub):
            return self._dependency == __value._dependency
        else:
            return self._dependency == __value
