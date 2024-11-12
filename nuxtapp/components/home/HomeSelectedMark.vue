<script setup lang="ts">
    const { getDepartmentName } = useDataMarkers();
    const { markData } = useDataMarkFocus();
    const { department } = useOptions();

    const departmentName = computed(
        () =>
            department.value ||
            getDepartmentName(markData.value?.name as string),
    );
</script>

<template>
    <template v-if="markData">
        <Motion
            :initial="{ y: 100, opacity: 0 }"
            :enter="{ y: 0, opacity: 1 }"
            class="h-full"
        >
            <Card
                class="pointer-events-auto bg-slate-50/20 dark:bg-gray-950/10 border-2 dark:border-gray-950 shadow-lg"
            >
                <CardHeader>
                    <CardTitle class="text-lg font-medium">{{
                        markData.name
                    }}</CardTitle>
                    <CardContent class="flex items-start justify-start p-0">
                        <Drawer>
                            <DrawerTrigger as-child>
                                <Button variant="outline">
                                    Mostrar Graficos
                                </Button>
                            </DrawerTrigger>
                            <DrawerContent class="z-[1000]">
                                <DrawerHeader>
                                    <DrawerTitle>{{
                                        departmentName
                                    }}</DrawerTitle>
                                </DrawerHeader>
                                <div class="px-8 py-2">
                                    <div
                                        class="flex flex-col items-center justify-center py-4"
                                    >
                                        <HomeGraphLineChart />
                                    </div>
                                </div>
                            </DrawerContent>
                        </Drawer>
                    </CardContent>
                </CardHeader>
            </Card>
        </Motion>
    </template>
</template>
