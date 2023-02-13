from drf_spectacular.extensions import OpenApiSerializerExtension
from drf_spectacular.plumbing import ResolvedComponent

from ...utils import underscore_to_camel


class PolymorphicSerializerExtension(OpenApiSerializerExtension):
    target_class = "vng_api_common.polymorphism.PolymorphicSerializer"
    match_subclasses = True

    def map_serializer(self, auto_schema, direction):
        serializer = self.target
        schema = auto_schema._map_basic_serializer(serializer, direction)
        root_component = auto_schema.resolve_serializer(serializer, direction)
        mapping = {}
        for attr, model_serializer in serializer.discriminator.mapping.items():
            linked_schema = {"allOf": [root_component.ref]}
            root_component_name = linked_schema['allOf'][0]['$ref'].split('/')[-1]
            if model_serializer:
                component = auto_schema.resolve_serializer(model_serializer, direction)

                if component:
                    linked_schema["allOf"].append(component.ref)

            mapping[attr] = f"#/components/schemas/{attr}_{root_component_name}"
            linked_component = ResolvedComponent(
                name=f"{attr}_{root_component_name}", type=ResolvedComponent.SCHEMA, schema=linked_schema
            )

            auto_schema.registry.register_on_missing(linked_component)

        polymorphic_schema = {
            "discriminator": {
                "propertyName": underscore_to_camel(
                    serializer.discriminator.discriminator_field
                ),
                "mapping":mapping
            }
        }

        return {**schema, **polymorphic_schema}
