<script setup lang="ts">
    import { capitalize } from "lodash";

    const { departments } = useDataDepartments();
    const { department } = useOptions();
</script>

<template>
    <Select
        :model-value="department"
        @update:model-value="(payload) => (department = payload)"
    >
        <SelectTrigger class="w-full pointer-events-auto">
            <SelectValue placeholder="Selecciona un departamento" />
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
</template>
