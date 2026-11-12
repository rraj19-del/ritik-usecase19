import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
LANDING_DIR = DATA_DIR / "landing"
PROFILES_DIR = DATA_DIR / "profiles"
STTM_DIR = DATA_DIR / "sttm"
BRONZE_DIR = DATA_DIR / "bronze_layer"
SILVER_DIR = DATA_DIR / "silver_layer"
GOLD_DIR = DATA_DIR / "gold_layer"
REPORTS_DIR = BASE_DIR / "reports"
AUDIT_DIR = BASE_DIR / "audit_logs"
CHROMA_DIR = BASE_DIR / ".chroma"

# ---------------------------------------------------------------------------
# LLM configuration
# ---------------------------------------------------------------------------

# Anthropic (Claude) - primary provider
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-5-5")

# Legacy providers (kept so other files that import these don't break)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
GEMINI_MODEL = "gemini-2.5-flash"
EMBEDDING_MODEL = "models/text-embedding-004"

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL = "llama-3.3-70b-versatile"

# Provider selection: explicit LLM_PROVIDER wins, otherwise Claude if a key exists
_env_llm = os.getenv("LLM_PROVIDER", "").strip().lower()
if _env_llm in ("claude", "groq", "gemini"):
    LLM_PROVIDER = _env_llm
elif ANTHROPIC_API_KEY:
    LLM_PROVIDER = "claude"
elif GROQ_API_KEY:
    LLM_PROVIDER = "groq"
else:
    LLM_PROVIDER = "gemini"

# Ensure directories exist
for d in [LANDING_DIR, PROFILES_DIR, STTM_DIR, BRONZE_DIR, SILVER_DIR, GOLD_DIR, REPORTS_DIR, AUDIT_DIR, CHROMA_DIR]:
    d.mkdir(parents=True, exist_ok=True)