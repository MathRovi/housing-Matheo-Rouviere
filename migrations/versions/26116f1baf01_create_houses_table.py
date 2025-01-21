from alembic import op
import sqlalchemy as sa

# Révision ID et dépendances
revision = 'xxxx_create_houses_table'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'houses',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('longitude', sa.Float, nullable=False),
        sa.Column('latitude', sa.Float, nullable=False),
        sa.Column('housing_median_age', sa.Float, nullable=False),
        sa.Column('total_rooms', sa.Integer, nullable=False),
        sa.Column('total_bedrooms', sa.Integer, nullable=False),
        sa.Column('population', sa.Integer, nullable=False),
        sa.Column('households', sa.Integer, nullable=False),
        sa.Column('median_income', sa.Float, nullable=False),
        sa.Column('median_house_value', sa.Float, nullable=False),
        sa.Column('ocean_proximity', sa.String(255), nullable=False),
    )

def downgrade():
    op.drop_table('houses')
