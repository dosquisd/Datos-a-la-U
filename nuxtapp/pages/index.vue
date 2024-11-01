<script setup lang="ts">
    import type { GeoJsonObject } from "geojson";
    import { LMap, LTileLayer, LGeoJson } from "@vue-leaflet/vue-leaflet";
    import { z } from "zod";
    import rawData from "@/data/data.json";

    useHead({
        title: "Home",
    });

    const data = rawData as GeoJsonObject;

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
        const { department } = useOptions();

        department.value =
            DataShape.parse(event).layer.feature.properties.NOMBRE_DPT;
    }
</script>

<template>
    <ClientOnly>
        <div class="w-screen h-screen">
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
        </div>
    </ClientOnly>
</template>
