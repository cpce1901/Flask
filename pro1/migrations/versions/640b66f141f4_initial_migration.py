"""Initial migration.

Revision ID: 640b66f141f4
Revises: 
Create Date: 2023-04-28 01:52:00.806318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '640b66f141f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Medidas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('v1', sa.Float(), nullable=True),
    sa.Column('v2', sa.Float(), nullable=True),
    sa.Column('v3', sa.Float(), nullable=True),
    sa.Column('v13', sa.Float(), nullable=True),
    sa.Column('v12', sa.Float(), nullable=True),
    sa.Column('v23', sa.Float(), nullable=True),
    sa.Column('i1', sa.Float(), nullable=True),
    sa.Column('i2', sa.Float(), nullable=True),
    sa.Column('i3', sa.Float(), nullable=True),
    sa.Column('p1', sa.Float(), nullable=True),
    sa.Column('p2', sa.Float(), nullable=True),
    sa.Column('p3', sa.Float(), nullable=True),
    sa.Column('pa', sa.Float(), nullable=True),
    sa.Column('fp', sa.Float(), nullable=True),
    sa.Column('hz', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('Sensor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('numero_sensor', sa.Integer(), nullable=True),
    sa.Column('numero_sensor_id', sa.Integer(), nullable=True),
    sa.Column('ubicación', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['numero_sensor_id'], ['Medidas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Equipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('marca', sa.String(length=32), nullable=True),
    sa.Column('modelo', sa.String(length=32), nullable=True),
    sa.Column('modelo_id', sa.Integer(), nullable=True),
    sa.Column('image', sa.LargeBinary(), nullable=True),
    sa.ForeignKeyConstraint(['modelo_id'], ['Sensor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Equipo')
    op.drop_table('Sensor')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    op.drop_table('Medidas')
    # ### end Alembic commands ###
