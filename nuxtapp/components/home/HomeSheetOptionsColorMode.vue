<script setup lang="ts">
    interface ColorMode {
        value: string;
        icon: string;
        action: () => void;
        active: () => boolean;
    }

    const colorMode = useColorMode();

    const options: ColorMode[] = [
        {
            value: "light",
            icon: "line-md:sunny-loop",
            action: () => (colorMode.preference = "light"),
            active: () => colorMode.preference === "light",
        },
        {
            value: "dark",
            icon: "line-md:moon-filled-alt-loop",
            action: () => (colorMode.preference = "dark"),
            active: () => colorMode.preference === "dark",
        },
    ];
</script>

<template>
    <div class="space-y-4">
        <Separator label="Color Schema" />
        <div class="flex justify-center gap-2">
            <Button
                v-for="{ value, icon, action } in options"
                :key="value"
                variant="outline"
                @click="action"
            >
                <Icon :name="icon" class="text-xl" />
            </Button>
        </div>
    </div>
</template>
