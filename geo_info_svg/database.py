from sqlmodel import SQLModel, create_engine


engine = create_engine("postgresql://user:supersecret@db/db")


def create_tables():
    SQLModel.metadata.create_all(engine)
