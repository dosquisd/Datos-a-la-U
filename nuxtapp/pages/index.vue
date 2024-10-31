<script setup lang="ts">
    import { LMap, LTileLayer } from "@vue-leaflet/vue-leaflet";
</script>

<template>
    <ClientOnly>
        <div class="w-screen h-screen">
            <LMap
                class="w-full h-full"
                :zoom="6"
                :center="[47.21322, -1.559482]"
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
