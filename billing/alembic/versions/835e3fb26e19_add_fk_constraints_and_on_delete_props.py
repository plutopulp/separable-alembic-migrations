"""Add FK constraints and on delete props

Revision ID: 835e3fb26e19
Revises: 205678aa4a47
Create Date: 2023-05-30 09:53:52.599983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "835e3fb26e19"
down_revision = "205678aa4a47"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        op.f("ix_billing_user_subscription_user_id"),
        "user_subscription",
        ["user_id"],
        unique=False,
        schema="billing",
    )
    op.drop_constraint(
        "fk_user_subscription_user",
        "user_subscription",
        schema="billing",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_user_subscription_user",
        "user_subscription",
        "user",
        ["user_id"],
        ["id"],
        source_schema="billing",
        referent_schema="auth",
        ondelete="CASCADE",
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
    op.create_foreign_key(
        "fk_user_subscription_user",
        "user_subscription",
        "user",
        ["user_id"],
        ["id"],
        source_schema="billing",
        referent_schema="auth",
    )
    op.drop_index(
        op.f("ix_billing_user_subscription_user_id"),
        table_name="user_subscription",
        schema="billing",
    )
    # ### end Alembic commands ###
