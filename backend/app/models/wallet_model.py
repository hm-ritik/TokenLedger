"""id (UUID, primary key): the public identifier of a wallet.
balance_paise (BIGINT, CHECK (balance_paise >= 0)): a cached balance, so reads don’t need a SUM over the ledger. The CHECK makes the database itself refuse a negative balance, even if your code has a bug.
created_at (timestamptz): audit.
This row is also what you lock with SELECT ... FOR UPDATE on Day 2, and that’s the reason the table exists."""


import uuid
from datetime import datetime, timezone
from app.core.database import Base

from sqlalchemy import BIGINT, DateTime , CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

class Wallet(Base):
    __tablename__ = "wallets"
    __table_args__ = (
        CheckConstraint("balance_paise >= 0", name="check_wallet_balance_non_negative"),
    )

    id: Mapped[uuid.UUID] = mapped_column( UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    balance_paise: Mapped[int] = mapped_column(BIGINT,nullable=False,default=0)
    created_at: Mapped[datetime] = mapped_column( DateTime(timezone=True),default=lambda: datetime.now(timezone.utc))
