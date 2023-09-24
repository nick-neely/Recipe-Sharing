"""Changed ratings to allow 1 per user

Revision ID: eb2b02048894
Revises: 05705f91cca7
Create Date: 2023-09-23 18:40:46.485507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb2b02048894'
down_revision = '05705f91cca7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rating', schema=None) as batch_op:
        batch_op.create_unique_constraint('_user_recipe_uc', ['user_id', 'recipe_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rating', schema=None) as batch_op:
        batch_op.drop_constraint('_user_recipe_uc', type_='unique')

    # ### end Alembic commands ###