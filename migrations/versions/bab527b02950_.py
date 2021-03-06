"""empty message

Revision ID: bab527b02950
Revises: 
Create Date: 2020-04-13 12:35:30.744743

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bab527b02950'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('address_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('address_line', sa.String(length=255), nullable=True),
    sa.Column('suburb_city', sa.String(length=255), nullable=True),
    sa.Column('state_area', sa.String(length=255), nullable=True),
    sa.Column('post_code', sa.String(length=20), nullable=True),
    sa.Column('country', sa.String(length=45), server_default=sa.text("'Australia'"), nullable=True),
    sa.Column('type', sa.String(length=45), nullable=True),
    sa.Column('users_user_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.PrimaryKeyConstraint('address_id', 'users_user_id')
    )
    op.create_table('asset_objects',
    sa.Column('asset_object_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('asset_table', sa.String(length=45), nullable=False),
    sa.Column('asset_target_id', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('assets_asset_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.PrimaryKeyConstraint('asset_object_id', 'assets_asset_id')
    )
    op.create_table('assets',
    sa.Column('asset_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('asset_name', sa.String(length=45), nullable=False),
    sa.Column('asset_hash', sa.String(length=255), nullable=False),
    sa.Column('type', sa.String(length=45), nullable=True),
    sa.Column('alt', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('asset_id')
    )
    op.create_table('audit_logs',
    sa.Column('audit_log_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('table', sa.String(length=45), nullable=False),
    sa.Column('table_id', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('action', sa.String(length=1), nullable=True, comment='C/U'),
    sa.Column('action_brief', sa.String(length=45), nullable=False),
    sa.Column('action_data', sa.Text(), nullable=True),
    sa.Column('action_by', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('action_at', sa.DateTime(), nullable=False),
    sa.Column('action_ip', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('audit_log_id')
    )
    op.create_table('brand_details',
    sa.Column('brand_detail_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('brands_brand_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('languages_language_id', mysql.INTEGER(display_width=2), nullable=False),
    sa.Column('brand_name', sa.String(length=255), nullable=False),
    sa.Column('brand_brief', sa.String(length=255), nullable=True),
    sa.Column('brand_description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('brand_detail_id', 'brands_brand_id', 'languages_language_id')
    )
    op.create_table('brands',
    sa.Column('brand_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('brand_url', sa.String(length=255), nullable=True),
    sa.Column('inactive', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('brand_id')
    )
    op.create_table('categories',
    sa.Column('category_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('parent_category', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('inactive', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('category_id')
    )
    op.create_table('categories_has_spec_groups',
    sa.Column('categories_category_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('spec_groups_spec_group_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.PrimaryKeyConstraint('categories_category_id', 'spec_groups_spec_group_id')
    )
    op.create_table('category_details',
    sa.Column('category_detail_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('categories_category_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('languages_language_id', mysql.INTEGER(display_width=2), nullable=False),
    sa.Column('category_name', sa.String(length=45), nullable=False),
    sa.Column('category_brief', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('category_detail_id', 'categories_category_id', 'languages_language_id')
    )
    op.create_table('delivery_methods',
    sa.Column('delivery_method_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('delivery_name', sa.String(length=45), nullable=True),
    sa.Column('delivery_charge', sa.DECIMAL(precision=10, scale=2), server_default=sa.text("'0.00'"), nullable=True),
    sa.Column('delivery_tracking_url', sa.String(length=255), nullable=True),
    sa.Column('inactive', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('delivery_method_id')
    )
    op.create_table('languages',
    sa.Column('language_id', mysql.INTEGER(display_width=2), nullable=False),
    sa.Column('language', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('language_id')
    )
    op.create_table('marketing_campaigns',
    sa.Column('marketing_campaign_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('coupon_code', sa.String(length=45), nullable=True),
    sa.Column('coupon_created_at', sa.DateTime(), nullable=False),
    sa.Column('coupon_expiry_date', sa.Date(), nullable=True),
    sa.Column('coupon_apply_user', mysql.INTEGER(display_width=11), nullable=True),
    sa.Column('coupon_apply_users', sa.String(length=45), nullable=True),
    sa.Column('marketing_campaign_condition', sa.String(length=45), nullable=True),
    sa.Column('marketing_campaign_value', sa.String(length=45), nullable=True),
    sa.Column('can_auto_check', mysql.TINYINT(display_width=1), nullable=True),
    sa.Column('inactive', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('marketing_campaign_id')
    )
    op.create_table('merchandise_details',
    sa.Column('merchandise_detail_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('languages_language_id', mysql.INTEGER(display_width=2), nullable=False),
    sa.Column('merchandises_merchandise_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('merchandise_name', sa.String(length=45), nullable=True),
    sa.Column('merchandise_brief', sa.String(length=255), nullable=True),
    sa.Column('merchandise_description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('merchandise_detail_id', 'languages_language_id', 'merchandises_merchandise_id')
    )
    op.create_table('merchandises',
    sa.Column('merchandise_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('inactive', sa.DateTime(), nullable=True),
    sa.Column('brands_brand_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('categories_category_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.PrimaryKeyConstraint('merchandise_id', 'brands_brand_id', 'categories_category_id')
    )
    op.create_table('order_line_logistics',
    sa.Column('order_line_logistic_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('order_lines_order_line_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('delivery_methods_delivery_method_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('qty', mysql.INTEGER(display_width=5), server_default=sa.text("'0'"), nullable=False),
    sa.Column('logistic_tracking_code', sa.String(length=45), nullable=True),
    sa.Column('logistic_status', sa.String(length=45), server_default=sa.text("'POSTED'"), nullable=False),
    sa.PrimaryKeyConstraint('order_line_logistic_id', 'order_lines_order_line_id', 'delivery_methods_delivery_method_id')
    )
    op.create_table('order_lines',
    sa.Column('order_line_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('orders_order_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('products_product_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('sku', sa.String(length=45), nullable=False),
    sa.Column('quantity', mysql.INTEGER(display_width=10), server_default=sa.text("'1'"), nullable=False),
    sa.Column('price', sa.DECIMAL(precision=10, scale=2), server_default=sa.text("'0.00'"), nullable=False),
    sa.Column('brief', sa.String(length=255), nullable=True),
    sa.Column('image_thumb', sa.String(length=255), nullable=True),
    sa.Column('image_1', sa.String(length=255), nullable=True),
    sa.Column('image_2', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('order_line_id', 'orders_order_id', 'products_product_id')
    )
    op.create_table('order_statuses',
    sa.Column('order_status_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('order_status', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('order_status_id')
    )
    op.create_table('orders',
    sa.Column('order_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('order_date', sa.DateTime(), nullable=False),
    sa.Column('users_user_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('order_statuses_order_status_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('is_paid_in_full', mysql.TINYINT(display_width=1), server_default=sa.text("'0'"), nullable=False),
    sa.Column('paid_amount', sa.DECIMAL(precision=10, scale=2), server_default=sa.text("'0.00'"), nullable=False),
    sa.Column('total_amount_include_tax', sa.DECIMAL(precision=10, scale=2), server_default=sa.text("'0.00'"), nullable=False),
    sa.Column('total_tax_amount', sa.DECIMAL(precision=10, scale=2), server_default=sa.text("'0.00'"), nullable=False),
    sa.Column('discount_code', sa.String(length=45), nullable=True),
    sa.Column('addresses_address_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('addresses_users_user_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.PrimaryKeyConstraint('order_id', 'users_user_id', 'order_statuses_order_status_id', 'addresses_address_id', 'addresses_users_user_id')
    )
    op.create_table('payment_methods',
    sa.Column('payment_method_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('payment_method_name', sa.String(length=45), nullable=False),
    sa.Column('payment_method_icon', sa.String(length=45), nullable=True),
    sa.Column('surcharge', sa.DECIMAL(precision=10, scale=2), server_default=sa.text("'0.00'"), nullable=False),
    sa.PrimaryKeyConstraint('payment_method_id')
    )
    op.create_table('payment_transactions',
    sa.Column('payment_transaction_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('users_user_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('payment_methods_payment_method_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('orders_order_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('transaction_amount', sa.DECIMAL(precision=10, scale=2), nullable=False),
    sa.Column('transaction_result', sa.Text(), nullable=True),
    sa.Column('transaction_decision', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('payment_transaction_id', 'users_user_id', 'payment_methods_payment_method_id', 'orders_order_id')
    )
    op.create_table('permissions',
    sa.Column('permission_id', mysql.TINYINT(display_width=2), nullable=False),
    sa.Column('permission_name', sa.String(length=45), nullable=False),
    sa.Column('inactive', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('permission_id')
    )
    op.create_table('products',
    sa.Column('product_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('sku', sa.String(length=45), nullable=False),
    sa.Column('price_exclude_tax', sa.String(length=45), nullable=True),
    sa.Column('merchandises_merchandise_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('taxes_tax_id', mysql.TINYINT(display_width=1), nullable=False),
    sa.Column('quantity', mysql.INTEGER(display_width=11), server_default=sa.text("'0'"), nullable=True),
    sa.PrimaryKeyConstraint('product_id', 'sku', 'merchandises_merchandise_id', 'taxes_tax_id')
    )
    op.create_table('products_has_spec_group_items',
    sa.Column('products_product_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('spec_group_items_spec_group_item_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.PrimaryKeyConstraint('products_product_id', 'spec_group_items_spec_group_item_id')
    )
    op.create_table('purchase_order',
    sa.Column('purchase_order_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('suppliers_supply_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('purchase_order_date', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False),
    sa.PrimaryKeyConstraint('purchase_order_id', 'suppliers_supply_id')
    )
    op.create_table('purchase_order_lines',
    sa.Column('purchase_order_line_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('purchase_item', sa.String(length=255), nullable=False),
    sa.Column('purchase_quantity', mysql.INTEGER(display_width=5), server_default=sa.text("'1'"), nullable=False),
    sa.Column('price', sa.DECIMAL(precision=11, scale=2), server_default=sa.text("'0.00'"), nullable=False),
    sa.Column('note', sa.String(length=255), nullable=True),
    sa.Column('inactive', sa.TIMESTAMP(), nullable=True),
    sa.Column('purchase_order_purchase_order_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.PrimaryKeyConstraint('purchase_order_line_id', 'purchase_order_purchase_order_id')
    )
    op.create_table('settings',
    sa.Column('setting_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('setting_name', sa.String(length=45), nullable=False),
    sa.Column('setting_value', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('setting_id')
    )
    op.create_table('spec_group_items',
    sa.Column('spec_group_item_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('spec_groups_spec_group_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('spec_group_item_name', sa.String(length=45), nullable=False),
    sa.Column('inactive', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('spec_group_item_id', 'spec_groups_spec_group_id')
    )
    op.create_table('spec_groups',
    sa.Column('spec_group_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('spec_group_name', sa.String(length=45), nullable=True),
    sa.Column('inactive', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('spec_group_id')
    )
    op.create_table('suppliers',
    sa.Column('supply_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('supplier_name', sa.String(length=255), nullable=False),
    sa.Column('supplier_no', sa.String(length=255), nullable=True),
    sa.Column('supplier_address', sa.String(length=255), nullable=True),
    sa.Column('supplier_suburb_city', sa.String(length=255), nullable=True),
    sa.Column('supplier_state_area', sa.String(length=255), nullable=True),
    sa.Column('supplier_contact_name', sa.String(length=255), nullable=True),
    sa.Column('supplier_contact_no', sa.String(length=45), nullable=True),
    sa.Column('inactive', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('supply_id')
    )
    op.create_table('taxes',
    sa.Column('tax_id', mysql.TINYINT(display_width=1), nullable=False),
    sa.Column('tax_code', sa.String(length=10), nullable=False),
    sa.Column('tax_rate', mysql.INTEGER(display_width=3), server_default=sa.text("'0'"), nullable=False),
    sa.Column('inactive', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('tax_id')
    )
    op.create_table('timestamps',
    sa.Column('create_time', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('update_time', sa.TIMESTAMP(), nullable=True)
    )
    op.create_table('user',
    sa.Column('username', sa.String(length=16), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=32), nullable=False),
    sa.Column('create_time', sa.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True)
    )
    op.create_table('user_point_histories',
    sa.Column('user_point_history_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('user_points_actioned', sa.DECIMAL(precision=11, scale=2), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('users_user_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.PrimaryKeyConstraint('user_point_history_id', 'users_user_id')
    )
    op.create_table('user_points',
    sa.Column('user_point_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('users_user_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('user_points', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('last_update', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_point_id', 'users_user_id')
    )
    op.create_table('users',
    sa.Column('user_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('mobile', sa.String(length=45), nullable=True),
    sa.Column('phone', sa.String(length=45), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('failed_login_attempts', mysql.TINYINT(display_width=1), nullable=True),
    sa.Column('last_failed_login', sa.DateTime(), nullable=True),
    sa.Column('password_reset_hash', sa.String(length=255), nullable=True),
    sa.Column('password_request_at', sa.DateTime(), nullable=True),
    sa.Column('external_source', sa.String(length=45), nullable=True),
    sa.Column('external_id', mysql.INTEGER(display_width=4), nullable=True),
    sa.Column('inactive', sa.DateTime(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('users_has_permissions',
    sa.Column('users_user_id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('permissions_permission_id', mysql.TINYINT(display_width=1), nullable=False),
    sa.Column('inactive', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('users_user_id', 'permissions_permission_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_has_permissions')
    op.drop_table('users')
    op.drop_table('user_points')
    op.drop_table('user_point_histories')
    op.drop_table('user')
    op.drop_table('timestamps')
    op.drop_table('taxes')
    op.drop_table('suppliers')
    op.drop_table('spec_groups')
    op.drop_table('spec_group_items')
    op.drop_table('settings')
    op.drop_table('purchase_order_lines')
    op.drop_table('purchase_order')
    op.drop_table('products_has_spec_group_items')
    op.drop_table('products')
    op.drop_table('permissions')
    op.drop_table('payment_transactions')
    op.drop_table('payment_methods')
    op.drop_table('orders')
    op.drop_table('order_statuses')
    op.drop_table('order_lines')
    op.drop_table('order_line_logistics')
    op.drop_table('merchandises')
    op.drop_table('merchandise_details')
    op.drop_table('marketing_campaigns')
    op.drop_table('languages')
    op.drop_table('delivery_methods')
    op.drop_table('category_details')
    op.drop_table('categories_has_spec_groups')
    op.drop_table('categories')
    op.drop_table('brands')
    op.drop_table('brand_details')
    op.drop_table('audit_logs')
    op.drop_table('assets')
    op.drop_table('asset_objects')
    op.drop_table('addresses')
    # ### end Alembic commands ###
