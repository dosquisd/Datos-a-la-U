<script setup lang="ts">
    const { markData } = useDataMarkFocus();
</script>

<template>
    <template v-if="markData">
        <div
            v-motion="{
                initial: {
                    y: 100,
                    opacity: 0,
                },
                enter: {
                    y: 0,
                    opacity: 1,
                },
            }"
        >
            {{ markData.name }}
        </div>
    </template>
</template>
