```order-service/
├── src/
│   ├── domain/
│   │   ├── entities/
│   │   │   ├── order.py
│   │   │   ├── session_booking.py
│   │   ├── repositories/
│   │   │   ├── order_repository.py
│   │   │   ├── session_booking_repository.py
│   │   ├── value_objects/
│   │   │   ├── money.py
│   ├── application/
│   │   ├── use_cases/
│   │   │   ├── place_order_use_case.py
│   │   │   ├── book_session_use_case.py
│   │   ├── dtos/
│   │   │   ├── order_dto.py
│   │   │   ├── session_booking_dto.py
│   │   ├── services/
│   │   │   ├── saga_orchestrator.py
│   ├── infrastructure/
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   ├── order_routes.py
│   │   │   ├── main.py
│   │   ├── database/
│   │   │   ├── models/
│   │   │   │   ├── order_model.py
│   │   │   │   ├── session_booking_model.py
│   │   │   ├── repositories/
│   │   │   │   ├── sql_order_repository.py
│   │   │   │   ├── sql_session_booking_repository.py
│   │   │   ├── database.py
│   │   ├── kafka/
│   │   │   ├── producer.py
│   │   │   ├── consumer.py
│   │   ├── redis/
│   │   │   ├── redis_client.py
│   │   ├── grpc_clients/
│   │   │   ├── payment_service_client.py
│   │   ├── observability/
│   │   │   ├── logging.py
│   │   │   ├── tracing.py
│   │   │   ├── metrics.py
│   ├── migrations/
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   ├── versions/
│   ├── schemas/
│   │   ├── order.avsc
│   │   ├── payment.avsc
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── alembic.ini 
```