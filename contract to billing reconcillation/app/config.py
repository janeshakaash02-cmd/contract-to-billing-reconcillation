import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CONTRACTS_DIR = DATA_DIR / "contracts"
INVOICES_DIR = DATA_DIR / "invoices"
POLICIES_DIR = DATA_DIR / "policies"
CHROMA_PERSIST_DIR = Path(os.getenv("CHROMA_PERSIST_DIR", str(DATA_DIR / "chromadb")))
DB_PATH = Path(os.getenv("DB_PATH", str(DATA_DIR / "reconciliation.db")))

# Ensure directories exist
CONTRACTS_DIR.mkdir(parents=True, exist_ok=True)
INVOICES_DIR.mkdir(parents=True, exist_ok=True)
POLICIES_DIR.mkdir(parents=True, exist_ok=True)
CHROMA_PERSIST_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# LLM & Embedding Settings
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "demo").lower()
LLM_API_KEY = os.getenv("LLM_API_KEY", "")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o-mini")

EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER", "demo").lower()
EMBEDDING_API_KEY = os.getenv("EMBEDDING_API_KEY", "")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

# Business Logic Defaults
DEFAULT_TOLERANCE_PERCENT = float(os.getenv("DEFAULT_TOLERANCE_PERCENT", "1.0"))  # 1%
DEFAULT_TOLERANCE_ABSOLUTE = float(os.getenv("DEFAULT_TOLERANCE_ABSOLUTE", "50.0"))  # $50
DATE_TOLERANCE_DAYS = int(os.getenv("DATE_TOLERANCE_DAYS", "3"))

# Operational / ROI Assumptions
MANUAL_MINUTES_PER_INVOICE = 15.0  # Industry standard time to manually check contract & invoice
FINANCE_HOURLY_COST = 45.0  # Blended finance specialist rate ($/hr)
