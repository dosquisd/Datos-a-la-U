<script setup lang="ts">
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
    <LineChart :data="sortedDataset" :categories="['value']" />
</template>
