<script setup lang="ts">
    import { LMap, LTileLayer } from "@vue-leaflet/vue-leaflet";
    import { capitalize } from "vue";

    useHead({
        title: "Home",
    });

    const { departments } = useDataDepartments();
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
            </LMap>
            <main
                class="absolute top-0 left-0 w-full h-full p-4 z-[1000] grid grid-cols-2 md:grid-cols-3"
            >
                <section class="h-full w-full flex items-end">
                    <div class="w-full">
                        <Select
                            @update:model-value="
                                (payload) => console.log(payload)
                            "
                        >
                            <SelectTrigger class="w-full pointer-events-auto">
                                <SelectValue placeholder="Department" />
                            </SelectTrigger>
                            <SelectContent class="z-[1000]">
                                <template v-if="departments.length">
                                    <SelectItem
                                        v-for="item in departments"
                                        :key="item"
                                        :value="item"
                                    >
                                        {{ capitalize(item) }}
                                    </SelectItem>
                                </template>
                            </SelectContent>
                        </Select>
                    </div>
                </section>
            </main>
        </div>
    </ClientOnly>
</template>
