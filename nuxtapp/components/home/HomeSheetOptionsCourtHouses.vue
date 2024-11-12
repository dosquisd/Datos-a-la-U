<script setup lang="ts">
    import { capitalize } from "lodash";

    interface Option {
        label: string;
        action: () => void;
        message: string;
    }

    const options: Option[] = [
        {
            label: "Mostrar todas las Casas de Justicia",
            action() {
                const { makeMarks } = useDataMarkers();
                const { department } = useOptions();

                makeMarks();
                department.value = "";
            },
            message: "ejecutar",
        },
    ];
</script>

<template>
    <div class="space-y-4">
        <Separator label="Casas de Justicia" />
        <div class="flex flex-col gap-2">
            <div
                v-for="{ label, action, message } in options"
                :key="label"
                class="grid grid-cols-[4fr_1fr] items-center gap-2 px-2"
            >
                <span class="text-sm text-gray-600">{{ label }}</span>
                <Button variant="outline" @click="action">
                    {{ capitalize(message) }}
                </Button>
            </div>
        </div>
    </div>
</template>
