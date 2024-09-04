from database import db, Base

order_product = db.Table(
    'Order_Product',
    Base.metadata,
    db.Column('order_id', db.ForeignKey('orders.id')),
    db.Column('product_id', db.ForeignKey('products.id'))
)