from grpc.aio import ServicerContext
from typing import Any, Optional, TypeVar, Callable

T = TypeVar("T")

def get_metadata_value(
    context: ServicerContext,
    key: str,
    default: Optional[T] = None,
    *,
    required: bool = False,
    cast: Optional[Callable[[str], T]] = None,
    strip_prefix: Optional[str] = None,
    logger=None,
) -> Optional[T]:
    """
    Args:
        context (ServicerContext): The gRPC context from which to extract metadata.
        key (str): The metadata key to retrieve (case-insensitive).
        default (Optional[T]): A default value to return if key is not found.
        required (bool): If True, raises ValueError if key is missing.
        cast (Callable[[str], T], optional): A function to cast the metadata value.
        strip_prefix (str, optional): If provided, strips this prefix from the value.
        logger (optional): Logger to use for warnings/errors.

    Returns:
        Optional[T]: The metadata value, casted if requested.

    Raises:
        ValueError: If required is True and key is missing.
        TypeError or ValueError: If cast fails.
    """
    try:
        metadata = context.invocation_metadata()
        metadata_dict = {k.lower(): v for k, v in (metadata or [])}

        raw_value = metadata_dict.get(key.lower())

        if raw_value is None:
            if required:
                raise ValueError(f"Missing required metadata key: '{key}'")
            return default

        # Optionally strip prefix (e.g. "Bearer ")
        if strip_prefix and raw_value.startswith(strip_prefix):
            raw_value = raw_value[len(strip_prefix):]

        # Optionally cast
        if cast:
            try:
                return cast(raw_value)
            except (ValueError, TypeError) as e:
                # logger.warning(f"Failed to cast metadata key '{key}' value '{raw_value}': {e}")
                if required:
                    raise
                return default

        return raw_value  # pyright: ignore[reportReturnType]

    except Exception as e:
        # logger.error(f"Error retrieving metadata key '{key}': {e}", exc_info=True)
        if required:
            raise
        return default
