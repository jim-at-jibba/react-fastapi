import datetime as dt

import database as database
import passlib.hash as hash
import sqlalchemy as sql
import sqlalchemy.orm as orm


class User(database.Base):
    __tablename__ = "users"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    email = sql.Column(sql.String, unique=True, index=True)
    hashed_password = sql.Column(sql.String)

    leads = orm.relationship("Lead", back_populates="owner")

    def verify_password(self, password: str):
        return hash.bcrypt.verify(password, self.hashed_password)


class Lead(database.Base):
    __tablename__ = "leads"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    owner_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    first_name = sql.Column(sql.String, index=True)
    last_name = sql.Column(sql.String, index=True)
    email = sql.Column(sql.String, index=True)
    company = sql.Column(sql.String, index=True, default="")
    note = sql.Column(sql.String, default="")
    date_created = sql.Column(sql.DateTime, default=dt.datetime.utcnow)
    date_last_updated = sql.Column(sql.DateTime, default=dt.datetime.utcnow)

    owner = orm.relationship("User", back_populates="leads")
