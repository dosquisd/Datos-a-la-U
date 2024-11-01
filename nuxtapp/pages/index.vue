<script setup lang="ts">
    import type { GeoJsonObject } from "geojson";
    import { LMap, LTileLayer, LGeoJson } from "@vue-leaflet/vue-leaflet";
    import { z } from "zod";
    import rawData from "@/data/data.json";

    useHead({
        title: "Home",
    });

    const data = rawData as GeoJsonObject;
    const { department } = useOptions();

    const DataShape = z.object({
        layer: z.object({
            feature: z.object({
                properties: z.object({
                    DPTO: z.string(),
                    NOMBRE_DPT: z.string(),
                }),
            }),
        }),
    });

    function handleClick(event: Event) {
        department.value =
            DataShape.parse(event).layer.feature.properties.NOMBRE_DPT;
    }
</script>

<template>
    <ClientOnly>
        <div class="w-screen h-screen relative">
            <LMap
                class="w-full h-full"
                :zoom="6"
                :center="[4.60971, -74.08175]"
                :max-bounds="[
                    [12.0, -82.0],
                    [-4.0, -66.0],
                ]"
                :use-global-leaflet="false"
            >
                <LTileLayer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    layer-type="base"
                />
                <LGeoJson :geojson="data" @click="handleClick" />
            </LMap>
            <div
                class="absolute top-0 left-0 w-full h-full p-4 z-[1000] grid grid-cols-2 md:grid-cols-3 grid-rows-3 pointer-events-none"
            >
                <Card v-auto-animate class="col-start-1 row-start-3">
                    <CardHeader>
                        <CardTitle>Information</CardTitle>
                        <CardDescription v-if="department">
                            Selected department:
                            <span>{{ department }}</span>
                        </CardDescription>
                    </CardHeader>
                    <CardContent>
                        Lorem ipsum dolor sit amet, consectetur adipisicing
                        elit. Facilis delectus assumenda qui consectetur natus
                        numquam non molestias earum sint? Consequuntur ea
                        corporis distinctio minima facere eos fugit quo
                        accusantium sint.
                    </CardContent>
                </Card>
            </div>
        </div>
    </ClientOnly>
</template>
