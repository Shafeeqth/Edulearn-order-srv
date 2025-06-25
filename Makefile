proto-gen:
    python -m grpc_tools.protoc -Iprotos --python_out=src/infrastructure/grpc --grpc_python_out=src/infrastructure/grpc src/infrastructure/grpc/protos/order_service.proto
