import logging
from pathlib import Path
import pandas as pd

# 1) Custom Exception Classes
class DataError(Exception):
    """Base class for all data-related errors."""
    pass


class DataFileNotFoundError(DataError):
    """Raised when the CSV file does not exist."""
    def __init__(self, path: Path):
        super().__init__(f"CSV file not found at path: {path}")


class MissingColumnError(DataError):
    """Raised when required columns are missing from the CSV."""
    def __init__(self, missing_columns: list[str]):
        super().__init__(f"Missing required column(s): {missing_columns}")


class InvalidAmountError(DataError):
    """Raised when 'amount' contains invalid or negative numbers."""
    def __init__(self, bad_rows_count: int):
        super().__init__(f"Found {bad_rows_count} invalid amount row(s) (must be numeric and >= 0).")

# 2) Logging Setup (Replaces print statements)
def setup_logging(log_file: str = "app.log") -> logging.Logger:
    logger = logging.getLogger("sales_app")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    # Log format: Time | Level | App Name | Message
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")

    # Console output (Terminal)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File output (saves to app.log)
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


logger = setup_logging()

REQUIRED_COLUMNS = ["order_id", "city", "category", "amount"]

# 3) Load & Validate Function
def load_and_validate(csv_path: Path) -> pd.DataFrame:
    logger.info("Attempting to load file from: %s", csv_path)

    # Check 1: Does file exist?
    if not csv_path.exists():
        raise DataFileNotFoundError(csv_path)

    logger.info("File found successfully! Loading CSV...")
    df = pd.read_csv(csv_path)

    # Check 2: Are required columns present?
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise MissingColumnError(missing)

    # Check 3: Is 'amount' valid numeric and >= 0?
    amount_numeric = pd.to_numeric(df["amount"], errors="coerce")
    bad_mask = amount_numeric.isna() | (amount_numeric < 0)
    bad_count = int(bad_mask.sum())

    if bad_count > 0:
        raise InvalidAmountError(bad_count)

    df["amount"] = amount_numeric
    return df

# 4) Main Execution
def main():
    # PATH FIX: Go up from "Task" to "Day 5", then into "Data" -> "sales.csv"
    csv_path = Path(__file__).resolve().parent.parent / "Data" / "sales.csv"

    logger.info("--- Starting Sales Processing Script ---")

    try:
        df = load_and_validate(csv_path)

        # Process & compute summary
        summary = (
            df.groupby("city")["amount"]
            .agg(["count", "sum", "mean"])
            .sort_values("sum", ascending=False)
        )

        logger.info("Processing complete. City Summary:\n\n%s\n", summary)

    # Catch custom data errors and log them as exceptions
    except DataError as e:
        logger.exception("Data processing stopped due to a DataError: %s", e)

    # Catch any other unexpected python errors
    except Exception as e:
        logger.exception("An unexpected error occurred: %s", e)


if __name__ == "__main__":
    main()