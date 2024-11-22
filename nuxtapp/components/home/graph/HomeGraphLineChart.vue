<script setup lang="ts">
    import HomeGraphLineChartTooltip from "@/components/home/graph/HomeGraphLineChartTooltip.vue";
    import { z } from "zod";

    const RealDataShape = z.object({
        date_request: z.string(),
        real_value: z.number(),
    });

    const RealDataShapeArray = z.array(RealDataShape);

    // const PredictedDataShape = z.object({
    //     date_request: z.string(),
    //     predicted_value: z.number(),
    // });

    const ResponseData = z.object({
        real: RealDataShapeArray,
        predicted: z.null(),
    });

    const { markData } = useDataMarkFocus();

    const { data } = await useFetch<unknown>("/data/courthouse-count", {
        baseURL: useRuntimeConfig().public.apiBase,
        query: {
            courthouse: markData.value?.name,
        },
        watch: [markData],
    });

    const parsedData = computed(() => ResponseData.parse(data.value));

    const mergedData = computed(() =>
        merge({
            initial: parsedData.value.real,
            other: parsedData.value.real,
            key: "date_request",
        }),
    );

    const parsedDates = computed(() =>
        mergedData.value.map((item) => ({
            ...item,
            date_request: new Date(item.date_request),
        })),
    );
</script>

<template>
    <LineChart
        :data="parsedDates"
        :categories="['real_value']"
        index="date_request"
        :x-formatter="
            (tick: unknown) => {
                if (typeof tick === 'number' && parsedDates[tick]) {
                    const date = new Date(parsedDates[tick].date_request);

                    const formattedDate = new Intl.DateTimeFormat('es', {
                        day: 'numeric',
                        month: 'long',
                        year: 'numeric',
                    });

                    return formattedDate.format(date);
                }

                return '';
            }
        "
        :custom-tooltip="HomeGraphLineChartTooltip"
    />
</template>
