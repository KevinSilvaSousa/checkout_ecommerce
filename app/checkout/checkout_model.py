from enum import Enum

from sqlalchemy import Column, DateTime, Integer, String, Float

from datetime import datetime, timezone

from app.infra.database import Base



class CheckoutStatus(Enum):
    PENDING = "pending"
    SUCCESS = "success"
    PROCESSING_PAYMENT = "processing_payment"
    CREATING_ORDER = "creating_order"
    FAILED = "failed"




class Checkout(Base):
    __tablename__ = "checkouts"


    id = Column (Integer, primary_key=True, autoincrement=True)
    customer_email = Column(String(128), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    payment_id = Column(String(64), nullable=True)
    order_id = Column (String(64), nullable=True)
    status = Column (String(24), default=CheckoutStatus.PENDING.value, nullable=False)
    error = Column(String, nullable=True)
    total_amount = Column(Float, nullable=False)
