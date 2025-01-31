from app.models import Stock
from marshmallow import fields, Schema, post_load, EXCLUDE

class StockSchema(Schema):
    class Meta:
        unknown = EXCLUDE 
    id = fields.Integer(dump_only=True)
    producto_id = fields.Integer(required=True)
    fecha_transaccion = fields.DateTime(required=False)
    cantidad = fields.Integer(required=True)
    entrada_salida = fields.Integer(required=True)

    @post_load
    def make_stock(self, data, **kwargs):
        return Stock(**data)

