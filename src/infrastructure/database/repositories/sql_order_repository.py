import json
from src.application.interfaces.logging_interface import ILoggingService
from src.application.interfaces.redis_interface import IRedisService
from src.domain.repositories.order_repository import IOrderRepository
from src.infrastructure.database.models.order_model import (
    OrderModel,
    OrderItemModel,
    PaymentDetailsModel,
)
# from src.infrastructure.database.mapper import DomainModelMapper
from src.domain.entities.order_items import OrderItem
from src.domain.entities.payment_details import PaymentDetails
from src.domain.entities.order import Order, OrderStatus
from src.domain.value_objects.money import Money
from src.infrastructure.database.database import AsyncSession
from sqlalchemy import select, update
from sqlalchemy.orm import selectinload
from typing import Optional, List
import logging
from uuid import uuid4
from datetime import datetime


class SqlOrderRepository(IOrderRepository):
    def __init__(self, redis: IRedisService, logging_service: ILoggingService):
        # session = session
        self.redis = redis
        self.logger = logging_service.get_logger("SqlOrderRepository")

    # async def save(self, order: Order,  session: AsyncSession) -> None:
    #     try:
    #         order_model = OrderModel.from_domain(order)
    #         session.add(order_model)
    #         # Persist items
    #         for item in order.items:
    #             session.add(OrderItemModel.from_domain(item, order.id))
    #         # Persist payment details if available
    #         if order.payment_details:
    #             session.add(PaymentDetailsModel.from_domain(order.payment_details, order.id))
    #         await session.commit()

    #         order_model_entity = order_model.map_to_domain()
    #         # Update the entity with the saved data
    #         order.id = order_model_entity.id
    #         order.created_at = order_model_entity.created_at
    #         order.updated_at = order_model_entity.updated_at

    #         # Update cache
    #         cache_key = f"orders:{order.id}"
    #         await self.redis.set(cache_key, json.dumps({
    #             "id": order.id,
    #             "user_id": order.user_id,
    #             "items": [
    #                 {"course_id": i.course_id, "price": i.price}
    #                 for i in order.items
    #             ],
    #             "amount": order.amount.amount,
    #             "currency": order.amount.currency,
    #             "discount": order.discount,
    #             "status": order.status.value,
    #             "payment_details": (
    #                 {
    #                     "payment_id": order.payment_details.payment_id,
    #                     "provider": order.payment_details.provider,
    #                     "provider_order_id": order.payment_details.provider_order_id,
    #                     "payment_status": order.payment_details.payment_status,
    #                     "updated_at": order.payment_details.updated_at.isoformat(),
    #                 }
    #                 if order.payment_details
    #                 else None
    #             ),
    #             "created_at": order.created_at.isoformat(),
    #             "updated_at": order.updated_at.isoformat(),
    #         }), expire=3600)

    #         # Invalidate user orders cache
    #         await self.redis.delete(f"user_orders:{order.user_id}")

    #     except Exception as e:
    #         self.logger.error(f"Failed to save order {order.id}: {str(e)}")
    #         await session.rollback()
    #         raise
    # async def save(self, order: Order, session: AsyncSession) -> None:
    #     try:
    #         # Build the OrderModel and attach children to it so relationships are populated in-memory.
    #         order_model = OrderModel.from_domain(order)

    #         # Attach item models to the order_model.items list (in-memory)
    #         item_models = []
    #         for item in order.items:
    #             item_model = OrderItemModel.from_domain(item, order.id)
    #             item_models.append(item_model)
    #         # Make sure we attach them to the relationship
    #         order_model.items = item_models

    #         # Attach payment details model (if present) directly to the relationship
    #         if order.payment_details:
    #             payment_model = PaymentDetailsModel.from_domain(order.payment_details, order.id)
    #             order_model.payment_details = payment_model

    #         # Add the root order_model only (children are in-memory attached)
    #         session.add(order_model)

    #         # Flush so DB-side defaults (timestamps etc.) are generated and PKs known.
    #         await session.flush()

    #         # Optional: refresh to load updated DB-side defaults (if you want)
    #         # await session.refresh(order_model)

    #         # Commit the transaction
    #         await session.commit()

    #         # Now map to domain using in-memory relationship objects (no lazy loads)
    #         order_model_entity = order_model.map_to_domain()
    #         order.id = order_model_entity.id
    #         order.created_at = order_model_entity.created_at
    #         order.updated_at = order_model_entity.updated_at

    #         # Cache (note: use .value or .name if using enums)
    #         cache_key = f"orders:{order.id}"
    #         await self.redis.set(
    #             cache_key,
    #             json.dumps(
    #                 {
    #                     "id": order.id,
    #                     "user_id": order.user_id,
    #                     "items": [{"course_id": i.course_id, "price": i.price} for i in order.items],
    #                     "amount": order.amount.amount,
    #                     "currency": order.amount.currency,
    #                     "discount": order.discount,
    #                     "status": order.status.value if hasattr(order.status, "value") else order.status,
    #                     "payment_details": (
    #                         {
    #                             "payment_id": order.payment_details.payment_id,
    #                             "provider": order.payment_details.provider,
    #                             "provider_order_id": order.payment_details.provider_order_id,
    #                             "payment_status": order.payment_details.payment_status,
    #                             "updated_at": order.payment_details.updated_at.isoformat()
    #                             if getattr(order.payment_details, "updated_at", None) else None,
    #                         }
    #                         if order.payment_details
    #                         else None
    #                     ),
    #                     "created_at": order.created_at.isoformat(),
    #                     "updated_at": order.updated_at.isoformat(),
    #                 }
    #             ),
    #             expire=3600,
    #         )

    #         # Invalidate user orders cache
    #         await self.redis.delete(f"user_orders:{order.user_id}")

    #     except Exception as e:
    #         # Rollback and re-raise
    #         self.logger.error(f"Failed to save order {order.id}: {str(e)}")
    #         try:
    #             await session.rollback()
    #         except Exception:
    #             pass
    #         raise
    # async def save(self, order: Order, session: AsyncSession) -> None:
    #     try:
    #         # Build the OrderModel and attach children to it so relationships are populated in-memory.
    #         order_model = OrderModel.from_domain(order)

    #         # Build and attach item models to the order_model.items list
    #         item_models = [OrderItemModel.from_domain(item, order.id) for item in order.items]
    #         order_model.items = item_models  # in-memory collection attached

    #         # Attach payment details model (if present) as a scalar attribute
    #         if order.payment_details:
    #             payment_model = PaymentDetailsModel.from_domain(order.payment_details, order.id)
    #             order_model.payment_details = payment_model  # works because uselist=False

    #         # Add and flush to persist; flushing will generate DB defaults but not commit yet.
    #         session.add(order_model)
    #         await session.flush()

    #         # Optionally refresh to read DB-generated defaults into the instance.
    #         # (Allowed here because we're still inside the async session)
    #         await session.refresh(order_model)

    #         # Commit transaction
    #         # await session.commit()

    #         # Now map to domain using in-memory relationship objects (no lazy loads)
    #         order_model_entity = order_model.map_to_domain()
    #         order.id = order_model_entity.id
    #         order.created_at = order_model_entity.created_at
    #         order.updated_at = order_model_entity.updated_at

    #         # Cache payload (as before)
    #         cache_key = f"orders:{order.id}"
    #         await self.redis.set(
    #             cache_key,
    #             json.dumps({
    #                 "id": order.id,
    #                 "user_id": order.user_id,
    #                 "items": [{"course_id": i.course_id, "price": i.price} for i in order.items],
    #                 "amount": order.amount.amount,
    #                 "currency": order.amount.currency,
    #                 "discount": order.discount,
    #                 "status": order.status.value if hasattr(order.status, "value") else order.status,
    #                 "payment_details": (
    #                     {
    #                         "payment_id": order.payment_details.payment_id,
    #                         "provider": order.payment_details.provider,
    #                         "provider_order_id": order.payment_details.provider_order_id,
    #                         "payment_status": order.payment_details.payment_status,
    #                         "updated_at": order.payment_details.updated_at.isoformat()
    #                             if getattr(order.payment_details, "updated_at", None) else None,
    #                     } if order.payment_details else None
    #                 ),
    #                 "created_at": order.created_at.isoformat(),
    #                 "updated_at": order.updated_at.isoformat(),
    #             }),
    #             expire=3600,
    #         )

    #         await self.redis.delete(f"user_orders:{order.user_id}")

    #     except Exception as e:
    #         self.logger.error(f"Failed to save order {order.id}: {str(e)}")
    #         try:
    #             await session.rollback()
    #         except Exception:
    #             pass
    #         raise
    async def save(self, order: Order, session: AsyncSession) -> Order:
        # Map domain → persistence model
        order_model = OrderModel(
            id=order.id,
            user_id=order.user_id,
            idempotency_key=order.idempotency_key,
            amount=order.amount.amount,
            currency=order.amount.currency,
            discount=order.discount,
            sub_total=order.sub_total,
            status=order.status.value if hasattr(
                order.status, "value") else order.status,
            created_at=order.created_at,
            updated_at=order.updated_at,
        )

        # Attach items
        item_models = [
            OrderItemModel(
                id=str(uuid4()),
                course_id=item.course_id,
                price=item.price
            )
            for item in order.items
        ]
        order_model.items = item_models

        # Attach payment details
        if order.payment_details:
            order_model.payment_details = PaymentDetailsModel(
                payment_id=order.payment_details.payment_id,
                provider=order.payment_details.provider,
                provider_order_id=order.payment_details.provider_order_id,
                payment_status=order.payment_details.payment_status,
                updated_at=order.payment_details.updated_at,
            )

        session.add(order_model)

        # Flush so PKs are available, refresh ensures values are in memory
        await session.flush()
        await session.refresh(order_model)

        #  no lazy loading: relationships are already attached
        return self._map_to_domain(order_model)

    async def find_by_id(self, order_id: str, session: AsyncSession) -> Optional[Order]:
        try:
            # Check cache first
            cache_key = f"orders:{order_id}"
            cached_order = await self.redis.get(cache_key)

            if cached_order:
                order_data = json.loads(cached_order)
                items = [
                    {
                        "course_id": i["course_id"],
                        "price": i["price"],
                    }
                    for i in order_data.get("items", [])
                ]
                payment_details = order_data.get("payment_details")
                from src.domain.entities.order_items import OrderItem
                from src.domain.entities.payment_details import PaymentDetails
                return Order(
                    id=order_data["id"],
                    user_id=order_data["user_id"],
                    idempotency_key=order_data["idempotency_key"],
                    items=[OrderItem.create(**i) for i in items],
                    amount=Money(
                        amount=order_data["amount"], currency=order_data["currency"]),
                    sub_total=order_data.get("sub_total"),
                    discount=order_data.get("discount"),
                    status=order_data["status"],
                    payment_details=(
                        PaymentDetails.create(
                            payment_id=payment_details["payment_id"],
                            provider=payment_details["provider"],
                            provider_order_id=payment_details["provider_order_id"],
                            payment_status=payment_details.get(
                                "payment_status", "pending"),
                        ) if payment_details else None
                    ),
                    created_at=datetime.fromisoformat(
                        order_data["created_at"]),
                    updated_at=datetime.fromisoformat(
                        order_data["updated_at"]),
                )

            # Fetch from database
            result = await session.execute(
                select(OrderModel)
                .options(
                    selectinload(OrderModel.items),
                    selectinload(OrderModel.payment_details),
                )
                .where(OrderModel.id == order_id)
            )
            order_model = result.scalars().first()
            if not order_model:
                return None
            order = order_model.map_to_domain()

            # Cache the result
            await self.redis.set(cache_key, json.dumps({
                "id": order.id,
                "user_id": order.user_id,
                "idempotency_key": order.idempotency_key,
                "items": [
                    {"course_id": i.course_id, "price": i.price}
                    for i in order.items
                ],
                "amount": order.amount.amount,
                "currency": order.amount.currency,
                "discount": order.discount,
                "sub_total": order.sub_total,
                "status": order.status.value,
                "payment_details": (
                    {
                        "payment_id": order.payment_details.payment_id,
                        "provider": order.payment_details.provider,
                        "provider_order_id": order.payment_details.provider_order_id,
                        "payment_status": order.payment_details.payment_status,
                        "updated_at": order.payment_details.updated_at.isoformat(),
                    }
                    if order.payment_details
                    else None
                ),
                "created_at": order.created_at.isoformat(),
                "updated_at": order.updated_at.isoformat(),
            }), expire=3600)

            return order

        except Exception as e:
            self.logger.error(f"Failed to find order {order_id}: {str(e)}")
            raise
        
    async def find_by_idempotency_key(self, idempotency_key: str, session: AsyncSession) -> Optional[Order]:
        try:
            # Check cache first
            cache_key = f"orders:idempotency_key:{idempotency_key}"
            cached_order = await self.redis.get(cache_key)

            if cached_order:
                order_data = json.loads(cached_order)
                items = [
                    {
                        "course_id": i["course_id"],
                        "price": i["price"],
                    }
                    for i in order_data.get("items", [])
                ]
                payment_details = order_data.get("payment_details")
                from src.domain.entities.order_items import OrderItem
                from src.domain.entities.payment_details import PaymentDetails
                return Order(
                    id=order_data["id"],
                    user_id=order_data["user_id"],
                    idempotency_key=order_data["idempotency_key"],
                    items=[OrderItem.create(**i) for i in items],
                    amount=Money(
                        amount=order_data["amount"], currency=order_data["currency"]),
                    sub_total=order_data.get("sub_total"),
                    discount=order_data.get("discount"),
                    status=order_data["status"],
                    payment_details=(
                        PaymentDetails.create(
                            payment_id=payment_details["payment_id"],
                            provider=payment_details["provider"],
                            provider_order_id=payment_details["provider_order_id"],
                            payment_status=payment_details.get(
                                "payment_status", "pending"),
                        ) if payment_details else None
                    ),
                    created_at=datetime.fromisoformat(
                        order_data["created_at"]),
                    updated_at=datetime.fromisoformat(
                        order_data["updated_at"]),
                )

            # Fetch from database
            result = await session.execute(
                select(OrderModel)
                .options(
                    selectinload(OrderModel.items),
                    selectinload(OrderModel.payment_details),
                )
                .where(OrderModel.idempotency_key == idempotency_key)
            )
            order_model = result.scalars().first()
            if not order_model:
                return None
            order = order_model.map_to_domain()

            # Cache the result
            await self.redis.set(cache_key, json.dumps({
                "id": order.id,
                "user_id": order.user_id,
                "idempotency_key": order.idempotency_key,
                "items": [
                    {"course_id": i.course_id, "price": i.price}
                    for i in order.items
                ],
                "amount": order.amount.amount,
                "currency": order.amount.currency,
                "discount": order.discount,
                "sub_total": order.sub_total,
                "status": order.status.value,
                "payment_details": (
                    {
                        "payment_id": order.payment_details.payment_id,
                        "provider": order.payment_details.provider,
                        "provider_order_id": order.payment_details.provider_order_id,
                        "payment_status": order.payment_details.payment_status,
                        "updated_at": order.payment_details.updated_at.isoformat(),
                    }
                    if order.payment_details
                    else None
                ),
                "created_at": order.created_at.isoformat(),
                "updated_at": order.updated_at.isoformat(),
            }), expire=3600)

            return order

        except Exception as e:
            self.logger.error(f"Failed to find order with idempotency_key {idempotency_key}: {str(e)}")
            raise

    async def find_by_user_id(self, user_id: str, session: AsyncSession) -> List[Order]:
        try:
            # Check cache first
            cache_key = f"user_orders:{user_id}"
            cached_orders = await self.redis.get(cache_key)
            if cached_orders:
                orders_data = json.loads(cached_orders)
                from src.domain.entities.order_items import OrderItem
                from src.domain.entities.payment_details import PaymentDetails
                return [
                    Order(
                        id=order_data["id"],
                        user_id=order_data["user_id"],
                        idempotency_key=order_data["idempotency_key"],
                        items=[OrderItem.create(**i)
                               for i in order_data.get("items", [])],
                        amount=Money(
                            amount=order_data["amount"], currency=order_data["currency"]),
                        sub_total=order_data.get("sub_total"),
                        discount=order_data.get("discount"),
                        status=order_data["status"],
                        payment_details=(
                            PaymentDetails.create(
                                payment_id=order_data["payment_details"]["payment_id"],
                                provider=order_data["payment_details"]["provider"],
                                provider_order_id=order_data["payment_details"]["provider_order_id"],
                                payment_status=order_data["payment_details"].get(
                                    "payment_status", "pending"),
                            ) if order_data.get("payment_details") else None
                        ),
                        created_at=datetime.fromisoformat(
                            order_data["created_at"]),
                        updated_at=datetime.fromisoformat(
                            order_data["updated_at"]),
                    )
                    for order_data in orders_data
                ]

            # Fetch from database
            result = await session.execute(
                select(OrderModel)
                .options(
                    selectinload(OrderModel.items),
                    selectinload(OrderModel.payment_details),
                )
                .where(OrderModel.user_id == user_id)
            )
            orders = result.scalars().all()
            domain_results = [order_model.map_to_domain()
                              for order_model in orders]

            # Cache the result
            await self.redis.set(cache_key, json.dumps([
                {
                    "id": order.id,
                    "user_id": order.user_id,
                    "idempotency_key": order.idempotency_key,
                    "items": [
                        {"course_id": i.course_id, "price": i.price}
                        for i in order.items
                    ],
                    "amount": order.amount.amount,
                    "currency": order.amount.currency,
                    "discount": order.discount,
                    "status": order.status.value,
                    "sub_total": order.sub_total,
                    "payment_details": (
                        {
                            "payment_id": order.payment_details.payment_id,
                            "provider": order.payment_details.provider,
                            "provider_order_id": order.payment_details.provider_order_id,
                            "payment_status": order.payment_details.payment_status,
                            "updated_at": order.payment_details.updated_at.isoformat(),
                        }
                        if order.payment_details
                        else None
                    ),
                    "created_at": order.created_at.isoformat(),
                    "updated_at": order.updated_at.isoformat(),
                }
                for order in domain_results
            ]), expire=3600)

            return domain_results
        except Exception as e:
            self.logger.error(
                f"Failed to find orders for user {user_id}: {str(e)}")
            raise

    async def update_status(self, order_id: str, status: str, session: AsyncSession) -> None:
        try:
            await session.execute(
                update(OrderModel)
                .where(OrderModel.id == order_id)
                .values(status=status)
            )
            await session.commit()
            await self.redis.delete(f"orders:{order_id}")
        except Exception as e:
            await session.rollback()
            self.logger.error(
                f"Failed to update status for order {order_id}: {str(e)}")
            raise

    async def add_items(self, order_id: str, items: List[OrderItem], session: AsyncSession) -> None:
        try:
            for item in items:
                session.add(OrderItemModel.from_domain(item, order_id))
            await session.commit()
            await self.redis.delete(f"orders:{order_id}")
        except Exception as e:
            await session.rollback()
            self.logger.error(
                f"Failed to add items for order {order_id}: {str(e)}")
            raise

    async def attach_payment_details(self, order_id: str, payment_details: PaymentDetails, session: AsyncSession) -> None:
        try:
            model = PaymentDetailsModel.from_domain(payment_details, order_id)
            session.add(model)
            await session.commit()
            await self.redis.delete(f"orders:{order_id}")
        except Exception as e:
            await session.rollback()
            self.logger.error(
                f"Failed to attach payment details for order {order_id}: {str(e)}")
            raise

    def _map_to_domain(self, order_model: OrderModel) -> Order:
        # Safe: items & payment_details are already loaded in memory
        items = [
            OrderItem(
                course_id=item.course_id,
                price=item.price
            )
            for item in (order_model.items or [])
        ]

        payment_details = None
        if order_model.payment_details:
            pd = order_model.payment_details
            payment_details = PaymentDetails(
                # id=pd.id,
                payment_id=pd.payment_id,
                provider=pd.provider,
                provider_order_id=pd.provider_order_id,
                payment_status=pd.payment_status,
                updated_at=pd.updated_at,
            )
        #   amount = Money(amount=self.__dict__[
        #                      "amount"], currency=self.__dict__["currency"])

        return Order(
            id=order_model.id,
            user_id=order_model.user_id,
            idempotency_key=order_model.idempotency_key,
            amount=Money(amount=order_model.amount,
                         currency=order_model.currency),
            discount=order_model.discount,
            sub_total=order_model.sub_total,
            status=OrderStatus(order_model.status) if isinstance(
                order_model.status, str) else order_model.status,
            created_at=order_model.created_at,
            updated_at=order_model.updated_at,
            items=items,
            payment_details=payment_details
        )
