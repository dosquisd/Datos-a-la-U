<script setup lang="ts">
    import {
        LMap,
        LTileLayer,
        LMarker,
        LTooltip,
    } from "@vue-leaflet/vue-leaflet";

    useHead({
        title: "Home",
    });

    const mapCenter = useState<[number, number]>("map-center", () => [
        4.60971, -74.08175,
    ]);
    const mapZoom = useState<number>("map-zoom", () => 6);

    const { marks } = useDataMarkers();
    const colorMode = useColorMode();

    async function handleMarkerClicked(mark: Mark) {
        const { markData } = useDataMarkFocus();

        mapCenter.value = [mark.lat, mark.lon];
        markData.value = mark;
    }

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
                :zoom="mapZoom"
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
                        @click="() => handleMarkerClicked({ lat, lon, name })"
                    >
                        <LTooltip>{{ name }}</LTooltip>
                    </LMarker>
                </template>
            </LMap>
            <main
                v-auto-animate
                class="absolute top-0 left-0 w-full h-full p-4 z-[1000] grid sm:grid-cols-2 md:grid-cols-3 xl:grid-cols-4 grid-rows-3 pointer-events-none"
            >
                <section
                    class="h-full w-full flex items-end col-start-1 row-start-3"
                >
                    <div class="w-full space-y-2">
                        <HomeSheetOptions />
                        <HomeSelectDepartment />
                    </div>
                </section>

                <section class="grid-row-0 grid-cols-1 col-start-1 row-start-2">
                    <div>Hola xD</div>
                </section>

                <!-- <div v-for="i in 1" :key="i">
                    {{ i }}
                </div> -->
            </main>
        </div>
    </ClientOnly>
</template>
