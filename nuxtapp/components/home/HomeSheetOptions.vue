<template>
    <Sheet>
        <SheetTrigger as-child class="pointer-events-auto">
            <Button variant="ghost"> Options </Button>
        </SheetTrigger>
        <SheetContent class="z-[1000]">
            <SheetHeader>
                <SheetTitle>Options</SheetTitle>
                <SheetDescription>
                    Here you will be hable to customize various parts of the UI
                    to your liking.
                </SheetDescription>
            </SheetHeader>
            <HomeSheetOptionsColorMode class="mt-4" />
        </SheetContent>
    </Sheet>
</template>
