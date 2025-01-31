from typing import List
from app.models import Compra
from app.repositories import CompraRepository

repository = CompraRepository()

class CompraService:
  def save(self, compra: Compra):
    return repository.save(compra)

