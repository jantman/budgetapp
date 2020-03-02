"""new plaid models and schema

Revision ID: 48658aaee0b5
Revises: 5709a5bb198e
Create Date: 2020-03-02 17:52:43.354795

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql
from sqlalchemy_utc.sqltypes import UtcDateTime

# revision identifiers, used by Alembic.
revision = '48658aaee0b5'
down_revision = '5709a5bb198e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plaid_items',
    sa.Column('item_id', sa.String(length=70), nullable=False),
    sa.Column('token', sa.String(length=70), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('last_updated', UtcDateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint(
        'item_id', name=op.f('pk_plaid_items')), mysql_engine='InnoDB'
    )
    op.create_index(
        op.f('ix_plaid_items_name'), 'plaid_items', ['name'], unique=True
    )
    op.drop_column('accounts', 'plaid_account_id')
    op.drop_column('accounts', 'plaid_item_id')
    op.drop_column('accounts', 'plaid_token')
    op.drop_column('accounts', 'plaid_account_mask')
    op.drop_column('accounts', 'plaid_account_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'accounts',
        sa.Column('plaid_account_name', mysql.VARCHAR(length=70), nullable=True)
    )
    op.add_column(
        'accounts',
        sa.Column('plaid_account_mask', mysql.VARCHAR(length=70), nullable=True)
    )
    op.add_column(
        'accounts',
        sa.Column('plaid_token', mysql.VARCHAR(length=70), nullable=True)
    )
    op.add_column(
        'accounts',
        sa.Column('plaid_item_id', mysql.VARCHAR(length=70), nullable=True)
    )
    op.add_column(
        'accounts',
        sa.Column('plaid_account_id', mysql.VARCHAR(length=70), nullable=True)
    )
    op.drop_index(op.f('ix_plaid_items_name'), table_name='plaid_items')
    op.drop_table('plaid_items')
    # ### end Alembic commands ###