
from sqlalchemy import Column, DECIMAL, Date, DateTime, MetaData, String, TIMESTAMP, Table, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT

metadata = MetaData()


##########################################################################

t_addresses = Table(
    'addresses', metadata,
    Column('address_id', INTEGER(11), primary_key=True, nullable=False),
    Column('address_line', String(255)),
    Column('suburb_city', String(255)),
    Column('state_area', String(255)),
    Column('post_code', String(20)),
    Column('country', String(45), server_default=text("'Australia'")),
    Column('type', String(45)),
    Column('users_user_id', INTEGER(11), primary_key=True, nullable=False)
)


t_asset_objects = Table(
    'asset_objects', metadata,
    Column('asset_object_id', INTEGER(11), primary_key=True, nullable=False),
    Column('asset_table', String(45), nullable=False),
    Column('asset_target_id', INTEGER(11)),
    Column('assets_asset_id', INTEGER(11), primary_key=True, nullable=False)
)


t_assets = Table(
    'assets', metadata,
    Column('asset_id', INTEGER(11), primary_key=True),
    Column('asset_name', String(45), nullable=False),
    Column('asset_hash', String(255), nullable=False),
    Column('type', String(45)),
    Column('alt', String(45))
)


t_audit_logs = Table(
    'audit_logs', metadata,
    Column('audit_log_id', INTEGER(11), primary_key=True),
    Column('table', String(45), nullable=False),
    Column('table_id', INTEGER(11)),
    Column('action', String(1), comment='C/U'),
    Column('action_brief', String(45), nullable=False),
    Column('action_data', Text),
    Column('action_by', INTEGER(11)),
    Column('action_at', DateTime, nullable=False),
    Column('action_ip', String(45), nullable=False)
)


t_brand_details = Table(
    'brand_details', metadata,
    Column('brand_detail_id', INTEGER(11), primary_key=True, nullable=False),
    Column('brands_brand_id', INTEGER(11), primary_key=True, nullable=False),
    Column('languages_language_id', INTEGER(2), primary_key=True, nullable=False),
    Column('brand_name', String(255), nullable=False),
    Column('brand_brief', String(255)),
    Column('brand_description', Text)
)


t_brands = Table(
    'brands', metadata,
    Column('brand_id', INTEGER(11), primary_key=True),
    Column('brand_url', String(255)),
    Column('inactive', DateTime)
)


t_categories = Table(
    'categories', metadata,
    Column('category_id', INTEGER(11), primary_key=True),
    Column('parent_category', INTEGER(11)),
    Column('inactive', DateTime)
)


t_categories_has_spec_groups = Table(
    'categories_has_spec_groups', metadata,
    Column('categories_category_id', INTEGER(11), primary_key=True, nullable=False),
    Column('spec_groups_spec_group_id', INTEGER(11), primary_key=True, nullable=False)
)


t_category_details = Table(
    'category_details', metadata,
    Column('category_detail_id', INTEGER(11), primary_key=True, nullable=False),
    Column('categories_category_id', INTEGER(11), primary_key=True, nullable=False),
    Column('languages_language_id', INTEGER(2), primary_key=True, nullable=False),
    Column('category_name', String(45), nullable=False),
    Column('category_brief', String(255))
)


t_delivery_methods = Table(
    'delivery_methods', metadata,
    Column('delivery_method_id', INTEGER(11), primary_key=True),
    Column('delivery_name', String(45)),
    Column('delivery_charge', DECIMAL(10, 2), server_default=text("'0.00'")),
    Column('delivery_tracking_url', String(255)),
    Column('inactive', DateTime)
)


t_languages = Table(
    'languages', metadata,
    Column('language_id', INTEGER(2), primary_key=True),
    Column('language', String(10))
)


t_marketing_campaigns = Table(
    'marketing_campaigns', metadata,
    Column('marketing_campaign_id', INTEGER(11), primary_key=True),
    Column('coupon_code', String(45)),
    Column('coupon_created_at', DateTime, nullable=False),
    Column('coupon_expiry_date', Date),
    Column('coupon_apply_user', INTEGER(11)),
    Column('coupon_apply_users', String(45)),
    Column('marketing_campaign_condition', String(45)),
    Column('marketing_campaign_value', String(45)),
    Column('can_auto_check', TINYINT(1)),
    Column('inactive', DateTime)
)


t_merchandise_details = Table(
    'merchandise_details', metadata,
    Column('merchandise_detail_id', INTEGER(11), primary_key=True, nullable=False),
    Column('languages_language_id', INTEGER(2), primary_key=True, nullable=False),
    Column('merchandises_merchandise_id', INTEGER(11), primary_key=True, nullable=False),
    Column('merchandise_name', String(45)),
    Column('merchandise_brief', String(255)),
    Column('merchandise_description', Text)
)


