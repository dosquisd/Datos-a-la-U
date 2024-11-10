<script setup lang="ts">
    import { LMap, LTileLayer, LMarker } from "@vue-leaflet/vue-leaflet";

    useHead({
        title: "Home",
    });

    const mapCenter = useState<[number, number]>("map-center", () => [
        4.60971, -74.08175,
    ]);

    const { marks } = useDataMarkers();
    const colorMode = useColorMode();

    onMounted(() => {
        watch(
            marks,
            (newMarks) => {
                if (!newMarks?.length) {
                    mapCenter.value = [4.60971, -74.08175];
                    return;
                }

                const { lat, lon } = newMarks[0];
                mapCenter.value = [lat, lon];
            },
            { immediate: true },
        );
    });
</script>

<template>
    <ClientOnly>
        <div class="w-screen h-screen relative">
            <LMap
                class="w-full h-full"
                :zoom="6"
                :center="mapCenter"
                :max-bounds="[
                    [16, -86],
                    [-8, -60],
                ]"
                :use-global-leaflet="false"
            >
                <template v-if="colorMode.preference === 'light'">
                    <LTileLayer
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                        layer-type="base"
                    />
                </template>

                <template v-if="colorMode.preference === 'dark'">
                    <LTileLayer
                        url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
                        layer-type="base"
                    />
                </template>

                <template v-if="marks?.length">
                    <LMarker
                        v-for="{ lat, lon, name } in marks"
                        :key="name"
                        :lat-lng="[lat, lon]"
                        @click="() => console.log('clicked')"
                    />
                </template>
            </LMap>
            <main
                class="absolute top-0 left-0 w-full h-full p-4 z-[1000] grid grid-cols-2 md:grid-cols-3 pointer-events-none"
            >
                <section class="h-full w-full flex items-end">
                    <div class="w-full space-y-2">
                        <HomeSheetOptions />
                        <HomeSelectDepartment />
                    </div>
                </section>
            </main>
        </div>
    </ClientOnly>
</template>
