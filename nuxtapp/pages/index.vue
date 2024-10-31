<script setup lang="ts">
    import { LMap, LTileLayer } from "@vue-leaflet/vue-leaflet";

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
            </LMap>
        </div>
    </ClientOnly>
</template>
