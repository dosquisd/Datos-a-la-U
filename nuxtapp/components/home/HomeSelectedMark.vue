<script setup lang="ts">
    const { markData } = useDataMarkFocus();
</script>

<template>
    <span v-if="markData"> {{ markData.name }} </span>
</template>
