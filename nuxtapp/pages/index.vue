<script setup lang="ts">
    import { LMap, LTileLayer, LGeoJson } from "@vue-leaflet/vue-leaflet";
    import type { GeoJsonObject } from "geojson";
    import data from "@/data/data.json";

    useHead({
        title: "Home",
    });
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
                <LGeoJson :geojson="data as GeoJsonObject" />
            </LMap>
        </div>
    </ClientOnly>
</template>
