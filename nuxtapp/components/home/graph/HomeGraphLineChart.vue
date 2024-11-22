<script setup lang="ts">
    // import { z } from "zod";

    // const DataShape = z.object({
    //     date_request: z.string(),
    //     value: z.number(),
    // });

    // const DataShapeArray = z.array(DataShape);

    // const ResponseData = z.object({
    //     real: DataShapeArray,
    //     // predicted: z.null(),
    // });

    // const { markData } = useDataMarkFocus();

    // const { data } = await useFetch<unknown>("/data/courthouse-count", {
    //     baseURL: useRuntimeConfig().public.apiBase,
    //     query: {
    //         courthouse: markData.value?.name,
    //     },
    //     watch: [markData],
    // });

    // const parsedData = computed(() => ResponseData.parse(data.value));

    // Dataset para `ObjectShapeA`
    const datasetA = Array.from({ length: 5 }).map((_, i) => ({
        id: `id-${i + 1}`,
        value: Math.floor(Math.random() * 100), // Valor aleatorio entre 0 y 100
        mergeOnField: `common-${i + 1}`, // Campo común
    }));

    // Dataset para `ObjectShapeB`
    const datasetB = Array.from({ length: 5 }).map((_, i) => ({
        key: `key-${i + 1}`,
        enabled: Math.random() > 0.5, // Valor booleano aleatorio
        mergeOnField: `common-${i + 1}`, // Campo común
    }));

    const mergedData = computed(() =>
        merge({
            initial: datasetA,
            other: datasetB,
            key: "mergeOnField",
        }),
    );
</script>

<template>
    <div>
        {{ mergedData }}
    </div>
</template>
