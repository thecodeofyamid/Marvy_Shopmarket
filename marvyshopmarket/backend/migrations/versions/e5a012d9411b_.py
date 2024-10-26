"""empty message

Revision ID: e5a012d9411b
Revises: 
Create Date: 2024-10-26 19:09:23.557825

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e5a012d9411b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wp_termmeta')
    op.drop_table('productos')
    op.drop_table('factura')
    op.drop_table('tiendas')
    op.drop_table('tenderos')
    op.drop_table('wp_terms')
    op.drop_table('wp_postmeta')
    op.drop_table('ventas')
    op.drop_table('ventas_has_productos')
    op.drop_table('caja')
    op.drop_table('wp_term_relationships')
    with op.batch_alter_table('wp_users', schema=None) as batch_op:
        batch_op.drop_index('user_login_key')

    op.drop_table('wp_users')
    with op.batch_alter_table('wp_posts', schema=None) as batch_op:
        batch_op.drop_index('type_status_date')

    op.drop_table('wp_posts')
    op.drop_table('wp_usermeta')
    with op.batch_alter_table('wp_comments', schema=None) as batch_op:
        batch_op.drop_index('comment_approved_date_gmt')

    op.drop_table('wp_comments')
    op.drop_table('informe')
    op.drop_table('suministros_has_proveedores')
    op.drop_table('wp_commentmeta')
    op.drop_table('administrador')
    op.drop_table('wp_links')
    op.drop_table('suministros')
    with op.batch_alter_table('wp_term_taxonomy', schema=None) as batch_op:
        batch_op.drop_index('term_id_taxonomy')

    op.drop_table('wp_term_taxonomy')
    op.drop_table('proveedores')
    with op.batch_alter_table('wp_options', schema=None) as batch_op:
        batch_op.drop_index('option_name')

    op.drop_table('wp_options')
    op.drop_table('gastos')
    op.drop_table('suministros_has_productos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('suministros_has_productos',
    sa.Column('suministros_sum_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('suministros_tienda_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('productos_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('productos_tendero_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('productos_tienda_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['productos_Id', 'productos_tendero_Id', 'productos_tienda_Id'], ['productos.Id', 'productos.tendero_Id', 'productos.tienda_Id'], name='suministros_has_productos_ibfk_2'),
    sa.ForeignKeyConstraint(['suministros_sum_Id'], ['suministros.sum_Id'], name='fk_sum_Id'),
    sa.PrimaryKeyConstraint('suministros_sum_Id', 'suministros_tienda_Id', 'productos_Id', 'productos_tendero_Id', 'productos_tienda_Id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('gastos',
    sa.Column('gastos_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('gastos_Descr', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('gastos_Tipo', mysql.VARCHAR(length=45), nullable=True),
    sa.Column('gastos_Precio', mysql.FLOAT(), nullable=True),
    sa.Column('tienda_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['tienda_Id'], ['tiendas.tienda_Id'], name='gastos_ibfk_1'),
    sa.PrimaryKeyConstraint('gastos_Id', 'tienda_Id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('wp_options',
    sa.Column('option_id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('option_name', mysql.VARCHAR(length=191), server_default=sa.text("''"), nullable=False),
    sa.Column('option_value', mysql.LONGTEXT(), nullable=False),
    sa.Column('autoload', mysql.VARCHAR(length=20), server_default=sa.text("'yes'"), nullable=False),
    sa.PrimaryKeyConstraint('option_id'),
    mysql_collate='utf8mb4_unicode_520_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('wp_options', schema=None) as batch_op:
        batch_op.create_index('option_name', ['option_name'], unique=False)

    op.create_table('proveedores',
    sa.Column('id', mysql.BIGINT(display_width=20), autoincrement=True, nullable=False),
    sa.Column('prov_Id', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('prov_Nombre', mysql.VARCHAR(length=70), nullable=True),
    sa.Column('prov_Ubicacion', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('prov_Contacto', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('prov_prod_nom', mysql.VARCHAR(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('wp_term_taxonomy',
    sa.Column('term_taxonomy_id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('term_id', mysql.BIGINT(display_width=20, unsigned=True), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('taxonomy', mysql.VARCHAR(length=32), server_default=sa.text("''"), nullable=False),
    sa.Column('description', mysql.LONGTEXT(), nullable=False),
    sa.Column('parent', mysql.BIGINT(display_width=20, unsigned=True), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('count', mysql.BIGINT(display_width=20), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('term_taxonomy_id'),
    mysql_collate='utf8mb4_unicode_520_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('wp_term_taxonomy', schema=None) as batch_op:
        batch_op.create_index('term_id_taxonomy', ['term_id', 'taxonomy'], unique=False)

    op.create_table('suministros',
    sa.Column('sum_Id', mysql.BIGINT(display_width=20), autoincrement=True, nullable=False),
    sa.Column('sum_prod_Nom', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('sum_Cantidad', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('sum_Datetime', mysql.DATETIME(), nullable=True),
    sa.Column('sum_Metodo_pago', mysql.VARCHAR(length=45), nullable=True),
    sa.Column('sum_Total', mysql.FLOAT(), nullable=True),
    sa.Column('tienda_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['tienda_Id'], ['tiendas.tienda_Id'], name='suministros_ibfk_1'),
    sa.PrimaryKeyConstraint('sum_Id', 'tienda_Id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('wp_links',
    sa.Column('link_id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('link_url', mysql.VARCHAR(length=255), server_default=sa.text("''"), nullable=False),
    sa.Column('link_name', mysql.VARCHAR(length=255), server_default=sa.text("''"), nullable=False),
    sa.Column('link_image', mysql.VARCHAR(length=255), server_default=sa.text("''"), nullable=False),
    sa.Column('link_target', mysql.VARCHAR(length=25), server_default=sa.text("''"), nullable=False),
    sa.Column('link_description', mysql.VARCHAR(length=255), server_default=sa.text("''"), nullable=False),
    sa.Column('link_visible', mysql.VARCHAR(length=20), server_default=sa.text("'Y'"), nullable=False),
    sa.Column('link_owner', mysql.BIGINT(display_width=20, unsigned=True), server_default=sa.text('1'), autoincrement=False, nullable=False),
    sa.Column('link_rating', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('link_updated', mysql.DATETIME(), server_default=sa.text("'0000-00-00 00:00:00'"), nullable=False),
    sa.Column('link_rel', mysql.VARCHAR(length=255), server_default=sa.text("''"), nullable=False),
    sa.Column('link_notes', mysql.MEDIUMTEXT(), nullable=False),
    sa.Column('link_rss', mysql.VARCHAR(length=255), server_default=sa.text("''"), nullable=False),
    sa.PrimaryKeyConstraint('link_id'),
    mysql_collate='utf8mb4_unicode_520_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('administrador',
    sa.Column('adm_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('adm_Nombre', mysql.VARCHAR(length=70), nullable=True),
    sa.Column('adm_Correo', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('adm_Celular', mysql.VARCHAR(length=12), nullable=True),
    sa.Column('adm_Password', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('tienda_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['tienda_Id'], ['tiendas.tienda_Id'], name='administrador_ibfk_1'),
    sa.PrimaryKeyConstraint('adm_Id', 'tienda_Id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('wp_commentmeta',
    sa.Column('meta_id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('comment_id', mysql.BIGINT(display_width=20, unsigned=True), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('meta_key', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('meta_value', mysql.LONGTEXT(), nullable=True),
    sa.PrimaryKeyConstraint('meta_id'),
    mysql_collate='utf8mb4_unicode_520_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('suministros_has_proveedores',
    sa.Column('Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('sum_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('tienda_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('prov_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['prov_Id'], ['proveedores.id'], name='suministros_has_proveedores_ibfk_1'),
    sa.PrimaryKeyConstraint('Id', 'sum_Id', 'tienda_Id', 'prov_Id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('informe',
    sa.Column('inf_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('inf_Datetime', mysql.DATETIME(), nullable=True),
    sa.Column('inf_Tipo', mysql.VARCHAR(length=45), nullable=True),
    sa.Column('inf_Doc', mysql.LONGBLOB(), nullable=True),
    sa.Column('tienda_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['tienda_Id'], ['tiendas.tienda_Id'], name='informe_ibfk_1'),
    sa.PrimaryKeyConstraint('inf_Id', 'tienda_Id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('wp_comments',
    sa.Column('comment_ID', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('comment_post_ID', mysql.BIGINT(display_width=20, unsigned=True), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('comment_author', mysql.TINYTEXT(), nullable=False),
    sa.Column('comment_author_email', mysql.VARCHAR(length=100), server_default=sa.text("''"), nullable=False),
    sa.Column('comment_author_url', mysql.VARCHAR(length=200), server_default=sa.text("''"), nullable=False),
    sa.Column('comment_author_IP', mysql.VARCHAR(length=100), server_default=sa.text("''"), nullable=False),
    sa.Column('comment_date', mysql.DATETIME(), server_default=sa.text("'0000-00-00 00:00:00'"), nullable=False),
    sa.Column('comment_date_gmt', mysql.DATETIME(), server_default=sa.text("'0000-00-00 00:00:00'"), nullable=False),
    sa.Column('comment_content', mysql.TEXT(), nullable=False),
    sa.Column('comment_karma', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('comment_approved', mysql.VARCHAR(length=20), server_default=sa.text("'1'"), nullable=False),
    sa.Column('comment_agent', mysql.VARCHAR(length=255), server_default=sa.text("''"), nullable=False),
    sa.Column('comment_type', mysql.VARCHAR(length=20), server_default=sa.text("'comment'"), nullable=False),
    sa.Column('comment_parent', mysql.BIGINT(display_width=20, unsigned=True), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('user_id', mysql.BIGINT(display_width=20, unsigned=True), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('comment_ID'),
    mysql_collate='utf8mb4_unicode_520_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('wp_comments', schema=None) as batch_op:
        batch_op.create_index('comment_approved_date_gmt', ['comment_approved', 'comment_date_gmt'], unique=False)

    op.create_table('wp_usermeta',
    sa.Column('umeta_id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.BIGINT(display_width=20, unsigned=True), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('meta_key', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('meta_value', mysql.LONGTEXT(), nullable=True),
    sa.PrimaryKeyConstraint('umeta_id'),
    mysql_collate='utf8mb4_unicode_520_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('wp_posts',
    sa.Column('ID', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('post_author', mysql.BIGINT(display_width=20, unsigned=True), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('post_date', mysql.DATETIME(), server_default=sa.text("'0000-00-00 00:00:00'"), nullable=False),
    sa.Column('post_date_gmt', mysql.DATETIME(), server_default=sa.text("'0000-00-00 00:00:00'"), nullable=False),
    sa.Column('post_content', mysql.LONGTEXT(), nullable=False),
    sa.Column('post_title', mysql.TEXT(), nullable=False),
    sa.Column('post_excerpt', mysql.TEXT(), nullable=False),
    sa.Column('post_status', mysql.VARCHAR(length=20), server_default=sa.text("'publish'"), nullable=False),
    sa.Column('comment_status', mysql.VARCHAR(length=20), server_default=sa.text("'open'"), nullable=False),
    sa.Column('ping_status', mysql.VARCHAR(length=20), server_default=sa.text("'open'"), nullable=False),
    sa.Column('post_password', mysql.VARCHAR(length=255), server_default=sa.text("''"), nullable=False),
    sa.Column('post_name', mysql.VARCHAR(length=200), server_default=sa.text("''"), nullable=False),
    sa.Column('to_ping', mysql.TEXT(), nullable=False),
    sa.Column('pinged', mysql.TEXT(), nullable=False),
    sa.Column('post_modified', mysql.DATETIME(), server_default=sa.text("'0000-00-00 00:00:00'"), nullable=False),
    sa.Column('post_modified_gmt', mysql.DATETIME(), server_default=sa.text("'0000-00-00 00:00:00'"), nullable=False),
    sa.Column('post_content_filtered', mysql.LONGTEXT(), nullable=False),
    sa.Column('post_parent', mysql.BIGINT(display_width=20, unsigned=True), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('guid', mysql.VARCHAR(length=255), server_default=sa.text("''"), nullable=False),
    sa.Column('menu_order', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('post_type', mysql.VARCHAR(length=20), server_default=sa.text("'post'"), nullable=False),
    sa.Column('post_mime_type', mysql.VARCHAR(length=100), server_default=sa.text("''"), nullable=False),
    sa.Column('comment_count', mysql.BIGINT(display_width=20), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('ID'),
    mysql_collate='utf8mb4_unicode_520_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('wp_posts', schema=None) as batch_op:
        batch_op.create_index('type_status_date', ['post_type', 'post_status', 'post_date', 'ID'], unique=False)

    op.create_table('wp_users',
    sa.Column('ID', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('user_login', mysql.VARCHAR(length=60), server_default=sa.text("''"), nullable=False),
    sa.Column('user_pass', mysql.VARCHAR(length=255), server_default=sa.text("''"), nullable=False),
    sa.Column('user_nicename', mysql.VARCHAR(length=50), server_default=sa.text("''"), nullable=False),
    sa.Column('user_email', mysql.VARCHAR(length=100), server_default=sa.text("''"), nullable=False),
    sa.Column('user_url', mysql.VARCHAR(length=100), server_default=sa.text("''"), nullable=False),
    sa.Column('user_registered', mysql.DATETIME(), server_default=sa.text("'0000-00-00 00:00:00'"), nullable=False),
    sa.Column('user_activation_key', mysql.VARCHAR(length=255), server_default=sa.text("''"), nullable=False),
    sa.Column('user_status', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('display_name', mysql.VARCHAR(length=250), server_default=sa.text("''"), nullable=False),
    sa.PrimaryKeyConstraint('ID'),
    mysql_collate='utf8mb4_unicode_520_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('wp_users', schema=None) as batch_op:
        batch_op.create_index('user_login_key', ['user_login'], unique=False)

    op.create_table('wp_term_relationships',
    sa.Column('object_id', mysql.BIGINT(display_width=20, unsigned=True), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('term_taxonomy_id', mysql.BIGINT(display_width=20, unsigned=True), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('term_order', mysql.INTEGER(display_width=11), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('object_id', 'term_taxonomy_id'),
    mysql_collate='utf8mb4_unicode_520_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('caja',
    sa.Column('caja_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('caja_Ingresos', mysql.FLOAT(), nullable=True),
    sa.Column('caja_Egresos', mysql.FLOAT(), nullable=True),
    sa.Column('caja_Total', mysql.FLOAT(), nullable=True),
    sa.Column('tienda_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['tienda_Id'], ['tiendas.tienda_Id'], name='caja_ibfk_1'),
    sa.PrimaryKeyConstraint('caja_Id', 'tienda_Id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('ventas_has_productos',
    sa.Column('ventas_venta_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('ventas_tendero_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('ventas_tienda_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('productos_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('productos_tendero_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('productos_tienda_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['productos_Id', 'productos_tendero_Id', 'productos_tienda_Id'], ['productos.Id', 'productos.tendero_Id', 'productos.tienda_Id'], name='ventas_has_productos_ibfk_2'),
    sa.ForeignKeyConstraint(['ventas_venta_Id', 'ventas_tendero_Id', 'ventas_tienda_Id'], ['ventas.venta_Id', 'ventas.tendero_Id', 'ventas.tienda_Id'], name='ventas_has_productos_ibfk_1'),
    sa.PrimaryKeyConstraint('ventas_venta_Id', 'ventas_tendero_Id', 'ventas_tienda_Id', 'productos_Id', 'productos_tendero_Id', 'productos_tienda_Id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('ventas',
    sa.Column('venta_Id', mysql.BIGINT(display_width=20), autoincrement=True, nullable=False),
    sa.Column('venta_Cantidad', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('venta_Metodo', mysql.VARCHAR(length=45), nullable=True),
    sa.Column('venta_Datetime', mysql.DATETIME(), nullable=True),
    sa.Column('venta_Total', mysql.FLOAT(), nullable=True),
    sa.Column('venta_Pago', mysql.FLOAT(), nullable=True),
    sa.Column('venta_Vueltos', mysql.FLOAT(), nullable=True),
    sa.Column('tendero_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('tienda_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['tendero_Id', 'tienda_Id'], ['tenderos.tendero_Id', 'tenderos.tienda_Id'], name='ventas_ibfk_1'),
    sa.PrimaryKeyConstraint('venta_Id', 'tendero_Id', 'tienda_Id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('wp_postmeta',
    sa.Column('meta_id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('post_id', mysql.BIGINT(display_width=20, unsigned=True), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('meta_key', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('meta_value', mysql.LONGTEXT(), nullable=True),
    sa.PrimaryKeyConstraint('meta_id'),
    mysql_collate='utf8mb4_unicode_520_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('wp_terms',
    sa.Column('term_id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=200), server_default=sa.text("''"), nullable=False),
    sa.Column('slug', mysql.VARCHAR(length=200), server_default=sa.text("''"), nullable=False),
    sa.Column('term_group', mysql.BIGINT(display_width=20), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('term_id'),
    mysql_collate='utf8mb4_unicode_520_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('tenderos',
    sa.Column('tendero_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('tendero_Nombre', mysql.VARCHAR(length=70), nullable=True),
    sa.Column('tendero_Correo', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('tendero_Celular', mysql.VARCHAR(length=12), nullable=True),
    sa.Column('tendero_Password', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('tienda_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['tienda_Id'], ['tiendas.tienda_Id'], name='tenderos_ibfk_1'),
    sa.PrimaryKeyConstraint('tendero_Id', 'tienda_Id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('tiendas',
    sa.Column('tienda_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('tienda_Nombre', mysql.VARCHAR(length=70), nullable=True),
    sa.Column('tienda_Correo', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('tienda_Celular', mysql.VARCHAR(length=12), nullable=True),
    sa.Column('tienda_Ubicacion', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('tienda_Img', mysql.LONGBLOB(), nullable=True),
    sa.PrimaryKeyConstraint('tienda_Id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('factura',
    sa.Column('fac_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('fac_Datetime', mysql.DATETIME(), nullable=True),
    sa.Column('fac_Tipo', mysql.VARCHAR(length=45), nullable=True),
    sa.Column('tienda_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['tienda_Id'], ['tiendas.tienda_Id'], name='factura_ibfk_1'),
    sa.PrimaryKeyConstraint('fac_Id', 'tienda_Id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('productos',
    sa.Column('Id', mysql.BIGINT(display_width=20), autoincrement=True, nullable=False),
    sa.Column('prod_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=True),
    sa.Column('prod_Nombre', mysql.VARCHAR(length=70), nullable=True),
    sa.Column('prod_Precio', mysql.FLOAT(), nullable=True),
    sa.Column('prod_Ganancia', mysql.FLOAT(), nullable=True),
    sa.Column('prod_TotalPrecio', mysql.FLOAT(), sa.Computed('(`prod_Precio` * (`prod_Ganancia` / 100) + `prod_Precio`)', persisted=False), nullable=True),
    sa.Column('prod_Cantidad', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('prod_Categoria', mysql.VARCHAR(length=45), nullable=True),
    sa.Column('prod_Total', mysql.FLOAT(), sa.Computed('(`prod_Precio` * `prod_Cantidad`)', persisted=False), nullable=True),
    sa.Column('prod_TotalGana', mysql.FLOAT(), sa.Computed('(`prod_TotalPrecio` * `prod_Cantidad`)', persisted=False), nullable=True),
    sa.Column('prod_Img', mysql.LONGBLOB(), nullable=True),
    sa.Column('tendero_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.Column('tienda_Id', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['tendero_Id', 'tienda_Id'], ['tenderos.tendero_Id', 'tenderos.tienda_Id'], name='productos_ibfk_1'),
    sa.PrimaryKeyConstraint('Id', 'tendero_Id', 'tienda_Id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('wp_termmeta',
    sa.Column('meta_id', mysql.BIGINT(display_width=20, unsigned=True), autoincrement=True, nullable=False),
    sa.Column('term_id', mysql.BIGINT(display_width=20, unsigned=True), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('meta_key', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('meta_value', mysql.LONGTEXT(), nullable=True),
    sa.PrimaryKeyConstraint('meta_id'),
    mysql_collate='utf8mb4_unicode_520_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
