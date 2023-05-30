"""add user id FK

Revision ID: 205678aa4a47
Revises: cbe514674831
Create Date: 2023-05-30 09:37:06.356635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "205678aa4a47"
down_revision = "cbe514674831"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(
        "fk_user_subscription_user",
        "user_subscription",
        "user",
        ["user_id"],
        ["id"],
        source_schema="billing",
        referent_schema="auth",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "fk_user_subscription_user",
        "user_subscription",
        schema="billing",
        type_="foreignkey",
    )
    # ### end Alembic commands ###