t_merchandises = Table(
    'merchandises', metadata,
    Column('merchandise_id', INTEGER(11), primary_key=True, nullable=False),
    Column('inactive', DateTime),
    Column('brands_brand_id', INTEGER(11), primary_key=True, nullable=False),
    Column('categories_category_id', INTEGER(11), primary_key=True, nullable=False)
)


t_order_line_logistics = Table(
    'order_line_logistics', metadata,
    Column('order_line_logistic_id', INTEGER(11), primary_key=True, nullable=False),
    Column('order_lines_order_line_id', INTEGER(11), primary_key=True, nullable=False),
    Column('delivery_methods_delivery_method_id', INTEGER(11), primary_key=True, nullable=False),
    Column('qty', INTEGER(5), nullable=False, server_default=text("'0'")),
    Column('logistic_tracking_code', String(45)),
    Column('logistic_status', String(45), nullable=False, server_default=text("'POSTED'"))
)


t_order_lines = Table(
    'order_lines', metadata,
    Column('order_line_id', INTEGER(11), primary_key=True, nullable=False),
    Column('orders_order_id', INTEGER(11), primary_key=True, nullable=False),
    Column('products_product_id', INTEGER(11), primary_key=True, nullable=False),
    Column('sku', String(45), nullable=False),
    Column('quantity', INTEGER(10), nullable=False, server_default=text("'1'")),
    Column('price', DECIMAL(10, 2), nullable=False, server_default=text("'0.00'")),
    Column('brief', String(255)),
    Column('image_thumb', String(255)),
    Column('image_1', String(255)),
    Column('image_2', String(255))
)


t_order_statuses = Table(
    'order_statuses', metadata,
    Column('order_status_id', INTEGER(11), primary_key=True),
    Column('order_status', String(45), nullable=False)
)


t_orders = Table(
    'orders', metadata,
    Column('order_id', INTEGER(11), primary_key=True, nullable=False),
    Column('order_date', DateTime, nullable=False),
    Column('users_user_id', INTEGER(11), primary_key=True, nullable=False),
    Column('order_statuses_order_status_id', INTEGER(11), primary_key=True, nullable=False),
    Column('is_paid_in_full', TINYINT(1), nullable=False, server_default=text("'0'")),
    Column('paid_amount', DECIMAL(10, 2), nullable=False, server_default=text("'0.00'")),
    Column('total_amount_include_tax', DECIMAL(10, 2), nullable=False, server_default=text("'0.00'")),
    Column('total_tax_amount', DECIMAL(10, 2), nullable=False, server_default=text("'0.00'")),
    Column('discount_code', String(45)),
    Column('addresses_address_id', INTEGER(11), primary_key=True, nullable=False),
    Column('addresses_users_user_id', INTEGER(11), primary_key=True, nullable=False)
)


t_payment_methods = Table(
    'payment_methods', metadata,
    Column('payment_method_id', INTEGER(11), primary_key=True),
    Column('payment_method_name', String(45), nullable=False),
    Column('payment_method_icon', String(45)),
    Column('surcharge', DECIMAL(10, 2), nullable=False, server_default=text("'0.00'"))
)


