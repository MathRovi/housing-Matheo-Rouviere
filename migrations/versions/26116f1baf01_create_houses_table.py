from alembic import op
import sqlalchemy as sa

revision = 'xxxx_create_houses_table'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'houses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('longitude', sa.Float),
        sa.Column('latitude', sa.Float),
        sa.Column('housing_median_age', sa.Integer),
        sa.Column('total_rooms', sa.Integer),
        sa.Column('total_bedrooms', sa.Integer),
        sa.Column('population', sa.Integer),
        sa.Column('households', sa.Integer),
        sa.Column('median_income', sa.Float),
        sa.Column('median_house_value', sa.Float),
        sa.Column('ocean_proximity', sa.String(50))
    )

def downgrade():
    op.drop_table('houses')
