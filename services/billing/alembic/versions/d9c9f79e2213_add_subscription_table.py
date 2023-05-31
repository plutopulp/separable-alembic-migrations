"""add subscription table

Revision ID: d9c9f79e2213
Revises: 
Create Date: 2023-05-26 13:58:54.804314

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "d9c9f79e2213"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "subscription",
        sa.Column("category", sa.String(length=64), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.Column("id", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        schema="billing",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("subscription", schema="billing")
    # ### end Alembic commands ###