t_payment_transactions = Table(
    'payment_transactions', metadata,
    Column('payment_transaction_id', INTEGER(11), primary_key=True, nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('users_user_id', INTEGER(11), primary_key=True, nullable=False),
    Column('payment_methods_payment_method_id', INTEGER(11), primary_key=True, nullable=False),
    Column('orders_order_id', INTEGER(11), primary_key=True, nullable=False),
    Column('transaction_amount', DECIMAL(10, 2), nullable=False),
    Column('transaction_result', Text),
    Column('transaction_decision', String(45))
)


t_permissions = Table(
    'permissions', metadata,
    Column('permission_id', TINYINT(2), primary_key=True),
    Column('permission_name', String(45), nullable=False),
    Column('inactive', DateTime)
)


t_products = Table(
    'products', metadata,
    Column('product_id', INTEGER(11), primary_key=True, nullable=False),
    Column('SKU', String(45), primary_key=True, nullable=False),
    Column('price_exclude_tax', String(45)),
    Column('merchandises_merchandise_id', INTEGER(11), primary_key=True, nullable=False),
    Column('taxes_tax_id', TINYINT(1), primary_key=True, nullable=False),
    Column('quantity', INTEGER(11), server_default=text("'0'"))
)


t_products_has_spec_group_items = Table(
    'products_has_spec_group_items', metadata,
    Column('products_product_id', INTEGER(11), primary_key=True, nullable=False),
    Column('spec_group_items_spec_group_item_id', INTEGER(11), primary_key=True, nullable=False)
)


t_purchase_order = Table(
    'purchase_order', metadata,
    Column('purchase_order_id', INTEGER(11), primary_key=True, nullable=False),
    Column('suppliers_supply_id', INTEGER(11), primary_key=True, nullable=False),
    Column('purchase_order_date', TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
)


t_purchase_order_lines = Table(
    'purchase_order_lines', metadata,
    Column('purchase_order_line_id', INTEGER(11), primary_key=True, nullable=False),
    Column('purchase_item', String(255), nullable=False),
    Column('purcase_quantity', INTEGER(5), nullable=False, server_default=text("'1'")),
    Column('price', DECIMAL(11, 2), nullable=False, server_default=text("'0.00'")),
    Column('note', String(255)),
    Column('inactive', TIMESTAMP),
    Column('purchase_order_purchase_order_id', INTEGER(11), primary_key=True, nullable=False)
)


t_settings = Table(
    'settings', metadata,
    Column('setting_id', INTEGER(11), primary_key=True),
    Column('setting_name', String(45), nullable=False),
    Column('setting_value', String(45), nullable=False)
)


t_spec_group_items = Table(
    'spec_group_items', metadata,
    Column('spec_group_item_id', INTEGER(11), primary_key=True, nullable=False),
    Column('spec_groups_spec_group_id', INTEGER(11), primary_key=True, nullable=False),
    Column('spec_group_item_name', String(45), nullable=False),
    Column('inactive', DateTime)
)


t_spec_groups = Table(
    'spec_groups', metadata,
    Column('spec_group_id', INTEGER(11), primary_key=True),
    Column('spec_group_name', String(45)),
    Column('inactive', TIMESTAMP)
)


t_suppliers = Table(
    'suppliers', metadata,
    Column('supply_id', INTEGER(11), primary_key=True),
    Column('supplier_name', String(255), nullable=False),
    Column('supplier_no', String(255)),
    Column('supplier_address', String(255)),
    Column('supplier_suburb_city', String(255)),
    Column('supplier_state_area', String(255)),
    Column('supplier_contact_name', String(255)),
    Column('supplier_contact_no', String(45)),
    Column('inactive', TIMESTAMP)
)


t_taxes = Table(
    'taxes', metadata,
    Column('tax_id', TINYINT(1), primary_key=True),
    Column('tax_code', String(10), nullable=False),
    Column('tax_rate', INTEGER(3), nullable=False, server_default=text("'0'")),
    Column('inactive', DateTime)
)


t_timestamps = Table(
    'timestamps', metadata,
    Column('create_time', TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")),
    Column('update_time', TIMESTAMP)
)


t_user = Table(
    'user', metadata,
    Column('username', String(16), nullable=False),
    Column('email', String(255)),
    Column('password', String(32), nullable=False),
    Column('create_time', TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
)


t_user_point_histories = Table(
    'user_point_histories', metadata,
    Column('user_point_history_id', INTEGER(11), primary_key=True, nullable=False),
    Column('user_points_actioned', DECIMAL(11, 2), nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('users_user_id', INTEGER(11), primary_key=True, nullable=False)
)


t_user_points = Table(
    'user_points', metadata,
    Column('user_point_id', INTEGER(11), primary_key=True, nullable=False),
    Column('users_user_id', INTEGER(11), primary_key=True, nullable=False),
    Column('user_points', INTEGER(11), nullable=False),
    Column('last_update', DateTime)
)


t_users = Table(
    'users', metadata,
    Column('user_id', INTEGER(11), primary_key=True),
    Column('email', String(255), nullable=False),
    Column('mobile', String(45)),
    Column('phone', String(45)),
    Column('password', String(255), nullable=False),
    Column('failed_login_attempts', TINYINT(1)),
    Column('last_failed_login', DateTime),
    Column('password_reset_hash', String(255)),
    Column('password_request_at', DateTime),
    Column('external_source', String(45)),
    Column('external_id', INTEGER(4)),
    Column('inactive', DateTime),
    Column('last_login', DateTime)
)


t_users_has_permissions = Table(
    'users_has_permissions', metadata,
    Column('users_user_id', INTEGER(11), primary_key=True, nullable=False),
    Column('permissions_permission_id', TINYINT(1), primary_key=True, nullable=False),
    Column('inactive', DateTime)
)


##########################################################################


__all__ = [name for name in locals().keys()
        if name.startswith('t_') or name.startswith('j_')]
__all__.insert(0, 'metadata')
