import strawberry
from strawberry.schema.config import StrawberryConfig

# TODO: Add queries
# - Progress, total / organized
# - Mutation to import a shiur


@strawberry.type
class Query:
    example_field: str


# TODO: Add extensions
schema = strawberry.Schema(query=Query, config=StrawberryConfig(auto_camel_case=False))
