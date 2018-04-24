"""Updated databse schema to remove relationship conflicts

Revision ID: 2fd9a2f377d7
Revises: ee7aac058132
Create Date: 2018-04-24 16:42:28.836715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fd9a2f377d7'
down_revision = 'ee7aac058132'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('events_joiner_id_fkey', 'events', type_='foreignkey')
    op.drop_constraint('events_category_id_fkey', 'events', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('events_category_id_fkey', 'events', 'events', ['category_id'], ['id'])
    op.create_foreign_key('events_joiner_id_fkey', 'events', 'users', ['joiner_id'], ['id'])
    # ### end Alembic commands ###
