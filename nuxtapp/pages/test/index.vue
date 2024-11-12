<script setup lang="ts">
    import CustomTooltip from "@/components/test/CustomTooltip.vue";

    function generateDataset(year: number, numEntries: number) {
        return Array.from({ length: numEntries }).map(() => {
            const month = Math.floor(Math.random() * 12) + 1;
            const day = Math.floor(Math.random() * 28) + 1;
            const date = new Date(year, month - 1, day);
            const value = Math.floor(Math.random() * 100) + 1;

            return {
                date: date,
                value,
            };
        });
    }

    const dataset = generateDataset(2023, 300);
    const sortedDataset = dataset.toSorted(
        (a, b) => Number(a.date) - Number(b.date),
    );
</script>

<template>
    <LineChart
        :data="sortedDataset"
        :categories="['value']"
        index="date"
        :x-formatter="
            (tick: unknown) => {
                if (typeof tick === 'number' && sortedDataset[tick]) {
                    const date = new Date(sortedDataset[tick].date);

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
        :custom-tooltip="CustomTooltip"
    />
</template>
