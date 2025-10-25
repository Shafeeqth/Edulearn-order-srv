from abc import ABC, abstractmethod
from typing import Optional, List

from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.entities.order import Order
from src.domain.entities.order_items import OrderItem
from src.domain.entities.payment_details import PaymentDetails


# This class is an abstract base class for an order repository interface in Python.
class IOrderRepository(ABC):
    @abstractmethod
    async def save(self, order: Order, session: AsyncSession) -> Order:
        """
        The `save` function in Python is an asynchronous method that saves an order object.

        :param order: Order object that contains information about a customer's order, such as items
        purchased, quantity, price, and any other relevant details
        :type order: Order
        """
        pass

    @abstractmethod
    async def find_by_id(self, order_id: str, session: AsyncSession) -> Optional[Order]:
        """
        Asynchronously retrieves an order by its unique identifier.
        Returns the order if found, otherwise returns None.

        Args:
            order_id (str): The unique identifier of the order.

        Returns:
            Optional[Order]: The order object if found, otherwise None.
        """
        pass
    @abstractmethod
    async def find_by_idempotency_key(self, idempotency_key: str, session: AsyncSession) -> Optional[Order]:
        """
        Asynchronously retrieves an order by idempotency key.
        Returns the order if found, otherwise returns None.

        Args:
            idempotency_key (str): A unique identifier.

        Returns:
            Optional[Order]: The order object if found, otherwise None.
        """
        pass


    @abstractmethod
    async def find_by_user_id(self, user_id: str, session: AsyncSession) -> List[Order]:
        """
        Asynchronously retrieves all orders associated with a specific user.
        Returns a list of orders for the given user identifier.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            List[Order]: A list of order objects associated with the user.
        """
        pass

    @abstractmethod
    async def update_status(self, order_id: str, status: str, session: AsyncSession) -> None:
        """
        Update the status of an order.

        Args:
            order_id (str): The unique identifier of the order.
            status (str): The new status value.
        """
        pass

    @abstractmethod
    async def add_items(self, order_id: str, items: List[OrderItem], session: AsyncSession) -> None:
        """
        Add one or more items to an order.

        Args:
            order_id (str): The unique identifier of the order.
            items (List[OrderItem]): Items to add.
        """
        pass

    @abstractmethod
    async def attach_payment_details(self, order_id: str, payment_details: PaymentDetails, session: AsyncSession) -> None:
        """
        Attach payment details to an order (one-to-one).

        Args:
            order_id (str): The unique identifier of the order.
            payment_details (PaymentDetails): Payment details to attach.
        """
        pass


