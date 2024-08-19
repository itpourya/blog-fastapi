from uuid import UUID, uuid4
from sqlalchemy.orm import Mapped, mapped_column
from database.engine import Base


class User(Base):
    __tablename__ = "users"

    password: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column(unique=True)
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column(unique=True)
    active: Mapped[bool] = mapped_column()

    id: Mapped[UUID] = mapped_column(primary_key=True, default_factory=uuid4)
