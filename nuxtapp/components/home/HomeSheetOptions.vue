<template>
    <Sheet>
        <SheetTrigger as-child class="pointer-events-auto">
            <Button variant="ghost"> Opciones </Button>
        </SheetTrigger>
        <SheetContent class="z-[1000]">
            <SheetHeader>
                <SheetTitle>Opciones</SheetTitle>
                <SheetDescription>
                    Aqui podras modificar varias partes de la interfaz para que
                    quede a tu gusto.
                </SheetDescription>
            </SheetHeader>
            <HomeSheetOptionsColorMode class="mt-4" />
        </SheetContent>
    </Sheet>
</template>
