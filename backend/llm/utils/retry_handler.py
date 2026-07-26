import time
from typing import Callable, TypeVar

T = TypeVar("T")


class RetryHandler:

    @staticmethod
    def execute(
        operation: Callable[[], T],
        max_retries: int = 3,
        wait_seconds: int = 20,
    ) -> T:

        last_error = None

        for attempt in range(1, max_retries + 1):

            try:
                return operation()

            except Exception as ex:

                last_error = ex
                message = str(ex).lower()

                # Don't retry if the request is invalid
                if (
                    "404" in message
                    or "not_found" in message
                    or "permission_denied" in message
                    or "invalid_argument" in message
                ):
                    raise ex

                # Retry only transient failures
                if (
                    "429" in message
                    or "rate_limit" in message
                    or "resource_exhausted" in message
                    or "503" in message
                    or "500" in message
                ):

                    if attempt < max_retries:

                        print(
                            f"Retry {attempt}/{max_retries} "
                            f"after {wait_seconds} seconds..."
                        )

                        time.sleep(wait_seconds)
                        continue

                raise ex

        raise last_error