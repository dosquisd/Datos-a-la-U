<script setup lang="ts">
    const { markData } = useDataMarkFocus();
</script>

<template>
    <template v-if="markData">
        <Motion :initial="{ y: 100, opacity: 0 }" :enter="{ y: 0, opacity: 1 }">
            {{ markData.name }}
        </Motion>
    </template>
</template>