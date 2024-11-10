import { filteredData } from "@/schema/datashape";

export default function () {
    const { department } = useOptions();
    const marks = computed<Mark[] | undefined>(() => {
        if (!department) return;

        const boundedData = filteredData.find(
            (item) => item.department === department.value,
        );

        if (!boundedData) return;

        return Object.values(boundedData.municipalities)
            .filter((courtHouseData) => courtHouseData !== null)
            .flatMap((courtHouseData) =>
                courtHouseData!.map((courtHouse) => ({
                    lat: parseFloat(courtHouse.lat),
                    lon: parseFloat(courtHouse.lon),
                    name: courtHouse.courthouse,
                })),
            );
    });

    return {
        marks,
    };
}
